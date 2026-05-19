# Kapitel 16: Praktiskt exempel från start till börläge

## Varför detta kapitel finns

De tidigare kapitlen har beskrivit arbetssätt, begrepp, perspektiv och kvalitetssäkring var för sig. Det här kapitlet visar hur delarna kan användas tillsammans i ett sammanhållet exempel.

Exemplet är fiktivt, men utformat för att likna ett utvecklingsområde i en större statlig myndighet. Syftet är inte att ge ett facit, utan att visa hur en arkitekt kan resonera från start till börläge.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- följa ett komplett arbetsflöde från uppdrag till börläge
- se hur behov, principer, arkitekturperspektiv, gap och färdplan hänger ihop
- använda ett case för att öva på egna arkitekturbedömningar
- identifiera vilka leverabler som behövs i olika steg
- förstå hur verksamhetsarkitekt och IT-arkitekt kompletterar varandra

## Innan vi börjar

Exemplet använder utvecklingsområdet **Digital ärendehantering**. Området ansvarar för flera tjänster där medborgare, handläggare och andra myndigheter utbyter information i ärenden.

Utvecklingsområdet har ett uttalat behov av att minska variationen mellan ärendeflöden, förbättra informationskvalitet och göra det lättare att bygga nya digitala tjänster.

## Huvudförklaring

### Steg 1: Uppdrag och avgränsning

Arkitektarbetet börjar med ett uppdrag från områdets styrgrupp. Uppdraget är att ta fram ett börläge för Digital ärendehantering med fokus på arbetssätt, information, systemstöd och styrning.

Arkitekterna formulerar en första avgränsning.

| Omfattas | Omfattas inte |
|---|---|
| Ärendeflöden inom utvecklingsområdet | Myndighetens alla ärendetyper |
| Informationsobjekt kopplade till ärenden | Fullständig begreppsmodell för hela myndigheten |
| Systemstöd och integrationer i området | Tekniskt detaljval för varje team |
| Roller och ansvar för informationshantering | Full organisationsöversyn |

Avgränsningen gör arbetet hanterbart. Den gör också tydligt vad som behöver hanteras som beroenden mot andra utvecklingsområden.

### Steg 2: Gemensam problembild

Arkitekterna genomför intervjuer och två workshops. De samlar in problem från handläggare, produktägare, team, informationssäkerhet och förvaltning.

Den gemensamma problembilden sammanfattas i fem observationer:

- liknande ärendeflöden hanteras på olika sätt
- begrepp som ärende, komplettering och beslut används olika
- flera system lagrar överlappande information
- det är oklart vem som äger vissa informationsobjekt
- nya digitala tjänster kräver mycket specialanpassning

Problembilden används inte för att peka ut skuld. Den används för att skapa en gemensam grund för börläget.

### Steg 3: Mål och principer

Utifrån problembilden formuleras tre mål.

| Mål | Förklaring |
|---|---|
| Enhetligare ärendehantering | Liknande ärenden ska följa gemensamma mönster där det är rimligt |
| Tydligare informationsansvar | Centrala informationsobjekt ska ha ägare och kvalitetskrav |
| Lägre förändringskostnad | Nya tjänster ska kunna byggas med mindre specialanpassning |

Arkitekterna föreslår också fyra principer.

- Gemensamma begrepp före lokala varianter.
- Information ska ägas där verksamhetsansvaret finns.
- Nya lösningar ska återanvända etablerade integrationsmönster.
- Övergångslösningar ska ha tydlig livslängd och avvecklingsplan.

Principerna blir ett stöd för senare vägval.

### Steg 4: Börläge för arbetssätt

I börläget används ett gemensamt grundmönster för ärendehantering. Det betyder inte att alla ärenden blir identiska, men att de centrala stegen beskrivs på samma sätt.

Exempel på gemensamma steg:

1. ta emot ärende
2. kontrollera underlag
3. begära komplettering
4. bereda beslut
5. fatta beslut
6. kommunicera beslut
7. arkivera eller avsluta

