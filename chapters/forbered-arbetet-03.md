# Kapitel 3: Förbered arbetet

## Varför detta kapitel finns

Ett börläge blir sällan bättre än förberedelserna bakom det. Om uppdraget är otydligt, intressenterna saknas eller avgränsningen är för bred riskerar arkitekturarbetet att bli en omfattande dokumentproduktion utan tydlig nytta.

Det här kapitlet visar hur du förbereder arbetet med börläge och tillhörande arkitektur innan workshops, analyser och modelleringsarbete tar fart. Fokus ligger på att skapa rätt förutsättningar: uppdrag, avgränsning, intressenter, material, arbetssätt och beslutspunkter.

För verksamhetsarkitekten är kapitlet särskilt viktigt eftersom det ger struktur åt en roll som ofta rör sig mellan strategi, verksamhetsutveckling och konkret förändringsarbete. För IT-arkitekten tydliggör kapitlet hur tekniska vägval behöver kopplas till verksamhetens behov redan från början.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- formulera ett tydligt uppdrag för framtagning av börläge
- avgränsa ett utvecklingsområde på ett praktiskt sätt
- identifiera viktiga intressenter och deras bidrag
- samla in styrande dokument och tidigare underlag
- planera ett arbetssätt med workshops, analys och förankring
- skapa en första leveransplan för börläge och arkitektur

## Innan vi börjar

I föregående kapitel skilde vi på nuläge, målbild, börläge, gap och färdplan. I det här kapitlet börjar vi använda begreppen praktiskt.

Förberedelsearbetet handlar inte om att veta allt i förväg. Det handlar om att skapa tillräcklig riktning för att kunna arbeta fokuserat och undvika att arkitekturarbetet växer okontrollerat.

En bra tumregel är:

> Förberedelserna ska göra arbetet lättare att starta, inte försöka lösa hela arkitekturen i förväg.

## Börja med uppdraget

Ett uppdrag för att ta fram börläge bör beskriva varför arbetet behövs, vad som ska tas fram och hur resultatet ska användas. Uppdraget behöver inte vara långt, men det behöver vara tillräckligt tydligt för att styra prioriteringar.

### Frågor som uppdraget bör besvara

- Varför behöver utvecklingsområdet ett börläge nu?
- Vilka beslut ska börläget stödja?
- Vilken del av verksamheten eller utvecklingsområdet omfattas?
- Vilka arkitekturperspektiv ska ingå?
- Vilka leverabler förväntas?
- Vem ska godkänna eller förankra resultatet?
- När behöver resultatet finnas tillgängligt?

Ett uppdrag kan till exempel formuleras så här:

> Utvecklingsområdet ska ta fram ett börläge och tillhörande arkitektur för att ge gemensam riktning åt kommande utvecklingsinitiativ. Arbetet ska beskriva önskat läge för arbetssätt, resurser, information, verktyg, teknik och regelverk samt identifiera större gap, beroenden och beslut som behöver hanteras i färdplanen.

Formuleringen är inte perfekt eller komplett, men den gör tre saker tydliga: syfte, omfattning och användning.

## Avgränsa utvecklingsområdet

I en större myndighet kan ett utvecklingsområde vara stort, tvärfunktionellt och beroende av andra områden. Därför måste arkitekten hjälpa gruppen att skilja mellan det som ska lösas inom arbetet och det som bara behöver förstås som beroende.

Avgränsning är inte samma sak som att ignorera omvärlden. Det är ett sätt att hålla arbetet hanterbart.

### Tre typer av avgränsning

| Typ | Fråga | Exempel |
|---|---|---|
| Verksamhetsmässig | Vilka processer, förmågor eller tjänster ingår? | Handläggning, uppföljning eller digital kundkontakt |
| Organisatorisk | Vilka delar av myndigheten berörs direkt? | En avdelning, flera enheter eller ett utvecklingsområde |
| Teknisk | Vilka system, integrationer eller plattformar ingår? | Ett ärendehanteringssystem, dataplattform eller integrationsflöde |

Avgränsningen bör dokumenteras både som text och gärna som enkel visuell bild. Bilden behöver inte vara avancerad. Den ska hjälpa personer att snabbt se vad som är innanför, utanför och beroende av området.

## Skapa en första intressentkarta

Börläget behöver vara förankrat i både verksamhet och IT. Det betyder att intressenterna inte bara är de som ska godkänna resultatet. De är också de som har kunskap, påverkas av förändringen eller kan stoppa genomförandet om de inte är med.

### Vanliga intressentgrupper

- verksamhetsledning
- produktägare eller motsvarande prioriteringsroll
- processägare eller förmågeansvariga
- verksamhetsexperter
- IT-arkitekter
- verksamhetsarkitekter
- informationsarkitekter eller dataansvariga
- säkerhets- och dataskyddsfunktioner
- juridik eller regelverksfunktioner
- utvecklingsteam
- förvaltning och drift
- andra utvecklingsområden med beroenden

