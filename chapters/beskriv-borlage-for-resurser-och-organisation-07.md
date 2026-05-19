# Kapitel 7: Beskriv börläge för resurser och organisation

## Varför detta kapitel finns

Ett börläge beskriver inte bara hur arbetet ska utföras, utan också vilka förutsättningar som krävs för att arbetssättet ska fungera. I ett utvecklingsområde kan ett nytt arbetssätt falla på att ansvar är otydligt, att kompetenser saknas, att teamen är organiserade runt fel saker eller att beslut behöver tas på flera nivåer utan tydlig samordning.

Det här kapitlet hjälper dig att beskriva börläget för resurser och organisation. Med resurser menas här inte enbart budget och antal personer, utan även kompetenser, roller, mandat, kapacitet, samverkansytor och organisatoriska beroenden.

Målet är att arkitekturen ska visa vilka organisatoriska förmågor som behövs för att börläget ska vara genomförbart.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva vilka resurser och organisatoriska förutsättningar som behövs i ett börläge
- skilja mellan roll, ansvar, mandat, kompetens och kapacitet
- identifiera organisatoriska beroenden mellan utvecklingsområden, linjeorganisation och styrande funktioner
- formulera organisatoriska konsekvenser av ett föreslaget börläge
- koppla resurser och organisation till arbetssätt, information, verktyg, teknik och regelverk

## Innan vi börjar

I kapitel 6 beskrev vi börläget för arbetssätt. Där handlade frågan främst om hur arbete ska utföras, samordnas och styras. Nu går vi ett steg vidare och frågar: vilka människor, kompetenser, ansvar och organisatoriska strukturer krävs för att det arbetssättet ska kunna bli verklighet?

Det är viktigt att inte beskriva organisationen för tidigt och för detaljerat. Ett börläge ska normalt inte bli ett organisationsschema. Däremot behöver det visa om nuvarande ansvarsfördelning, kompetensförsörjning och styrning räcker för det framtida läget.

## Vad menas med resurser och organisation?

I den här boken omfattar resurser och organisation de mänskliga och organisatoriska förutsättningar som behövs för att ett börläge ska fungera.

Perspektivet kan omfatta:

- roller och ansvar
- kompetenser och förmågor
- team, grupper och forum
- mandat och beslutsvägar
- kapacitet och bemanning
- beroenden mellan utvecklingsområden
- koppling till linjeorganisation och styrning

Det handlar alltså både om vem som gör vad och om organisationen har förmåga att göra det över tid.

## Börläge för resurser är inte samma sak som bemanningsplan

En vanlig fallgrop är att göra resursdelen till en lista över personer eller heltidsekvivalenter. Det kan behövas i genomförandeplanering, men det är sällan rätt nivå för arkitekturbeskrivningen.

I arkitekturen bör du i stället fokusera på:

- vilka roller som måste finnas
- vilka ansvar som måste vara tydliga
- vilka kompetenser som måste säkras
- vilka beslut som behöver mandat
- vilka beroenden som måste hanteras
- vilka organisatoriska förändringar som kan krävas

En bemanningsplan svarar på frågan hur många och när. Arkitekturen svarar på frågan vilka förutsättningar som krävs och varför.

## Börja med arbetssättets behov

Det enklaste sättet att beskriva resurs- och organisationsperspektivet är att utgå från de arbetssätt som beskrevs i föregående kapitel.

Ställ frågor som:

- Vilka roller behövs för att utföra arbetssättet?
- Vilka roller behöver fatta beslut?
- Vilka kompetenser krävs för att arbetssättet ska fungera?
- Vilka delar av arbetet kräver samverkan mellan flera utvecklingsområden?
- Vilka aktiviteter kräver stöd från juridik, säkerhet, informationsförvaltning eller drift?
- Finns ansvar som i dag ligger mellan organisatoriska stolar?

När du börjar i arbetssättet blir resursbeskrivningen konkret. Du undviker också att föreslå organisatoriska lösningar som inte har tydlig koppling till verksamhetens behov.

## Roll, ansvar, mandat, kompetens och kapacitet

Fem begrepp återkommer ofta i detta perspektiv. De behöver hållas isär.

| Begrepp | Fråga begreppet besvarar | Exempel |
|---|---|---|
| Roll | Vilken funktion behövs i arbetet? | Verksamhetsarkitekt, produktägare, informationsägare |
| Ansvar | Vad ska rollen säkerställa? | Att begrepp är definierade och förankrade |
| Mandat | Vilka beslut får rollen fatta? | Godkänna informationsmodell inom området |
| Kompetens | Vilken kunskap eller färdighet krävs? | Informationsmodellering, regelverksanalys, integrationsförståelse |
| Kapacitet | Hur mycket tillgänglig tid eller förmåga behövs? | Tillräcklig arkitekturtid under utredning och genomförande |

