# Kapitel 11: Sammanfoga arkitekturen

## Varför detta kapitel finns

När varje arkitekturperspektiv har beskrivits finns en risk att resultatet blir en samling separata dokument: ett om arbetssätt, ett om resurser, ett om information, ett om verktyg och teknik och ett om regelverk. Det kan se komplett ut, men ändå vara svårt att använda som stöd för beslut och genomförande.

Det här kapitlet visar hur perspektiven kan sammanfogas till en helhet. Målet är att börläget ska bli begripligt, spårbart och användbart för både verksamhet, IT, ledning och utvecklingsteam.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför arkitekturperspektiven behöver kopplas ihop
- identifiera beroenden mellan arbetssätt, resurser, information, verktyg, teknik och regelverk
- skapa en sammanhängande arkitekturbeskrivning
- använda en enkel spårbarhetsmodell från mål och behov till arkitekturbeslut
- upptäcka motsägelser, luckor och överlapp mellan perspektiven

## Innan vi börjar

De tidigare kapitlen har behandlat olika delar av börläget. Varje perspektiv har ett eget värde, men börläget blir styrande först när delarna hänger ihop.

Ett beslut om arbetssätt påverkar ofta resurser och verktyg. Ett informationsbehov påverkar teknik, integrationer och ansvar. Ett regelkrav kan påverka både processer, behörigheter och datalagring. Därför behöver arkitekten växla från perspektivvis analys till helhetsanalys.

## Vad innebär det att sammanfoga arkitektur?

Att sammanfoga arkitekturen betyder inte att allt ska pressas in i ett enda stort diagram. Det betyder att arkitekturen ska kunna svara på frågor som rör flera perspektiv samtidigt.

Exempel på sådana frågor är:

- Vilka arbetssätt behöver ändras för att informationsflödet ska fungera?
- Vilka roller måste finnas för att den tekniska lösningen ska kunna förvaltas?
- Vilka regelkrav påverkar val av verktyg, integrationer och datalagring?
- Vilka beroenden finns mellan utvecklingsområdet och andra utvecklingsområden?
- Vilka beslut är redan tagna och vilka behöver eskaleras?

En sammanfogad arkitektur gör det möjligt att se konsekvenser. Den visar inte bara hur en del fungerar, utan hur delarna påverkar varandra.

## Sex perspektiv som en helhet

I den här boken används sex perspektiv:

- arbetssätt
- resurser
- information
- verktyg
- teknik
- regelverk

De ska inte ses som sex separata kapitel i ett dokument, utan som sex ingångar till samma börläge.

Ett praktiskt sätt att arbeta är att skapa en enkel beroendekarta. Den behöver inte vara avancerad. Den ska hjälpa gruppen att se vilka delar som hänger ihop.

| Fråga | Exempel på koppling |
|---|---|
| Vilket arbetssätt krävs? | Processer, roller och beslutspunkter |
| Vilka resurser behövs? | Kompetenser, team, ansvar och finansiering |
| Vilken information används? | Begrepp, datakällor, informationsägare och kvalitet |
| Vilka verktyg behövs? | Systemstöd, handläggarstöd, analysverktyg och samarbetsytor |
| Vilken teknik krävs? | Integrationer, plattformar, säkerhet och drift |
| Vilka regelverk styr? | Lagar, interna riktlinjer, säkerhetskrav och arkitekturprinciper |

Tabellen är inte slutprodukten. Den är ett arbetsredskap för att upptäcka samband.

## Spårbarhet från behov till lösning

En sammanhängande arkitektur behöver vara spårbar. Spårbarhet innebär att det går att följa varför en lösning ser ut som den gör.

En enkel kedja kan se ut så här:

1. Verksamhetsbehov
2. Mål eller princip
3. Krav eller förmåga
4. Arkitekturbeslut
5. Påverkat perspektiv
6. Genomförandeaktivitet

Kedjan behöver inte vara tungrodd. Syftet är att undvika att arkitekturen består av påståenden som inte går att koppla tillbaka till behov eller styrning.

### Exempel

Ett utvecklingsområde behöver minska ledtiden i en viss handläggningsprocess.

Det kan leda till följande spårbarhet:

| Nivå | Exempel |
|---|---|
| Behov | Kortare ledtid och färre manuella överlämningar |
| Mål | Ärenden ska kunna följas genom hela processen |
| Princip | Information ska registreras en gång och återanvändas |
| Arkitekturbeslut | Inför gemensam ärendevy och tydliga informationsägare |
| Påverkade perspektiv | Arbetssätt, information, verktyg och teknik |
| Genomförande | Processändring, begreppsmodell, integration och utbildning |