För varje intressentgrupp bör du notera vad de bidrar med och när de behöver involveras.

| Intressent | Bidrag | När behövs de? |
|---|---|---|
| Verksamhetsledning | Mål, prioriteringar och mandat | Tidigt och vid beslut |
| Verksamhetsexperter | Nuläge, problem och praktiska behov | Vid analys och validering |
| IT-arkitekter | Teknisk riktning, begränsningar och beroenden | Tidigt och löpande |
| Juridik/dataskydd | Regelverk, risker och tolkningar | Före större vägval |
| Utvecklingsteam | Genomförbarhet och tekniska konsekvenser | Vid gap och färdplan |

## Samla styrande och beskrivande underlag

Innan nya workshops bokas bör arkitekten samla det som redan finns. Det sparar tid och minskar risken att arbetet börjar om från noll.

### Exempel på underlag

- strategier och verksamhetsplaner
- målarkitekturer och arkitekturprinciper
- tidigare utredningar och beslutsunderlag
- processbeskrivningar
- informationsmodeller och begreppsmodeller
- systemkartor och integrationsbeskrivningar
- riskanalyser
- regelverksanalyser
- säkerhets- och dataskyddsbedömningar
- planer, roadmaps och portföljunderlag
- resultat från tidigare workshops

Allt underlag behöver inte vara aktuellt eller korrekt. Poängen är att förstå vad som finns, vad som saknas och vad som behöver verifieras.

### Enkel underlagslogg

| Underlag | Ägare | Status | Kommentar |
|---|---|---|---|
| Verksamhetsstrategi | Ledningsstab | Aktuell | Styrande för målbild |
| Systemkarta | IT-arkitektur | Behöver verifieras | Senast uppdaterad föregående år |
| Processbeskrivning | Verksamhet | Delvis aktuell | Täcker bara huvudflöde |
| Regelverksanalys | Juridik | Saknas | Behöver tas fram eller kompletteras |

## Bestäm arbetssätt

Framtagning av börläge är både analysarbete och samverkansarbete. Om arbetssättet inte bestäms tidigt riskerar processen att bli otydlig: vissa tror att arkitekten ska skriva färdigt själv, andra tror att allt ska lösas i workshops.

Ett fungerande arbetssätt kombinerar normalt fyra delar:

1. Förberedande analys av befintligt underlag.
2. Intervjuer eller korta avstämningar med nyckelpersoner.
3. Workshops där gemensamma bilder tas fram.
4. Förankring och kvalitetssäkring i flera steg.

### Exempel på enkel arbetsrytm

| Vecka | Fokus | Resultat |
|---|---|---|
| 1 | Uppdrag, avgränsning och underlag | Startbild och arbetsplan |
| 2 | Intressenter och nulägesförståelse | Problembild och första gap |
| 3 | Målbild och principer | Riktning för börläge |
| 4 | Arkitekturperspektiv | Utkast per perspektiv |
| 5 | Sammanfogning och konsekvenser | Samlad börlägesbild |
| 6 | Förankring och färdplan | Beslutsunderlag och nästa steg |

Detta är bara ett exempel. Ett större utvecklingsområde kan behöva längre tid, men en rytm med tydliga mellanleveranser är ofta bättre än ett öppet arbete utan slutpunkt.

## Planera leverabler

En vanlig fallgrop är att börja skriva dokument innan man vet vilka leverabler som faktiskt behövs. Leverablerna bör styras av hur resultatet ska användas.

### Typiska leverabler

- uppdragsbeskrivning och avgränsning
- intressentkarta
- nuläges- och problembild
- målbild och arkitekturprinciper
- börläge per arkitekturperspektiv
- sammanhållen arkitekturbild
- gap- och konsekvensanalys
- färdplan eller övergångsarkitektur
- beslutsunderlag
- presentationsmaterial för förankring

Alla leverabler behöver inte vara separata dokument. I många fall är det bättre att ha ett sammanhållet arbetsmaterial med tydliga avsnitt och ett kortare beslutsunderlag för styrning.

## Bestäm beslutspunkter

Arkitekturarbete behöver inte bara producera information. Det behöver leda till beslut. Därför bör beslutspunkter identifieras tidigt.

Exempel på beslutspunkter:

- Godkänna uppdrag och avgränsning.
- Bekräfta målbild och vägledande principer.
- Välja huvudinriktning för börläge.
- Acceptera större gap och konsekvenser.
- Prioritera steg i färdplanen.
- Besluta vilka frågor som ska lyftas till portfölj, ledning eller arkitekturforum.

Beslutspunkterna hjälper också till att visa när arbetet är tillräckligt klart. Ett börläge behöver inte vara fullständigt för att skapa värde, men det behöver vara tillräckligt tydligt för nästa beslut.

## Exempel: första arbetsplan för ett utvecklingsområde

