#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML saknas. Installera med: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]
META_PATH = ROOT / "docs" / "export-metadata.yaml"
BUILD_DIR = ROOT / "build"
EXPORTS_DIR = ROOT / "exports"


def fail(message: str) -> None:
    print(f"FEL: {message}", file=sys.stderr)
    sys.exit(1)


def warn(message: str) -> None:
    print(f"VARNING: {message}", file=sys.stderr)


def load_metadata() -> dict:
    if not META_PATH.exists():
        fail("docs/export-metadata.yaml saknas.")
    with META_PATH.open("r", encoding="utf-8") as f:
        meta = yaml.safe_load(f) or {}
    for key in ["title", "author", "language", "identifier", "chapters"]:
        if not meta.get(key):
            fail(f"Metadatafält saknas eller är tomt: {key}")
    if meta["language"] not in ("sv", "en"):
        fail("language måste vara 'sv' eller 'en'.")
    if not meta["chapters"] or meta["chapters"][0] != "chapters/00-inledning.md":
        fail("Första kapitlet i metadata måste vara chapters/00-inledning.md.")
    return meta


def split_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def validate_markdown(path: Path) -> list[str]:
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    h1_count = len(re.findall(r"^# ", text, flags=re.MULTILINE))
    if h1_count != 1:
        errors.append(f"{rel}: ska ha exakt en H1-rubrik, hittade {h1_count}.")

    if re.search(r"^####", text, flags=re.MULTILINE):
        errors.append(f"{rel}: innehåller H4 eller djupare rubriker.")

    if text.count("```") % 2 != 0:
        errors.append(f"{rel}: obalanserade kodblock.")

    # Validate image references.
    for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text):
        target = (path.parent / match.group(1)).resolve()
        if not target.exists():
            errors.append(f"{rel}: bild saknas: {match.group(1)}")

    # Validate simple markdown tables.
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and line.strip().endswith("|"):
            cells = split_table_row(line)
            if i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[i + 1]):
                sep_cells = split_table_row(lines[i + 1])
                if len(cells) != len(sep_cells):
                    errors.append(f"{rel}: tabellrad {i+1} har annan cellmängd än separatorraden.")
                j = i + 2
                while j < len(lines) and lines[j].strip().startswith("|") and lines[j].strip().endswith("|"):
                    row_cells = split_table_row(lines[j])
                    if len(row_cells) != len(cells):
                        errors.append(f"{rel}: tabellrad {j+1} har fel antal celler.")
                    j += 1

    return errors


def build_markdown(meta: dict) -> Path:
    BUILD_DIR.mkdir(exist_ok=True)
    out = BUILD_DIR / "book.md"
    parts: list[str] = []

    for rel in meta["chapters"]:
        path = ROOT / rel
        if not path.exists():
            fail(f"Kapitel saknas: {rel}")
        text = path.read_text(encoding="utf-8").strip()
        # Chapter files may use paths relative to chapters/. The merged build file lives in build/,
        # so convert chapter-relative asset paths to project-root-relative paths for Pandoc.
        text = re.sub(r'(!\\[[^\\]]*\\]\\()\\.\\./assets/', r'\\1assets/', text)
        parts.append(text)

    out.write_text("\n\n<div class=\"pagebreak\"></div>\n\n".join(parts) + "\n", encoding="utf-8")
    return out


def run_pandoc(meta: dict, build_md: Path, target: str) -> None:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        fail("Pandoc saknas. Installera Pandoc och kör scriptet igen.")

    EXPORTS_DIR.mkdir(exist_ok=True)
    title = meta["title"]
    author = meta["author"]
    lang = "sv-SE" if meta["language"] == "sv" else "en-US"

    if target == "epub":
        output = EXPORTS_DIR / "ta-fram-borlage-och-arkitektur.epub"
        cmd = [
            pandoc,
            str(build_md),
            "--from=gfm",
            "--to=epub3",
            "--metadata", f"title={title}",
            "--metadata", f"author={author}",
            "--metadata", f"lang={lang}",
            "--metadata", f"identifier={meta.get('identifier', '')}",
            "--css=styles/epub.css",
            "--toc",
            "--toc-depth=3",
            "--output", str(output),
        ]
        cover = meta.get("cover_image")
        if cover and (ROOT / cover).exists():
            cmd.insert(-2, f"--epub-cover-image={cover}")
        subprocess.run(cmd, cwd=ROOT, check=True)
        print(f"Skapade {output}")

    elif target == "pdf":
        output = EXPORTS_DIR / "ta-fram-borlage-och-arkitektur.pdf"
        pdf_engine = shutil.which("xelatex") or shutil.which("lualatex") or shutil.which("pdflatex")
        if not pdf_engine:
            fail("PDF-engine saknas. Installera MacTeX/TinyTeX eller annan Pandoc-kompatibel LaTeX-motor.")
        cmd = [
            pandoc,
            str(build_md),
            "--from=gfm",
            "--pdf-engine", Path(pdf_engine).name,
            "--toc",
            "--toc-depth=3",
            "--metadata", f"title={title}",
            "--metadata", f"author={author}",
            "--metadata", f"lang={lang}",
            "--output", str(output),
        ]
        subprocess.run(cmd, cwd=ROOT, check=True)
        print(f"Skapade {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validera och exportera boken.")
    parser.add_argument("--validate-only", action="store_true", help="Validera utan export.")
    parser.add_argument("--epub", action="store_true", help="Skapa EPUB.")
    parser.add_argument("--pdf", action="store_true", help="Skapa PDF.")
    args = parser.parse_args()

    meta = load_metadata()

    errors: list[str] = []
    for rel in meta["chapters"]:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"Kapitel saknas: {rel}")
        else:
            errors.extend(validate_markdown(path))

    if errors:
        print("Valideringsfel:", file=sys.stderr)
        for err in errors:
            print(f"- {err}", file=sys.stderr)
        sys.exit(1)

    build_md = build_markdown(meta)
    print(f"Validering OK. Sammanslagen markdown: {build_md}")

    if args.validate_only:
        return

    if not args.epub and not args.pdf:
        print("Ingen export vald. Använd --epub, --pdf eller --validate-only.")
        return

    if args.epub:
        run_pandoc(meta, build_md, "epub")
    if args.pdf:
        run_pandoc(meta, build_md, "pdf")


if __name__ == "__main__":
    main()
