# Kapitel 12: Analysera gap och konsekvenser

## Varför detta kapitel finns

När börläget har formulerats och arkitekturperspektiven har fogats samman uppstår nästa viktiga fråga: vad krävs för att ta sig från nuläget till börläget?

En gap- och konsekvensanalys hjälper utvecklingsområdet att förstå skillnaden mellan dagens situation och det önskade läget. Den gör arbetet mer beslutsbart genom att synliggöra förändringsbehov, risker, beroenden, kostnadsdrivare och sådant som behöver hanteras innan färdplanen kan bli trovärdig.

Utan en sådan analys riskerar börläget att bli en attraktiv målbild utan praktisk förankring. Med en genomarbetad analys blir börläget ett underlag för prioritering, planering och styrning.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva vad ett gap är i arkitekturarbete
- skilja mellan gap, konsekvens, risk och beroende
- analysera gap för flera arkitekturperspektiv
- dokumentera konsekvenser på ett sätt som stödjer beslut
- använda analysen som grund för färdplan och övergångsarkitektur

## Innan vi börjar

I tidigare kapitel har vi stegvis byggt upp ett börläge för arbetssätt, resurser, information, verktyg, teknik, regelverk och styrning. I kapitel 11 sammanfogades perspektiven så att arkitekturen kunde granskas som en helhet.

I detta kapitel byter vi fokus från beskrivning till analys. Vi frågar inte längre bara hur börläget ser ut, utan vad skillnaden mellan nuläge och börläge innebär.

## Vad är ett gap?

Ett gap är en identifierad skillnad mellan nuläge och börläge som behöver hanteras för att börläget ska kunna realiseras.

Ett gap kan handla om exempelvis:

- att ett arbetssätt saknas eller inte används konsekvent
- att roller och ansvar är otydliga
- att viktig information inte har en tydlig ägare
- att ett system saknar nödvändigt stöd
- att en integration inte finns
- att en teknisk lösning inte uppfyller säkerhetskrav
- att regelverk tolkas olika i olika delar av organisationen

Ett gap är inte automatiskt ett problem som ska lösas omedelbart. Det är först en skillnad som behöver förstås, värderas och prioriteras.

## Skillnaden mellan gap, konsekvens, risk och beroende

I praktiskt arkitekturarbete blandas dessa begrepp ofta ihop. Det gör analyser svåra att använda, eftersom olika typer av information kräver olika hantering.

| Begrepp | Fråga det svarar på | Exempel |
|---|---|---|
| Gap | Vad skiljer nuläget från börläget? | Dagens informationsmodell saknar gemensamma begrepp för ärendetyp. |
| Konsekvens | Vad innebär gapet om det inte hanteras? | Utvecklingsteam tolkar ärenden olika och bygger olika lösningar. |
| Risk | Vad kan hända, och hur allvarligt är det? | Felaktig datatolkning kan leda till bristande rättssäkerhet. |
| Beroende | Vad måste finnas på plats för att gapet ska kunna hanteras? | Gemensamt begreppsarbete behöver beslutas i arkitekturforum. |

När dessa hålls isär blir analysen mer användbar. Den visar inte bara att något saknas, utan också varför det spelar roll och vad som krävs för att komma vidare.

## En enkel arbetsgång

En gap- och konsekvensanalys kan göras på olika nivåer. För ett utvecklingsområde är det ofta bäst att börja med en enkel struktur och fördjupa den där det behövs.

En praktisk arbetsgång är:

1. Beskriv relevant del av nuläget.
2. Beskriv motsvarande del av börläget.
3. Identifiera gapet.
4. Beskriv konsekvensen om gapet kvarstår.
5. Bedöm risk, nytta och angelägenhet.
6. Identifiera beroenden.
7. Föreslå åtgärd eller fortsatt utredning.
8. Koppla resultatet till färdplanen.