Om dessa blandas ihop blir börläget otydligt. En roll utan mandat leder ofta till flaskhalsar. Ett ansvar utan kompetens leder till låg kvalitet. Kompetens utan kapacitet leder till att arbetet inte blir gjort.

## Beskriv roller på rätt nivå

I ett utvecklingsområde kan det finnas många roller. Alla behöver inte beskrivas i arkitekturen. Välj de roller som påverkar börlägets genomförbarhet.

En bra rollbeskrivning kan innehålla:

- rollens syfte
- viktigaste ansvar
- viktiga beslut eller mandat
- vilka andra roller den samverkar med
- vilka kompetenser rollen kräver
- om rollen finns i dag eller behöver etableras

Exempel:

| Roll | Syfte i börläget | Viktiga ansvar | Viktiga samverkansytor |
|---|---|---|---|
| Verksamhetsarkitekt | Säkerställa att börläget stödjer verksamhetens mål och arbetssätt | Förmågor, processer, begrepp och verksamhetsregler | IT-arkitekt, produktägare, verksamhetsexperter |
| IT-arkitekt | Säkerställa teknisk sammanhållning och genomförbarhet | Systemstöd, integrationer, tekniska vägval och tekniska risker | Verksamhetsarkitekt, säkerhetsarkitekt, utvecklingsteam |
| Informationsägare | Säkerställa ansvar för centrala informationsmängder | Definitioner, kvalitet, åtkomst och livscykel | Verksamhet, juridik, informationssäkerhet |

Poängen är inte att skapa en komplett rollkatalog. Poängen är att visa vilka roller som är avgörande för börläget.

## Synliggör organisatoriska beroenden

I en större statlig myndighet är ett utvecklingsområde sällan självförsörjande. Det kan bero på andra utvecklingsområden, gemensamma plattformar, centrala stödfunktioner eller externa regelverk.

Exempel på organisatoriska beroenden:

- ett annat utvecklingsområde äger ett system eller en informationsmängd
- en central funktion beslutar om tekniska standarder
- juridik behöver tolka eller godkänna regelverksfrågor
- informationssäkerhet behöver granska åtkomst och skyddsnivå
- drift eller förvaltning behöver kunna ta emot lösningen
- verksamhetslinjen behöver ändra ansvar eller arbetssätt

Beskriv beroenden så konkret som möjligt. Ett användbart format är:

| Beroende | Varför det är viktigt | Risk om det inte hanteras | Föreslagen hantering |
|---|---|---|---|
| Centralt integrationsforum | Nya informationsflöden kräver gemensamma integrationsmönster | Lokala lösningar skapar teknisk skuld | Tidig avstämning och arkitekturbeslut |
| Juridisk funktion | Regelverk påverkar informationsdelning | Börläget blir inte genomförbart | Gemensam tolkning före designbeslut |
| Annat utvecklingsområde | Delar informationsobjekt och systemstöd | Dubbelarbete och motstridiga modeller | Gemensam modellworkshop och ansvarskarta |

## Använd ansvarskarta i stället för organisationsschema

Ett organisationsschema visar formell struktur. En ansvarskarta visar vem som behöver ta ansvar för centrala delar av börläget. I arkitekturarbetet är ansvarskartan ofta mer användbar.

En ansvarskarta kan visa:

- vem som äger en förmåga
- vem som äger information
- vem som fattar beslut
- vem som utför arbetet
- vem som behöver rådfrågas
- vem som behöver informeras

Ett enkelt sätt är att använda en RACI-liknande modell:

| Område | Ansvarig | Utförande | Rådfrågas | Informeras |
|---|---|---|---|---|
| Begreppsmodell | Verksamhetsarkitekt | Verksamhetsexperter | Informationsarkitekt, juridik | Produktledning |
| Teknisk integrationsprincip | IT-arkitekt | Utvecklingsteam | Säkerhetsarkitekt, integrationsforum | Verksamhetsarkitekt |
| Regelverkstolkning | Juridisk funktion | Jurist och verksamhetsexpert | Informationssäkerhet | Arkitekturforum |

Anpassa modellen till myndighetens språk. Det viktiga är inte exakt metodnamn, utan att ansvar och samverkan blir tydliga.