Verksamhetsarkitekten beskriver vilka variationer som är tillåtna och vilka som behöver styras mer gemensamt.

### Steg 5: Börläge för information

Informationsperspektivet fokuserar på centrala informationsobjekt.

| Informationsobjekt | Beskrivning | Föreslaget ansvar |
|---|---|---|
| Ärende | Samlad hantering av en begäran eller prövning | Processansvarig funktion |
| Part | Person eller organisation kopplad till ärendet | Gemensam informationsförvaltning |
| Underlag | Dokument eller data som krävs för handläggning | Ansvarig verksamhetsfunktion |
| Beslut | Formellt ställningstagande i ärendet | Beslutsansvarig funktion |

Arkitekterna identifierar också informationsflöden mellan e-tjänster, ärendesystem, dokumenthantering och analysstöd.

### Steg 6: Börläge för verktyg och teknik

IT-arkitekten beskriver en målbild där nya tjänster ska använda gemensamma integrationsmönster och tydliga gränssnitt.

Börläget innebär att:

- e-tjänster inte ska direktintegrera med flera interna system utan tydliga tjänstegränssnitt
- ärendeinformation ska kunna hämtas via definierade API:er
- dokument och metadata ska hanteras enligt gemensamma regler
- tekniska speciallösningar ska motiveras och tidsbegränsas
- avveckling av överlappande funktionalitet ska planeras i etapper

Teknikdelen kopplas till informationsmodellen så att systemgränssnitt inte definieras frikopplat från verksamhetens begrepp.

### Steg 7: Börläge för resurser och styrning

Arkitekterna ser att börläget kräver tydligare ansvar. Det räcker inte att beskriva nya modeller och systemmönster.

Följande roller behöver tydliggöras:

- informationsägare
- processansvarig
- produktägare
- arkitekt för utvecklingsområdet
- systemansvarig
- ansvarig för regelverkstolkning

Styrningen behöver också beskriva var beslut tas. Exempelvis behöver förändringar i gemensamma begrepp hanteras på ett annat sätt än teamnära designbeslut.

### Steg 8: Gap-analys

När börläget jämförs med nuläget identifieras flera gap.

| Gap | Konsekvens | Förändringspaket |
|---|---|---|
| Olika begrepp används i olika tjänster | Svårt att återanvända information | Gemensam begreppsmodell |
| Otydligt informationsägarskap | Svag datakvalitet och oklara beslut | Informationsansvar |
| Direktintegrationer mellan system | Hög förändringskostnad | Integrationsmönster |
| Lokala ärendevarianter utan styrning | Svårt att skala arbetssätt | Gemensamt processmönster |
| Överlappande systemstöd | Kostnad och komplexitet | Avvecklingsplan |

Gapen grupperas till förändringspaket som kan användas i färdplanen.

### Steg 9: Färdplan och övergångsarkitektur

Färdplanen delas in i tre etapper.

| Etapp | Fokus | Nytta |
|---|---|---|
| Etapp 1 | Begrepp, ansvar och processmönster | Gemensam riktning |
| Etapp 2 | Integrationsmönster och nya tjänster | Lägre kostnad för nyutveckling |
| Etapp 3 | Avveckling och konsolidering | Minskad komplexitet |

Övergångsarkitekturen beskriver att gamla och nya integrationssätt får samexistera under etapp 2. Den anger också att alla nya initiativ ska följa det nya mönstret om inget undantag beslutas.

### Steg 10: Förankring och beslut

Arkitekterna tar fram olika vyer för olika målgrupper.

| Målgrupp | Vy | Syfte |
|---|---|---|
| Styrgrupp | Färdplan, risker och beslut | Besluta om riktning och etapper |
| Verksamhet | Arbetssätt, roller och begrepp | Förstå konsekvenser i vardagen |
| Utvecklingsteam | API:er, integrationer och övergångsläge | Styra lösningsdesign |
| Arkitekturforum | Helhet och principer | Kvalitetssäkra arkitekturen |