Arbetsgången behöver inte göras lika detaljerat för allt. Vissa gap kan dokumenteras kort. Andra kräver fördjupad analys, särskilt om de påverkar flera utvecklingsområden, säkerhet, juridik, ekonomi eller grundläggande informationsstruktur.

## Analysera per arkitekturperspektiv

Ett bra sätt att börja är att analysera gap per arkitekturperspektiv. Det skapar ordning och gör det lättare att se vilka delar av börläget som är mest krävande.

### Arbetssätt

För arbetssätt bör analysen fokusera på hur arbete utförs, beslutas och följs upp.

Frågor att ställa:

- Vilka processer eller flöden saknas i nuläget?
- Var finns manuella moment som bör automatiseras eller standardiseras?
- Var finns otydliga överlämningar mellan roller eller team?
- Vilka beslut tas i fel forum eller utan rätt underlag?
- Vilka arbetssätt behöver ändras för att börläget ska fungera?

Exempel på gap:

| Nuläge | Börläge | Gap | Konsekvens |
|---|---|---|---|
| Varje team dokumenterar lösningsbeslut på eget sätt. | Gemensam beslutsmall används för arkitekturrelevanta vägval. | Beslut är inte jämförbara eller sökbara. | Det blir svårt att följa upp konsekvenser över tid. |

### Resurser och organisation

För resurser och organisation bör analysen visa om ansvar, kompetens och kapacitet räcker för börläget.

Frågor att ställa:

- Finns de roller som krävs?
- Är ansvarsfördelningen tydlig?
- Finns kompetens för nya arbetssätt, verktyg eller tekniska lösningar?
- Behövs nya forum, mandat eller samverkansformer?
- Finns beroenden till andra utvecklingsområden eller centrala funktioner?

Exempel på gap:

| Nuläge | Börläge | Gap | Konsekvens |
|---|---|---|---|
| Informationsägarskap är informellt. | Informationsägare är utsedda för centrala informationsobjekt. | Mandat och ansvar saknas. | Datakvalitetsfrågor riskerar att hamna mellan roller. |

### Information

Informationsgap är ofta särskilt viktiga i statlig verksamhet eftersom de kan påverka rättssäkerhet, spårbarhet, datakvalitet och återanvändning.

Frågor att ställa:

- Saknas gemensamma begrepp?
- Finns olika tolkningar av samma information?
- Är informationsägarskap tydligt?
- Är informationsflöden dokumenterade?
- Finns krav på gallring, sekretess, arkivering eller spårbarhet som inte hanteras?

Exempel på gap:

| Nuläge | Börläge | Gap | Konsekvens |
|---|---|---|---|
| Samma begrepp används med olika innebörd i olika system. | Gemensam begreppsmodell används i utvecklingsområdet. | Begrepp är inte harmoniserade. | Integrationer och rapportering riskerar att ge felaktiga resultat. |

### Verktyg och teknik

För verktyg och teknik handlar analysen om hur väl nuvarande systemstöd och tekniska lösningar stödjer börläget.

Frågor att ställa:

- Stödjer befintliga verktyg det önskade arbetssättet?
- Finns teknisk skuld som hindrar förändring?
- Behövs nya integrationer eller API:er?
- Finns säkerhetskrav som nuvarande teknik inte uppfyller?
- Finns avvecklingsbehov eller livscykelproblem?

Exempel på gap:

| Nuläge | Börläge | Gap | Konsekvens |
|---|---|---|---|
| Ärendedata flyttas manuellt mellan två system. | Ärendedata överförs via kontrollerad integration. | Integration saknas. | Manuell hantering skapar risk för fel, dubbelarbete och bristande spårbarhet. |

### Regelverk och styrning

Regelverks- och styrningsgap uppstår när börläget kräver tydligare beslut, tolkningar eller kontrollpunkter.

Frågor att ställa:

- Finns juridiska krav som påverkar börläget?
- Är regelverk tolkade och omsatta till praktiska krav?
- Finns beslutspunkter för arkitektur, säkerhet och informationshantering?
- Behövs nya riktlinjer eller uppdaterade styrdokument?
- Finns konflikter mellan lokala arbetssätt och myndighetsgemensamma regler?