## Bedöm kompetensbehov

Börläget kan kräva kompetenser som inte finns tillräckligt nära utvecklingsområdet i dag. Det behöver synliggöras tidigt, annars riskerar färdplanen att bli orealistisk.

Vanliga kompetensområden i den här typen av arbete är:

- verksamhetsarkitektur
- IT-arkitektur
- informationsarkitektur
- informationssäkerhet
- juridik och regelverkstolkning
- förändringsledning
- produktledning
- upphandling och leverantörsstyrning
- teknisk integration
- datakvalitet och informationsförvaltning

Beskriv inte kompetensbehov som önskelistor. Koppla varje behov till ett konkret börlägeskrav.

Exempel:

- Om börläget kräver gemensamma informationsdefinitioner behövs informationsarkitektur och begreppsmodellering.
- Om börläget kräver ny informationsdelning behövs juridisk analys och informationssäkerhet.
- Om börläget kräver förändrade arbetssätt behövs förändringsledning och verksamhetsförankring.
- Om börläget kräver ny integration behövs integrationsarkitektur och teknisk plattformskunskap.

## Kapacitet och uthållighet

Kapacitet handlar inte bara om hur många personer som finns. Det handlar också om hur mycket tillgänglig tid och uthållighet som finns för att driva förändringen.

I börläget bör du därför bedöma:

- om nyckelroller har tillräcklig tid
- om arkitekturarbetet kan följas genom genomförande
- om beslutsforum har tillräcklig frekvens
- om linjeorganisationen kan ta emot förändringen
- om förvaltning och drift har kapacitet efter införande
- om beroenden kan hanteras inom rimlig tid

Ett börläge som kräver omfattande samordning men saknar kapacitet för samordning är inte realistiskt.

## Koppling till övriga arkitekturperspektiv

Resurser och organisation ska inte beskrivas isolerat. Perspektivet behöver kopplas till övriga perspektiv.

| Perspektiv | Koppling till resurser och organisation |
|---|---|
| Arbetssätt | Roller, ansvar och samverkansformer krävs för att arbetssättet ska fungera |
| Information | Informationsägarskap och kompetens behövs för kvalitet, begrepp och åtkomst |
| Verktyg | Roller behöver kunna använda, förvalta och besluta om verktygsstöd |
| Teknik | Teknisk kompetens, driftansvar och arkitekturbeslut behöver vara tydliga |
| Regelverk | Juridiskt ansvar, regelefterlevnad och styrning behöver kopplas till arbetet |

En bra tumregel är att varje viktig förändring i övriga perspektiv ska ha en organisatorisk motsvarighet. Om ingen äger, förstår eller har mandat för förändringen är den inte färdigbeskriven.

## Arbetsgång

Använd följande arbetsgång när du beskriver resurser och organisation:

1. Utgå från börlägets viktigaste arbetssätt.
2. Identifiera roller som krävs för att arbetssätten ska fungera.
3. Beskriv ansvar, mandat och samverkansytor.
4. Identifiera kompetensbehov.
5. Synliggör organisatoriska beroenden.
6. Bedöm kapacitet och uthållighet.
7. Dokumentera organisatoriska konsekvenser.
8. Stäm av med berörda chefer, produktledning och arkitekturforum.

Arbetsgången kan genomföras som en workshop med arkitekter, produktägare, verksamhetsrepresentanter och relevanta stödfunktioner.

## Workshop: organisatoriska förutsättningar

En enkel workshop kan genomföras på två timmar.

### Syfte

Syftet är att identifiera vilka roller, ansvar, kompetenser och beroenden som krävs för börläget.

### Deltagare

Rekommenderade deltagare:

- verksamhetsarkitekt
- IT-arkitekt
- produktägare eller motsvarande
- representant från verksamheten
- representant från linjeorganisationen
- informationssäkerhet eller juridik vid behov

### Genomförande

1. Börja med ett arbetssätt eller en förändring från börläget.
2. Lista vilka roller som behövs.
3. Markera vilka ansvar som är otydliga.
4. Identifiera vilka beslut som kräver mandat.
5. Lista vilka kompetenser som krävs.
6. Identifiera beroenden till andra områden eller funktioner.
7. Sammanfatta organisatoriska konsekvenser och öppna beslut.

### Leverabler

Efter workshopen bör du ha:

- en preliminär roll- och ansvarskarta
- lista över organisatoriska beroenden
- lista över kritiska kompetensbehov
- frågor som behöver lyftas till styrning eller arkitekturforum