Efter förankring justeras börläget. Ett av besluten flyttas fram eftersom informationsägarskapet behöver förankras bredare.

## Exempel på leverabler

I caset skapas följande leverabler:

- uppdragsbeskrivning
- intressentkarta
- problembild
- mål och principer
- processvy
- informationsvy
- system- och integrationsvy
- ansvarsvy
- gap-analys
- färdplan
- övergångsarkitektur
- beslutsunderlag
- kvalitetschecklista

Alla leverabler behöver inte vara långa dokument. Vissa kan vara en sida, ett diagram eller en tabell. Det viktiga är att de tillsammans stödjer beslut och genomförande.

## Vanliga misstag

- **Misstag: Att försöka lösa hela myndighetens informationsmodell.**
  - Varför det händer: Begreppsfrågor växer snabbt.
  - Hur du undviker det: Håll fokus på utvecklingsområdets ansvar och dokumentera beroenden till myndighetsgemensamma modeller.

- **Misstag: Att beskriva teknik utan verksamhetskoppling.**
  - Varför det händer: Tekniska problem är ofta konkreta och akuta.
  - Hur du undviker det: Koppla varje tekniskt vägval till mål, informationsbehov eller arbetssätt.

- **Misstag: Att färdplanen bara visar systemförändringar.**
  - Varför det händer: Systemleveranser är lättare att planera än arbetssätt och ansvar.
  - Hur du undviker det: Lägg in förändringspaket för roller, styrning och informationsansvar.

- **Misstag: Att förankring sker för sent.**
  - Varför det händer: Arkitekterna vill ha ett färdigt material innan de visar det.
  - Hur du undviker det: Förankra problembild och principer tidigt, innan börläget blir för låst.

## Övningar

### Övning 1: Gör caset mer konkret

Välj ett verkligt eller fiktivt utvecklingsområde. Fyll i motsvarande tabell:

| Fråga | Svar |
|---|---|
| Vad är utvecklingsområdet? | |
| Vilken förändring behövs? | |
| Vilka mål är viktigast? | |
| Vilka perspektiv påverkas mest? | |
| Vilka beslut behövs först? | |

### Övning 2: Identifiera saknade leverabler

Utgå från caset Digital ärendehantering. Anta att styrgruppen ska fatta beslut om etapp 1.

Vilka tre leverabler behöver vara starkast?

Motivera svaret utifrån:

- beslutets karaktär
- risker
- målgrupp
- behov av spårbarhet

### Fördjupning

Bygg en egen enkel övergångsarkitektur för caset. Beskriv:

- vilka gamla lösningar som finns kvar under övergången
- vilka nya regler som gäller för nya initiativ
- hur undantag hanteras
- när övergångsläget ska avvecklas
- vilka risker som behöver följas upp

## Snabb sammanfattning

- Ett sammanhållet case visar hur bokens delar hänger ihop.
- Börläget behöver börja i uppdrag, avgränsning och problembild.
- Principer hjälper arkitekterna att fatta konsekventa vägval.
- Arkitekturperspektiven behöver kopplas ihop, inte hanteras som separata spår.
- Gap-analysen leder vidare till förändringspaket och färdplan.
- Förankring och kvalitetssäkring kan förändra börläget på ett kontrollerat sätt.

## Quiz/reflektionsfrågor

1. Vilken del av caset är viktigast för att skapa gemensam riktning?
2. Varför räcker det inte att bara beskriva system och integrationer?
3. Hur används principerna i exemplet?
4. Vilka övergångsrisker finns i caset?
5. Vilka leverabler skulle du ta fram först i ett verkligt utvecklingsområde?

## Nästa steg

Nästa kapitel samlar mallar och checklistor som kan användas praktiskt i arbetet med börläge och arkitektur. Där finns stöd för intervjuer, workshops, beslut, granskning och kapitelns centrala arbetsmoment.