Exempel på gap:

| Nuläge | Börläge | Gap | Konsekvens |
|---|---|---|---|
| Regelkrav hanteras sent i utvecklingsarbetet. | Regelkrav beaktas i tidig behovs- och arkitekturanalys. | Kontrollpunkt saknas i processen. | Lösningar kan behöva göras om sent, vilket skapar kostnad och försening. |

## Bedömning av gap

När gapen är identifierade behöver de bedömas. Syftet är inte att skapa en exakt matematisk sanning, utan att ge beslutsfattare och planeringsforum ett bättre underlag.

En enkel bedömning kan använda tre nivåer:

| Bedömningsområde | Låg | Medel | Hög |
|---|---|---|---|
| Verksamhetspåverkan | Begränsad påverkan på enstaka team. | Påverkar flera flöden eller roller. | Påverkar kärnverksamhet, rättssäkerhet eller strategiska mål. |
| Genomförandekomplexitet | Kan hanteras inom teamet. | Kräver samverkan mellan flera parter. | Kräver större beslut, finansiering eller myndighetsgemensam samordning. |
| Brådska | Kan vänta. | Bör planeras inom kommande etapp. | Behöver hanteras tidigt för att undvika stora följdfel. |

Det är ofta bättre att bedöma få dimensioner konsekvent än att införa en avancerad modell som ingen använder.

## Prioritera utan att förenkla bort verkligheten

Gap- och konsekvensanalysen ska hjälpa till att prioritera, men den ska inte dölja komplexitet. Ett gap med hög verksamhetspåverkan kan vara svårt att lösa snabbt. Ett tekniskt gap kan vara litet i sig men blockera flera andra förändringar. Ett juridiskt gap kan kräva tidig hantering även om det inte ger omedelbar verksamhetsnytta.

Prioriteringen bör därför väga ihop:

- verksamhetsnytta
- riskreducering
- regelefterlevnad
- beroenden
- genomförbarhet
- kostnad och resursbehov
- påverkan på andra utvecklingsområden

Resultatet behöver inte vara en detaljerad projektplan. Det ska däremot ge tillräckligt underlag för nästa steg: färdplan och övergångsarkitektur.

## Dokumentera analysen

En gap- och konsekvensanalys bör dokumenteras så att den går att läsa, granska och använda. Undvik att skapa ett stort kalkylblad där alla rader ser lika viktiga ut. Kombinera gärna en sammanfattande vy med mer detaljerade rader.

En användbar mall kan innehålla:

| Fält | Beskrivning |
|---|---|
| ID | Kort identifierare, till exempel GAP-INFO-01. |
| Perspektiv | Arbetssätt, resurser, information, verktyg, teknik eller regelverk. |
| Nuläge | Kort beskrivning av dagens situation. |
| Börläge | Kort beskrivning av önskat läge. |
| Gap | Skillnaden som behöver hanteras. |
| Konsekvens | Vad gapet innebär om det kvarstår. |
| Risknivå | Låg, medel eller hög. |
| Beroenden | Andra beslut, initiativ eller förutsättningar. |
| Föreslagen åtgärd | Rekommenderat nästa steg. |
| Beslutsbehov | Eventuellt beslut som krävs. |

## Exempel: gap som påverkar flera perspektiv

Anta att ett utvecklingsområde vill skapa ett mer sammanhållet digitalt flöde för handläggning. Börläget kräver att information återanvänds mellan steg i processen, att roller har tydliga ansvar och att regelkrav hanteras tidigt.

Ett identifierat gap är att centrala informationsobjekt saknar gemensamma definitioner.

Detta gap hör hemma i informationsperspektivet, men konsekvenserna finns i flera perspektiv:

- Arbetssätt påverkas eftersom handläggare behöver tolka information manuellt.
- Resurser påverkas eftersom specialister måste lägga tid på att reda ut begrepp.
- Verktyg påverkas eftersom system inte kan integreras säkert utan gemensam innebörd.
- Teknik påverkas eftersom API:er och datamodeller riskerar att byggas på olika tolkningar.
- Regelverk påverkas eftersom felaktig tolkning kan få rättsliga konsekvenser.

Detta är ett exempel på ett gap som bör få hög prioritet även om det först kan se ut som en dokumentationsfråga.

## Vanliga misstag

- **Misstag: Att skriva gap som lösningar.**
  - Varför det händer: Gruppen vill snabbt komma vidare till åtgärder.
  - Hur du undviker det: Beskriv först skillnaden mellan nuläge och börläge innan lösningen formuleras.

- **Misstag: Att blanda ihop konsekvens och risk.**
  - Varför det händer: Båda beskriver negativa effekter.
  - Hur du undviker det: Skriv konsekvensen som en direkt följd och risken som något som kan inträffa.

- **Misstag: Att analysera varje perspektiv isolerat.**
  - Varför det händer: Perspektiven har ofta olika ägare eller kompetensområden.
  - Hur du undviker det: Leta aktivt efter gap som påverkar flera perspektiv.

- **Misstag: Att göra analysen för detaljerad för tidigt.**
  - Varför det händer: Arkitekter vill vara noggranna.
  - Hur du undviker det: Börja med en översiktlig analys och fördjupa bara de gap som är viktiga för beslut.

- **Misstag: Att inte koppla analysen till färdplanen.**
  - Varför det händer: Analysen ses som en separat leverabel.
  - Hur du undviker det: Markera vilka gap som måste hanteras i kommande etapper.

## Övningar

### Övning 1: Identifiera gap

Välj ett område där nuläge och börläge redan är beskrivna. Identifiera tre gap.

För varje gap, skriv:

- nuläge
- börläge
- gap
- konsekvens

Kontrollera sedan om gapet verkligen beskriver en skillnad och inte redan är en föreslagen lösning.

### Övning 2: Bedöm påverkan

Välj fem gap från övning 1 eller från ett verkligt utvecklingsområde.

Bedöm varje gap utifrån:

- verksamhetspåverkan
- genomförandekomplexitet
- brådska

Använd nivåerna låg, medel och hög. Diskutera vilka gap som behöver hanteras först och varför.

### Övning 3: Hitta tvärgående konsekvenser

Välj ett informationsgap eller teknikgap. Undersök hur det påverkar minst tre andra arkitekturperspektiv.

Skriv en kort sammanfattning som kan användas i ett beslutsunderlag.

### Fördjupning

Ta fram en enkel gaplogg för ett utvecklingsområde. Använd mallen i kapitlet och fyll i minst tio gap. Markera vilka som bör påverka färdplanen och vilka som kan hanteras inom ordinarie förbättringsarbete.

## Snabb sammanfattning

- Ett gap är skillnaden mellan nuläge och börläge.
- En konsekvens beskriver vad gapet innebär om det kvarstår.
- En risk beskriver något som kan inträffa och hur allvarligt det kan bli.
- Ett beroende visar vad som måste finnas på plats för att gapet ska kunna hanteras.
- Gap bör analyseras per perspektiv, men även granskas tvärgående.
- Analysen ska ge underlag för prioritering, färdplan och beslut.

## Quiz och reflektionsfrågor

1. Vad är skillnaden mellan ett gap och en konsekvens?
2. Varför är informationsgap ofta viktiga i statlig verksamhet?
3. Hur kan ett tekniskt gap påverka arbetssätt och regelverk?
4. Vilka gap i ditt utvecklingsområde behöver hanteras innan andra förändringar kan genomföras?
5. När är det bättre att fördjupa analysen än att gå direkt till lösningsförslag?

## Nästa steg

I nästa kapitel används gap- och konsekvensanalysen som grund för färdplan och övergångsarkitektur. Då går vi från analys till planering: vilka steg bör tas, i vilken ordning och med vilka beslutspunkter?