När kedjan är synlig blir det lättare att förklara varför en viss teknisk eller organisatorisk förändring behövs.

## Identifiera beroenden mellan perspektiv

Beroenden är ofta den viktigaste delen av en sammanfogad arkitektur. De visar vad som måste lösas tillsammans.

Vanliga beroenden är:

- ett nytt arbetssätt kräver nya roller eller ändrat ansvar
- ett informationsflöde kräver gemensamma begrepp
- ett verktygsval kräver tekniska integrationer
- ett regelkrav kräver loggning, behörighet eller gallring
- en teknisk plattform kräver viss kompetens och förvaltningsförmåga
- en förändring i ett utvecklingsområde kräver samverkan med ett annat

Beroenden bör dokumenteras så att de går att använda i prioritering och färdplanering. Alla beroenden behöver inte lösas direkt, men de ska vara synliga.

## Sammanhängande arkitekturvy

En bra helhetsvy visar de viktigaste sambanden utan att försöka visa allt. Den bör vara tillräckligt enkel för att kunna användas i samtal med intressenter.

En användbar helhetsvy kan innehålla:

- utvecklingsområdets mål
- centrala förmågor eller processer
- viktigaste informationsobjekt
- berörda system och verktyg
- större tekniska beroenden
- styrande regelverk och principer
- viktiga arkitekturbeslut
- beroenden till andra utvecklingsområden

Helhetsvyn kan kompletteras med mer detaljerade vyer för respektive perspektiv.

## Kontrollera konsistens

När perspektiven sammanfogas behöver arkitekten aktivt leta efter inkonsekvenser.

Ställ till exempel följande frågor:

- Finns ett mål utan tydlig arkitekturkonsekvens?
- Finns ett arkitekturbeslut utan spårbart behov?
- Finns ett informationsobjekt utan ägare?
- Finns ett nytt arbetssätt utan ansvarig roll?
- Finns en teknisk lösning utan förvaltningsförmåga?
- Finns ett regelkrav som inte syns i arbetssätt, information eller teknik?
- Finns beroenden till andra utvecklingsområden som saknar ägare?

Dessa frågor gör arkitekturen mer robust. De hjälper också till att skilja mellan verkliga beslut och lösa antaganden.

## Hantera motsägelser

När flera perspektiv förs samman blir motsägelser tydligare. Det är positivt. Arkitektens uppgift är inte att dölja motsägelser, utan att göra dem hanterbara.

Vanliga motsägelser är:

- verksamheten vill ha flexibilitet, men regelverket kräver stark standardisering
- ett utvecklingsteam vill välja ett nytt verktyg, men myndigheten har en gemensam plattformsstrategi
- information behöver delas brett, men säkerhetskrav begränsar åtkomst
- ett arbetssätt kräver snabb återkoppling, men beslutsstrukturen är långsam
- en målbild förutsätter kompetens som inte finns tillgänglig

Motsägelser bör formuleras som arkitekturfrågor eller beslutspunkter.

Exempel:

> Ska utvecklingsområdet prioritera lokal snabbhet eller myndighetsgemensam standardisering i val av verktygsstöd?

En sådan formulering gör det möjligt att fatta beslut i rätt forum.

## Från vyer till arkitekturbeslut

En sammanfogad arkitektur ska leda till tydliga arkitekturbeslut. Besluten bör vara få, tydliga och spårbara.

Ett arkitekturbeslut bör beskriva:

- vad som beslutats
- varför beslutet behövs
- vilka alternativ som övervägts
- vilka perspektiv som påverkas
- vilka konsekvenser beslutet får
- vilka risker eller beroenden som finns
- vem som äger beslutet
- när beslutet ska omprövas

Beslut behöver inte alltid vara stora teknikval. Det kan lika gärna vara beslut om gemensamma begrepp, ansvarsfördelning eller arbetssätt.

## Dokumentera helheten lagom detaljerat

En vanlig fallgrop är att försöka göra en komplett arkitekturbeskrivning innan den används. Det leder ofta till stora dokument som få läser.

En mer praktisk nivå är att dokumentera:

- den övergripande helhetsvyn
- centrala beroenden
- beslut och vägval
- risker och öppna frågor
- de vyer som behövs för att förstå och genomföra förändringen