## Exempel

Ett utvecklingsområde ska skapa ett mer sammanhållet stöd för handläggning. I arbetssättsperspektivet har arkitekterna beskrivit att ärenden ska kunna följas över flera processdelar och att verksamheten behöver gemensamma begrepp för status, beslut och komplettering.

När resurs- och organisationsperspektivet analyseras blir flera saker tydliga:

- Ingen roll har tydligt ansvar för begreppsmodellen.
- IT-arkitekten kan beskriva integrationsbehovet, men informationsägarskapet är oklart.
- Juridisk kompetens behöver delta tidigare eftersom informationsdelning påverkas av regelverk.
- Produktägaren har mandat över prioritering i området, men inte över gemensamma informationsdefinitioner.
- Ett annat utvecklingsområde äger ett system som behövs i börläget.

Arkitekturbeskrivningen bör därför inte bara säga att en gemensam begreppsmodell behövs. Den bör också beskriva vilket ansvar, mandat och samverkan som krävs för att modellen ska kunna tas fram, beslutas och förvaltas.

## Vanliga misstag

- **Misstag: Att beskriva personer i stället för roller.**
  - Varför det händer: Det är ofta lättare att utgå från vilka personer som är involverade i dag.
  - Hur du undviker det: Beskriv först roller, ansvar och kompetens. Koppla till personer först i genomförandeplanering.

- **Misstag: Att skapa ett organisationsschema i stället för en ansvarskarta.**
  - Varför det händer: Organisationen känns konkret och lätt att strukturera.
  - Hur du undviker det: Fokusera på ansvar, mandat, samverkan och beroenden.

- **Misstag: Att anta att mandat följer automatiskt av ansvar.**
  - Varför det händer: Rollen ser ansvarig ut på papperet.
  - Hur du undviker det: Fråga vilka beslut rollen faktiskt får fatta och var beslut behöver lyftas.

- **Misstag: Att underskatta kapacitet.**
  - Varför det händer: Börläget beskrivs som en målbild, inte som något som ska genomföras.
  - Hur du undviker det: Bedöm tid, uthållighet, forum och mottagarkapacitet.

- **Misstag: Att missa beroenden utanför utvecklingsområdet.**
  - Varför det händer: Arbetet avgränsas för snävt.
  - Hur du undviker det: Gör en beroendekarta och stäm av med angränsande utvecklingsområden.

## Övningar

### Övning 1: Skapa en roll- och ansvarskarta

Välj ett viktigt arbetssätt från kapitel 6. Identifiera vilka roller som behövs för att arbetssättet ska fungera i börläget.

Beskriv för varje roll:

- syfte
- ansvar
- mandat
- viktigaste samverkansytor
- kompetensbehov

### Övning 2: Identifiera organisatoriska beroenden

Välj en förändring i börläget. Lista minst fem beroenden till andra utvecklingsområden, centrala funktioner eller linjeorganisationen.

För varje beroende, beskriv:

- varför beroendet finns
- vilken risk som uppstår om det inte hanteras
- hur beroendet bör hanteras
- vem som bör ta nästa steg

### Fördjupning

Gå igenom ett befintligt arkitekturdokument. Markera alla ställen där en förändring kräver ansvar, kompetens eller mandat. Kontrollera om detta faktiskt är beskrivet. Om inte, formulera en komplettering.

## Snabb sammanfattning

- Resurser och organisation beskriver de mänskliga och organisatoriska förutsättningarna för börläget.
- Perspektivet ska inte reduceras till bemanning eller organisationsschema.
- Håll isär roll, ansvar, mandat, kompetens och kapacitet.
- Utgå från arbetssätten och identifiera vilka organisatoriska förutsättningar de kräver.
- Synliggör beroenden till andra utvecklingsområden, linjeorganisation och centrala funktioner.
- Ett börläge är inte genomförbart om ansvar, mandat och kompetens saknas.

## Quiz/reflektionsfrågor

1. Varför räcker det inte att beskriva resurser som antal personer?
2. Vad är skillnaden mellan ansvar och mandat?
3. När är en ansvarskarta mer användbar än ett organisationsschema?
4. Vilka organisatoriska beroenden är vanligast i ditt utvecklingsområde?
5. Vilka kompetenser är mest kritiska för att börläget ska kunna realiseras?

## Nästa steg

Nästa kapitel behandlar informationsperspektivet. Där går vi från roller och organisation till de begrepp, informationsobjekt, informationsflöden och kvalitetskrav som börläget behöver bygga på.