Anta att ett utvecklingsområde ska förbättra digital hantering av ärenden där både verksamhetsprocesser, information, systemstöd och regelverk påverkas.

En första arbetsplan kan se ut så här:

| Del | Innehåll | Resultat |
|---|---|---|
| Start | Bekräfta uppdrag, mål och avgränsning | Start-PM |
| Kunskapsinsamling | Läsa underlag och intervjua nyckelpersoner | Underlagslogg och frågelista |
| Workshop 1 | Gemensam nuläges- och problembild | Prioriterade problem och behov |
| Workshop 2 | Målbild och principer | Utkast till börlägesriktning |
| Workshop 3 | Arkitekturperspektiv | Utkast per perspektiv |
| Analys | Gap, beroenden och konsekvenser | Gaplista och riskbild |
| Förankring | Genomgång med berörda forum | Reviderat börläge |
| Beslut | Presentera rekommenderad riktning | Beslutsunderlag |

## Vanliga misstag

- **Misstag: Att börja modellera innan uppdraget är tydligt.**
  - Varför det händer: Arkitekter vill ofta snabbt skapa struktur.
  - Hur du undviker det: Skriv först en kort uppdragsformulering och låt ansvariga bekräfta den.

- **Misstag: Att avgränsa för snävt.**
  - Varför det händer: Man vill göra arbetet hanterbart.
  - Hur du undviker det: Skilj mellan sådant som ska lösas i området och sådant som måste hanteras som beroende.

- **Misstag: Att bara involvera arkitekter.**
  - Varför det händer: Börläge uppfattas som ett arkitekturdokument.
  - Hur du undviker det: Involvera verksamhet, utveckling, säkerhet, juridik och andra nyckelroller tidigt.

- **Misstag: Att samla underlag men inte värdera det.**
  - Varför det händer: Befintliga dokument känns tryggare än muntliga uppgifter.
  - Hur du undviker det: Markera varje underlag som aktuellt, osäkert, delvis aktuellt eller inaktuellt.

- **Misstag: Att sakna beslutspunkter.**
  - Varför det händer: Fokus ligger på analys och dokumentation.
  - Hur du undviker det: Bestäm tidigt vilka frågor som behöver beslutas och av vem.

## Övningar

### Övning 1: Formulera uppdraget

Skriv en kort uppdragsformulering för ett utvecklingsområde du känner till.

Använd följande struktur:

- Syftet med arbetet är att ...
- Arbetet omfattar ...
- Resultatet ska användas för att ...
- Viktiga beslut som arbetet ska stödja är ...

### Övning 2: Gör en enkel avgränsning

Rita eller skriv en tredelad avgränsning:

- Ingår i utvecklingsområdet.
- Ingår inte.
- Är beroende eller påverkas.

Fundera särskilt på om informationsflöden, regelverk eller tekniska plattformar hamnar utanför trots att de påverkar genomförandet.

### Övning 3: Skapa en intressentkarta

Lista minst tio intressenter eller intressentgrupper.

För varje intressent, skriv:

- vad de kan bidra med
- vilken risk som uppstår om de inte involveras
- när de bör delta i arbetet

### Fördjupning

Välj ett tidigare arkitekturarbete eller förändringsinitiativ. Identifiera vilka problem som hade kunnat undvikas med tydligare förberedelser.

Använd frågorna:

1. Var uppdraget tydligt?
2. Var avgränsningen begriplig?
3. Fanns rätt intressenter med?
4. Hade arbetet tydliga beslutspunkter?
5. Fanns det en gemensam syn på vilka leverabler som skulle tas fram?

## Snabb sammanfattning

- Förberedelsearbetet gör börlägesarbetet fokuserat och genomförbart.
- Uppdraget ska beskriva syfte, omfattning, leverabler och användning.
- Avgränsning handlar om att skilja mellan det som ska lösas, det som inte ingår och det som är beroenden.
- Intressenter behövs både för kunskap, förankring och beslut.
- Befintliga underlag ska samlas in, men också värderas.
- Arbetssättet bör kombinera analys, intervjuer, workshops och förankring.
- Beslutspunkter bör definieras innan arbetet blir för omfattande.

## Quiz/reflektionsfrågor

1. Varför är uppdragsformuleringen viktig innan arkitekturarbetet startar?
2. Vad är skillnaden mellan något som ingår i avgränsningen och något som är ett beroende?
3. Vilka intressenter är ofta lätta att glömma i börlägesarbete?
4. Varför räcker det inte att bara samla in befintliga dokument?
5. Vilka beslutspunkter skulle du rekommendera i början av ett börlägesarbete?

## Nästa steg

När uppdrag, avgränsning, intressenter och arbetssätt är tydliga kan arbetet gå vidare till en gemensam problembild. Nästa kapitel handlar om hur arkitekter kan samla in, strukturera och förankra nulägesförståelse utan att fastna i detaljer.