Detaljer ska finnas där de behövs, inte överallt.

## Exempel: sammanfogning i ett utvecklingsområde

Anta att ett utvecklingsområde ska förbättra ett myndighetsgemensamt handläggningsflöde.

Arbetssättsperspektivet visar att handläggningen behöver gå från sekventiella överlämningar till gemensam ärendehantering.

Informationsperspektivet visar att begreppet ärendestatus används olika av flera enheter.

Verktygsperspektivet visar att dagens stöd finns i flera separata system.

Teknikperspektivet visar att integrationer saknas mellan centrala system.

Regelverksperspektivet visar att vissa uppgifter kräver särskild åtkomststyrning och loggning.

Resursperspektivet visar att ingen tydligt äger informationsmodellen.

Om varje perspektiv hanteras separat kan lösningen bli splittrad. När perspektiven sammanfogas blir ett möjligt börläge tydligare:

- gemensamt arbetssätt för ärendehantering
- gemensam begreppsmodell för ärendestatus
- tydligt informationsägarskap
- gemensam ärendevy
- integrationer mellan berörda system
- behörighets- och loggningskrav inbyggda från början
- förvaltningsansvar för både arbetssätt och informationsmodell

Detta är en mer användbar arkitektur än enbart en systemskiss eller en processkarta.

## Vanliga misstag

- **Misstag: Att låta varje perspektiv bli ett eget slutdokument.**
  - Varför det händer: Arbetet delas upp mellan olika specialister.
  - Hur du undviker det: Planera en gemensam sammanfogning där perspektiven jämförs och kopplas ihop.

- **Misstag: Att börja med ett stort helhetsdiagram.**
  - Varför det händer: Man vill visa hela arkitekturen på en gång.
  - Hur du undviker det: Börja med de viktigaste sambanden och bygg ut vyn successivt.

- **Misstag: Att dokumentera samband men inte beslut.**
  - Varför det händer: Analysen stannar vid beskrivning.
  - Hur du undviker det: Avsluta sammanfogningen med tydliga arkitekturfrågor och beslutspunkter.

- **Misstag: Att undvika konflikter mellan perspektiv.**
  - Varför det händer: Gruppen vill behålla samsyn.
  - Hur du undviker det: Formulera konflikter som beslut som behöver tas i rätt forum.

## Övningar

### Övning 1: Skapa en beroendekarta

Välj ett utvecklingsområde eller ett delområde.

Gör följande:

1. Lista tre viktiga mål.
2. Lista de mest relevanta delarna i varje perspektiv.
3. Markera minst fem beroenden mellan perspektiven.
4. Identifiera två beroenden som behöver beslut eller förankring.

### Övning 2: Testa spårbarhet

Välj ett arkitekturbeslut från ett pågående eller fiktivt arbete.

Besvara följande frågor:

1. Vilket behov motiverar beslutet?
2. Vilket mål eller vilken princip stödjer beslutet?
3. Vilka perspektiv påverkas?
4. Vilka konsekvenser får beslutet?
5. Vem behöver förstå eller godkänna beslutet?

### Fördjupning

Skapa en sammanhängande arkitekturvy för ett helt utvecklingsområde. Begränsa vyn till de tio viktigaste sambanden. Jämför sedan vyn med era befintliga dokument och notera vilka delar som saknas, överlappar eller motsäger varandra.

## Snabb sammanfattning

- Arkitekturperspektiven behöver kopplas ihop för att börläget ska bli användbart.
- Sammanfogning handlar om samband, spårbarhet, beroenden och beslut.
- En helhetsvy ska stödja samtal och beslut, inte visa allt.
- Motsägelser mellan perspektiv är viktiga signaler.
- En bra sammanfogad arkitektur visar varför förändringen behövs, vad som påverkas och vilka beslut som krävs.

## Quiz/reflektionsfrågor

1. Varför räcker det inte att beskriva varje arkitekturperspektiv separat?
2. Vad betyder spårbarhet i en arkitekturbeskrivning?
3. Vilka beroenden kan finnas mellan information och teknik?
4. Hur kan ett regelkrav påverka arbetssätt?
5. Vilka tecken visar att ett helhetsdiagram har blivit för detaljerat?

## Nästa steg

När arkitekturen har sammanfogats blir det möjligt att analysera skillnaden mellan nuläge och börläge. Nästa kapitel handlar därför om gap, konsekvenser, risker och genomförbarhet.
