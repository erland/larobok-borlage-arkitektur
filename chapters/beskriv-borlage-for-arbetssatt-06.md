# Kapitel 6: Beskriv börläge för arbetssätt

## Varför detta kapitel finns

Ett börläge blir ofta för tekniskt om arbetssätten inte beskrivs tydligt. I en större statlig myndighet är det vanligt att flera utvecklingsområden delar system, information, regler, beroenden och verksamhetsprocesser. Därför behöver arkitekturen visa hur människor, roller, beslut, processer och digitala stöd ska samverka i det framtida läget.

Det här kapitlet hjälper dig att beskriva börläget för arbetssätt på ett sätt som både verksamhet och IT kan använda. Fokus ligger inte på att dokumentera varje detalj i en process, utan på att visa vilka arbetssätt som behöver förändras, varför de behöver förändras och hur de hänger ihop med övriga arkitekturperspektiv.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva vad ett arbetssättsperspektiv bör innehålla i ett börläge
- skilja mellan process, förmåga, roll, ansvar och samverkansform
- identifiera arbetssätt som behöver förändras för att börläget ska bli möjligt
- formulera principer och krav på framtida arbetssätt
- koppla arbetssätt till information, verktyg, teknik, resurser och regelverk

## Innan vi börjar

Tidigare kapitel har etablerat varför börläge behövs, hur arbetet förbereds, hur en gemensam problembild skapas och hur principer och målbild formuleras. Nu börjar vi beskriva själva börläget mer konkret.

Arbetssätt är ett bra första arkitekturperspektiv eftersom det ligger nära verksamhetens vardag. Om arbetssättet är otydligt blir det svårt att bedöma vilka informationsflöden, verktyg, integrationer, resurser och beslut som behövs.

## Vad menas med arbetssätt?

I den här boken betyder arbetssätt det sätt som verksamheten utför, samordnar och förbättrar sitt arbete. Det omfattar både formella processer och mer praktiska samverkansmönster.

Ett arbetssätt kan beskriva:

- vilka aktiviteter som utförs
- i vilken ordning aktiviteterna sker
- vilka roller som deltar
- vilka beslut som behöver fattas
- vilken information som skapas, används eller ändras
- vilka verktyg som stödjer arbetet
- vilka regler och styrande principer som påverkar arbetet
- hur avvikelser, prioriteringar och förbättringar hanteras

Ett vanligt misstag är att likställa arbetssätt med processkartor. Processkartor kan vara viktiga, men arbetssättet är bredare än processens steg. Det handlar också om ansvar, samverkan, styrning, kultur, kompetens och praktiska överenskommelser.

## Börläge för arbetssätt i praktiken

När du beskriver börläget för arbetssätt behöver du svara på fyra frågor:

1. Vilket arbete ska utföras i det framtida läget?
2. Vilka roller eller funktioner ska utföra arbetet?
3. Hur ska arbetet styras, prioriteras och följas upp?
4. Vilka förändringar krävs jämfört med nuläget?

Svaren ska vara tillräckligt tydliga för att kunna vägleda både verksamhetsutveckling och IT-utveckling. De ska däremot inte vara så detaljerade att börläget blir en instruktion för varje handgrepp.

## Rekommenderad arbetsgång

### Steg 1: Utgå från problembilden

Börja med de problem, behov och mål som redan har identifierats. Markera vilka som beror på dagens arbetssätt.

Exempel på arbetssättsproblem kan vara:

- samma ärende hanteras på olika sätt i olika delar av myndigheten
- beslut fattas sent eftersom ansvar är otydligt
- handläggare behöver föra över information manuellt mellan verktyg
- verksamhet och IT använder olika begrepp för samma arbete
- regelefterlevnad kontrolleras först i slutet av processen
- utvecklingsområdet saknar tydliga former för prioritering och uppföljning

Syftet är inte att lösa allt direkt. Syftet är att avgöra vilka arbetssätt som behöver beskrivas i börläget.

### Steg 2: Välj nivå

Alla arbetssätt behöver inte beskrivas på samma detaljnivå. En praktisk indelning är:

| Nivå | Används för | Exempel |
|---|---|---|
| Förmåga | Vad organisationen behöver kunna göra | Hantera ansökan, följa upp tillsyn, dela information |
| Huvudprocess | Hur arbetet flödar över tid | Från inkommet ärende till beslut |
| Delprocess | Hur ett avgränsat arbetsmoment utförs | Granska komplettering |
| Samverkansform | Hur flera aktörer arbetar tillsammans | Gemensam prioritering mellan utvecklingsområden |
| Beslutspunkt | Var styrning eller ansvar behöver vara tydligt | Beslut om undantag, prioritering eller arkitekturavvikelse |

Börläget bör ofta börja på förmåge- och huvudprocessnivå. Detaljerade delprocesser tas bara fram när de behövs för att förstå konsekvenser, ansvar eller systemstöd.

### Steg 3: Beskriv roller och ansvar

Ett börläge för arbetssätt behöver visa vem som gör vad. Det räcker sällan att skriva att “verksamheten ansvarar” eller att “IT stödjer”. Sådana formuleringar blir för otydliga.

Använd hellre roller eller funktioner, till exempel:

- ärendeansvarig
- informationsägare
- processansvarig
- produktägare
- verksamhetsarkitekt
- IT-arkitekt
- säkerhetsansvarig
- dataskyddsfunktion
- utvecklingsteam
- arkitekturforum

Rollerna ska inte alltid motsvara befintliga tjänstetitlar. I börläget beskriver de vilket ansvar som behöver finnas. Senare kan organisationen besluta var ansvaret ska placeras.

### Steg 4: Identifiera styrande principer för arbetssättet

Principer hjälper när flera lösningar är möjliga. De ger riktning utan att detaljstyra.

Exempel på principer för arbetssätt:

- Beslut ska fattas så nära verksamhetskunskapen som möjligt.
- Information ska registreras en gång och återanvändas där det är tillåtet.
- Regelefterlevnad ska byggas in i arbetssättet, inte kontrolleras först i efterhand.
- Arbetssätt ska vara gemensamma där variation inte ger verksamhetsnytta.
- Manuella överlämningar ska minimeras när de skapar risk eller ledtid.

En bra princip ska kunna påverka ett faktiskt vägval. Om principen inte hjälper vid prioritering, design eller granskning är den troligen för allmän.

### Steg 5: Koppla arbetssätt till andra perspektiv

Arbetssättet är aldrig isolerat. Varje viktig förändring i arbetssätt bör kopplas till minst ett annat perspektiv.

| Arbetssättsfråga | Koppling till annat perspektiv |
|---|---|
| Vem fattar beslut? | Resurser, organisation, styrning |
| Vilken information används? | Information, begrepp, datakvalitet |
| Vilket stöd behövs? | Verktyg, teknik, integrationer |
| Vilka regler måste följas? | Regelverk, säkerhet, regelefterlevnad |
| Hur följs arbetet upp? | Mätetal, styrning, ansvar |

Denna koppling gör att börläget inte blir en verksamhetsbeskrivning vid sidan av IT-arkitekturen. Det blir en del av samma arkitektur.

## Exempel: Från problem till börläge

Anta att ett utvecklingsområde har följande problembild:

- handläggning sker olika mellan regioner
- information kompletteras flera gånger
- beslutskriterier tolkas olika
- IT-systemet stödjer inte gemensam uppföljning

Ett svagt börläge skulle kunna säga:

> Arbetssättet ska standardiseras och systemstödet ska förbättras.

Det är för allmänt. Det ger inte tillräcklig vägledning.

Ett starkare börläge kan beskrivas så här:

- Ärendeflödet ska bestå av gemensamma huvudsteg: ta emot, bedöma, komplettera, besluta och följa upp.
- Bedömningskriterier ska vara gemensamt definierade och kopplade till styrande regelverk.
- Kompletteringsbehov ska dokumenteras strukturerat så att de kan följas upp.
- Regioner får anpassa lokala rutiner, men inte ändra gemensamma beslutspunkter eller informationskrav.
- Systemstödet ska stödja spårbarhet mellan ärende, beslut, komplettering och regelgrund.

Det senare exemplet beskriver arbetssätt, ansvar, information, regelverk och systemstöd i ett sammanhang.

## Mall: Beskrivning av arbetssätt i börläge

Använd följande struktur när du dokumenterar ett arbetssätt i börläget.

| Fält | Beskrivning |
|---|---|
| Namn | Kort namn på arbetssättet eller processen |
| Syfte | Varför arbetssättet behövs |
| Omfattning | Vad som ingår och inte ingår |
| Aktörer och roller | Vilka roller som deltar och vilket ansvar de har |
| Huvudsteg | De viktigaste stegen i arbetet |
| Beslutspunkter | Var beslut fattas och av vem |
| Informationsbehov | Vilken information som används eller skapas |
| Verktygsstöd | Vilka verktyg eller system som stödjer arbetet |
| Regelverkskoppling | Vilka regler, riktlinjer eller principer som styr |
| Skillnad mot nuläge | Vad som förändras |
| Öppna frågor | Vad som behöver utredas vidare |

Mallen bör användas konsekvent för centrala arbetssätt, men inte för varje liten rutin.

## Vanliga misstag

- **Misstag: Att börja med systemlösningen.**
  - Varför det händer: IT-arkitekter har ofta god kunskap om tekniska begränsningar och ser snabbt möjliga lösningar.
  - Hur du undviker det: Beskriv först vilket arbete som ska fungera bättre och vilka beslut som behöver stödjas.

- **Misstag: Att rita för detaljerade processkartor för tidigt.**
  - Varför det händer: Det känns konkret och ger sken av kontroll.
  - Hur du undviker det: Börja med huvudflöden, ansvar och beslutspunkter. Detaljera bara där det påverkar arkitekturen.

- **Misstag: Att beskriva arbetssätt utan ansvar.**
  - Varför det händer: Ansvar kan vara organisatoriskt känsligt.
  - Hur du undviker det: Beskriv först nödvändiga roller och ansvar i börläget. Organisationsplacering kan beslutas senare.

- **Misstag: Att acceptera all lokal variation.**
  - Varför det händer: Variation kan upplevas som nödvändig eftersom nuläget fungerar olika på olika ställen.
  - Hur du undviker det: Skilj på variation som ger verksamhetsnytta och variation som skapar risk, kostnad eller otydlighet.

- **Misstag: Att göra arbetssättet fristående från information och teknik.**
  - Varför det händer: Perspektiven dokumenteras ofta var för sig.
  - Hur du undviker det: Koppla varje viktig arbetssättsförändring till informationsbehov, verktygsstöd och tekniska konsekvenser.

## Övningar

### Övning 1: Identifiera arbetssätt som behöver beskrivas

Välj ett utvecklingsområde eller ett pågående initiativ. Lista fem problem i nuläget. Markera vilka problem som beror på arbetssätt, ansvar, beslut eller samverkan.

Skriv sedan vilka två arbetssätt som bör beskrivas först i börläget.

### Övning 2: Skriv ett börläge på rätt nivå

Välj ett arbetssätt och beskriv det med följande rubriker:

- syfte
- huvudsteg
- roller
- beslutspunkter
- informationsbehov
- skillnad mot nuläge

Begränsa beskrivningen till högst en sida. Syftet är att träna på tydlighet, inte fullständighet.

### Övning 3: Koppla arbetssätt till andra perspektiv

För samma arbetssätt, skapa en enkel tabell med fyra kolumner:

| Förändring i arbetssätt | Informationskonsekvens | Verktygs-/teknikkonsekvens | Regelverkskonsekvens |
|---|---|---|---|

Fyll i minst tre rader.

## Fördjupning

För mer erfarna arkitekter kan arbetssättsperspektivet också användas för att identifiera arkitekturella konflikter. Ett exempel är när verksamheten vill ha lokal flexibilitet medan IT och informationsstyrning kräver standardisering.

I sådana fall bör börläget inte dölja konflikten. Det bör beskriva avvägningen öppet:

- Var krävs gemensamt arbetssätt?
- Var är lokal variation tillåten?
- Vilka informationskrav får inte variera?
- Vilka beslut behöver lyftas till styrning eller arkitekturforum?

Detta gör börläget mer användbart som beslutsunderlag.

## Snabb sammanfattning

- Arbetssätt beskriver hur verksamheten utför, samordnar och styr arbetet.
- Ett börläge för arbetssätt ska visa huvudflöden, roller, ansvar, beslutspunkter och förändringar mot nuläget.
- Arbetssätt bör beskrivas på rätt nivå: tillräckligt konkret för beslut, men inte som detaljerade instruktioner.
- Kopplingen till information, verktyg, teknik, resurser och regelverk är avgörande.
- Ett bra arbetssättsperspektiv hjälper både verksamhet och IT att förstå vad arkitekturen ska möjliggöra.

## Quiz/reflektionsfrågor

1. Varför räcker det inte att beskriva arbetssätt som en processkarta?
2. Vad är skillnaden mellan en roll i börläget och en befintlig organisatorisk tjänst?
3. När bör lokal variation i arbetssätt tillåtas?
4. Vilka andra arkitekturperspektiv påverkas när arbetssätt förändras?
5. Hur kan en princip hjälpa när ett arbetssätt ska utformas?

## Nästa steg

Nästa kapitel går vidare till börläge för resurser och organisation. Där fördjupar vi frågor om kompetens, ansvarsfördelning, team, styrning och organisatoriska beroenden.
