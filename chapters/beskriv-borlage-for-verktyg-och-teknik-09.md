# Kapitel 9: Beskriv börläge för verktyg och teknik

## Varför detta kapitel finns

Verktyg och teknik är ofta den del av börläget som får mest uppmärksamhet, särskilt när utvecklingsområdet har många IT-beroenden. Samtidigt är det vanligt att teknikdiskussionen börjar för tidigt. Då riskerar lösningen att styras av befintliga system, enskilda plattformsval eller lokala önskemål innan verksamhetens behov, informationskrav och regelverk är tillräckligt tydliga.

Det här kapitlet hjälper dig att beskriva börläget för verktyg och teknik på ett sätt som stödjer verksamhetsmålen, hänger ihop med informationsarkitekturen och ger tillräckligt underlag för beslut. Målet är inte att skapa en fullständig lösningsdesign. Målet är att beskriva den tekniska riktningen, de viktigaste förmågorna, systemstödet, integrationerna, plattformarna och de arkitekturval som behövs för att utvecklingsområdet ska kunna röra sig mot börläget.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva vilket systemstöd och vilka verktyg som behövs i börläget
- skilja mellan verksamhetsnära verktygsbehov och tekniska lösningsval
- formulera tekniska principer som stödjer målbild, information och arbetssätt
- identifiera viktiga integrationer, beroenden och plattformskrav
- beskriva tekniska konsekvenser utan att gå för långt in i detaljdesign
- bedöma när teknisk fördjupning eller separat lösningsarkitektur behövs

## Innan vi börjar

I kapitel 6 beskrev vi arbetssätt. I kapitel 7 beskrev vi resurser och organisation. I kapitel 8 beskrev vi information. Nu ska dessa delar översättas till behov av verktyg och teknik.

En bra teknisk börlägesbeskrivning börjar därför inte med frågan “vilket system ska vi välja?”. Den börjar med frågor som:

- Vilka arbetsmoment ska stödjas?
- Vilken information ska skapas, användas, delas och skyddas?
- Vilka roller behöver vilket stöd?
- Vilka regelverk och säkerhetskrav påverkar lösningen?
- Vilka beroenden finns till andra utvecklingsområden och gemensamma plattformar?
- Vilka tekniska val är redan styrande?

## Vad menas med verktyg och teknik i börläget?

I den här boken använder vi verktyg och teknik som ett samlingsbegrepp för de digitala stöd, system, plattformar, integrationer, datalager, tekniska komponenter och driftmiljöer som behövs för att börläget ska fungera.

Det är hjälpsamt att skilja mellan fyra nivåer:

| Nivå | Fråga | Exempel |
|---|---|---|
| Verktygsbehov | Vad behöver användaren stöd för? | Söka ärenden, fatta beslut, följa upp status |
| Systemstöd | Vilket digitalt stöd används eller behövs? | Ärendehanteringssystem, beslutsstöd, portal |
| Teknisk förmåga | Vilken teknisk kapacitet krävs? | Integration, behörighet, loggning, spårbarhet |
| Plattform eller komponent | Var och hur realiseras förmågan? | API-plattform, dataplattform, identitetstjänst |

Ett vanligt misstag är att blanda ihop dessa nivåer. Om man skriver “vi behöver system X” när behovet egentligen är “vi behöver kunna dela statusinformation med andra aktörer” blir lösningen snabbt låst. Om man i stället beskriver behovet, den tekniska förmågan och möjliga realiseringsvägar blir börläget mer användbart.

## Utgå från verksamhetsförmågorna

Ett bra sätt att börja är att koppla tekniken till de verksamhetsförmågor som utvecklingsområdet behöver stärka. En verksamhetsförmåga beskriver vad verksamheten behöver kunna göra, oberoende av exakt organisation eller system.

Exempel på förmågor kan vara:

- ta emot och validera information
- handlägga och besluta i ärenden
- dela information med andra myndigheter
- följa upp resultat och kvalitet
- styra behörighet och åtkomst
- dokumentera beslut och spårbarhet

För varje viktig förmåga bör du fråga:

- Vilket nuvarande systemstöd finns?
- Vilket stöd saknas eller fungerar dåligt?
- Vilken information behöver förmågan?
- Vilka användargrupper berörs?
- Vilka krav finns på säkerhet, tillgänglighet och spårbarhet?
- Vilka tekniska beroenden finns till andra områden?

Resultatet behöver inte vara en komplett applikationskarta. Det räcker ofta med en tabell som visar kopplingen mellan förmåga, informationsbehov, befintligt stöd och önskat stöd.

| Förmåga | Informationsbehov | Nuvarande stöd | Börlägesstöd | Kommentar |
|---|---|---|---|---|
| Handlägga ärende | Ärende, beslut, underlag | Flera system och manuella listor | Samlat handläggningsstöd med tydlig status | Kräver gemensam begreppsmodell |
| Följa upp kvalitet | Mätetal, avvikelser, ledtider | Rapporter manuellt sammanställda | Automatiserad uppföljning från gemensam datakälla | Kräver datakvalitet och ägarskap |
| Dela information | Status, beslut, metadata | Filöverföring och e-post | Styrda integrationer via gemensam integrationsförmåga | Kräver informationsklassning |

## Beskriv systemlandskapet på rätt nivå

När verktyg och teknik ska beskrivas är det lätt att skapa antingen för lite eller för mycket detalj. En enkel systemlista räcker sällan. En komplett teknisk lösningsdesign blir ofta för detaljerad för ett börläge. Målet är en mellanform: tillräckligt tydlig för beslut, men inte så detaljerad att den låser framtida design i onödan.

En användbar systemlandskapsbeskrivning bör visa:

- centrala system och verktyg
- vilka verksamhetsförmågor de stödjer
- vilka informationsobjekt de hanterar
- viktiga integrationer
- beroenden till gemensamma plattformar
- system som bör avvecklas, ersättas eller moderniseras
- områden där särskild teknisk analys behövs

Undvik att rita alla system som finns. Fokusera på de system och komponenter som är viktiga för börläget.

### Exempel på enkel systemöversikt

| Komponent | Roll i börläget | Hanterar information | Viktiga beroenden |
|---|---|---|---|
| Handläggningsstöd | Stödjer ärendeflöde och beslut | Ärende, underlag, beslut | Identitet, dokumenthantering, integration |
| Dokument- och arkivstöd | Lagrar och bevarar handlingar | Handling, metadata, arkivreferens | Regelverk, informationssäkerhet |
| Integrationsplattform | Möjliggör informationsutbyte | Meddelanden, status, referenser | API-standarder, säkerhetslösning |
| Uppföljningsstöd | Ger statistik och ledningsinformation | Mätetal, ledtider, avvikelser | Datakälla, begreppsmodell, kvalitetssäkring |

## Identifiera tekniska förmågor

En teknisk förmåga beskriver vad den tekniska miljön behöver kunna stödja. Den är inte samma sak som ett system. En teknisk förmåga kan realiseras genom ett system, en plattform, en tjänst eller en kombination av flera komponenter.

Vanliga tekniska förmågor i större myndigheter är:

- identitet och behörighet
- integration och API-hantering
- loggning och spårbarhet
- dokumenthantering och arkivering
- datadelning och informationsutbyte
- informationssäkerhet och klassning
- uppföljning och analys
- regelstyrning och beslutsstöd
- övervakning och driftsäkerhet
- testdata och testmiljöer
- automatiserad distribution och versionshantering

För varje teknisk förmåga kan börläget beskriva:

- varför förmågan behövs
- vilken verksamhetsnytta den stödjer
- vilka informationsobjekt den berör
- vilka krav som finns på säkerhet och kvalitet
- om förmågan redan finns, behöver förstärkas eller saknas
- vilket forum eller vilken funktion som äger förmågan

## Koppla teknik till informationsarkitektur

Tekniska lösningar blir svaga om de inte bygger på tydlig information. Därför bör varje teknisk börlägesbeskrivning kopplas tillbaka till kapitel 8.

Fråga särskilt:

- Vilka informationsobjekt ska vara masterdata eller auktoritativa källor?
- Var skapas informationen första gången?
- Var ändras den?
- Var används den?
- Vilka system behöver läsa informationen?
- Vilka system får skriva informationen?
- Vilka informationsflöden behöver realtidsstöd och vilka kan vara periodiska?
- Vilken information får delas mellan områden?
- Vilka krav finns på gallring, bevarande och åtkomst?

Om dessa frågor lämnas obesvarade riskerar tekniken att skapa nya dubbellagringar, otydligt ägarskap och bristande spårbarhet.

### Praktisk princip

Beskriv inte en integration bara som “system A skickar data till system B”. Beskriv också vilken information som skickas, varför den skickas, vem som ansvarar för kvaliteten och vilket regelverk som påverkar överföringen.

## Beskriv integrationer och beroenden

I en större myndighet är utvecklingsområden sällan självständiga. Ett utvecklingsområde kan vara beroende av gemensamma tjänster, andra områdens information, centrala plattformar och externa aktörer. Därför är integrationer och beroenden en central del av börläget.

En bra integrationsbeskrivning bör visa:

- vilka parter eller system som utbyter information
- vilken information som utbyts
- riktning på informationsflödet
- frekvens eller händelse som triggar utbytet
- krav på säkerhet, spårbarhet och tillgänglighet
- om integrationen är befintlig, ny eller behöver förändras
- vilket område eller vilken funktion som ansvarar för gränssnittet

| Från | Till | Information | Trigger | Krav | Status i börläge |
|---|---|---|---|---|---|
| Handläggningsstöd | Dokumentstöd | Beslut och metadata | Beslut fattas | Bevarande, spårbarhet | Förändras |
| Extern aktör | Integrationsplattform | Ansökningsinformation | Inkommen ansökan | Autentisering, validering | Ny |
| Handläggningsstöd | Uppföljningsstöd | Ledtider och status | Daglig uppdatering | Datakvalitet | Förstärks |

## Hantera säkerhet från början

Säkerhet ska inte läggas till i slutet av teknikbeskrivningen. I en statlig myndighet påverkar säkerhetskraven både arbetssätt, information, system, integrationer och drift.

I börläget bör du åtminstone beskriva:

- informationsklassning för centrala informationsobjekt
- åtkomstprinciper för olika roller
- behov av autentisering och behörighetsstyrning
- krav på loggning, spårbarhet och uppföljning
- skydd av information i integrationer
- krav på kontinuitet och tillgänglighet
- hantering av testdata
- beroenden till säkerhetsfunktioner och regelverk

Undvik att formulera säkerhet som en allmän ambition, till exempel “lösningen ska vara säker”. Skriv i stället vad säkerhet innebär i sammanhanget.

Exempel:

- Handläggare ska endast se ärenden som tillhör det egna ansvarsområdet.
- Beslut ska loggas med tidpunkt, användare, ärende och beslutsgrund.
- Informationsutbyte med externa aktörer ska ske via godkänd integrationsförmåga.
- Testmiljöer ska inte innehålla produktionsdata om inte data är godkänd och skyddad enligt gällande regler.

## Beskriv teknikval utan att låsa för tidigt

Ett börläge behöver ofta ange teknisk riktning, men det bör inte alltid ange exakt produkt eller detaljdesign. Skillnaden är viktig.

En teknisk riktning kan vara:

- information ska delas via styrda API:er i stället för manuella filöverföringar
- behörighet ska hanteras via gemensam identitets- och åtkomstförmåga
- rapportering ska bygga på definierade informationsobjekt och kvalitetssäkrade datakällor
- nya lösningar ska använda myndighetens etablerade plattformar när de uppfyller behoven
- avvikelser från gemensamma plattformar ska motiveras och beslutas

Ett för tidigt låst teknikval kan vara:

- system X ska användas för alla framtida behov
- all information ska ligga i en viss databas
- alla integrationer ska byggas enligt en specifik teknisk lösning utan analys
- befintligt system ska byggas ut oavsett konsekvenser

Börläget bör därför ange vilka beslut som redan är tagna, vilka val som rekommenderas och vilka frågor som kräver fortsatt lösningsarkitektur.

## Vanliga leverabler

För verktyg och teknik räcker det sällan med löpande text. Följande leverabler är ofta användbara:

- systemlandskapskarta
- tabell över tekniska förmågor
- integrationsöversikt
- beroendekarta
- principer för verktyg och teknik
- lista över system som påverkas
- lista över tekniska beslut som krävs
- risk- och konsekvenslista
- frågor till lösningsarkitektur eller teknisk fördjupning

Alla leverabler behöver inte skapas i varje arbete. Välj de som behövs för att kunna fatta beslut och föra dialog med berörda parter.

## Exempel på tekniska börlägesprinciper

Tekniska principer ska vara konkreta nog att styra, men inte så detaljerade att de ersätter lösningsdesign.

Exempel:

- Information ska skapas en gång och återanvändas där det är möjligt.
- Centrala informationsobjekt ska ha tydligt systemansvar och informationsägarskap.
- Integrationer ska beskrivas med informationsinnehåll, ansvar och säkerhetskrav.
- Nya verktyg ska i första hand använda etablerade gemensamma förmågor.
- Manuell informationsöverföring ska ersättas när den skapar risk, dubbelarbete eller bristande spårbarhet.
- Tekniska avvikelser från gemensamma riktlinjer ska dokumenteras och beslutas.
- Lösningar ska utformas så att regelverk, informationssäkerhet och arkivering kan följas.

## Vanliga misstag

- **Misstag: Att börja med systemval.**
  - Varför det händer: System är konkreta och lätta att diskutera.
  - Hur du undviker det: Börja med förmågor, arbetssätt, information och krav innan du föreslår lösning.

- **Misstag: Att beskriva teknik frikopplat från verksamheten.**
  - Varför det händer: Teknikdelen skrivs ibland avskilt från övriga arkitekturperspektiv.
  - Hur du undviker det: Koppla varje teknisk förmåga till verksamhetsförmåga, informationsobjekt och regelkrav.

- **Misstag: Att rita för detaljerade systemkartor.**
  - Varför det händer: Det finns många system och alla intressenter vill se sina delar.
  - Hur du undviker det: Fokusera på de system och komponenter som påverkar börläget och besluten.

- **Misstag: Att underskatta integrationer.**
  - Varför det händer: Integrationer betraktas som tekniska detaljer.
  - Hur du undviker det: Beskriv informationsflöden, ansvar, säkerhet och beroenden tidigt.

- **Misstag: Att formulera säkerhet som en generell kvalitet.**
  - Varför det händer: Säkerhetskrav lämnas ofta till senare faser.
  - Hur du undviker det: Skriv konkreta krav på åtkomst, loggning, klassning, spårbarhet och skydd.

## Övningar

### Övning 1: Koppla förmågor till systemstöd

Välj tre viktiga verksamhetsförmågor i ditt utvecklingsområde. Fyll i tabellen:

| Förmåga | Informationsbehov | Nuvarande systemstöd | Brist eller risk | Börlägesbehov |
|---|---|---|---|---|
|  |  |  |  |  |

Diskutera sedan om bristen främst handlar om arbetssätt, information, verktyg, teknik eller styrning.

### Övning 2: Beskriv en integration

Välj en viktig integration eller ett viktigt informationsutbyte. Beskriv:

1. vilka parter som ingår
2. vilken information som utbyts
3. varför utbytet behövs
4. vem som ansvarar för informationskvaliteten
5. vilka säkerhets- och regelkrav som påverkar
6. om utbytet bör vara manuellt, halvautomatiserat eller automatiserat i börläget

### Fördjupning: Teknikval och beslut

Lista tre tekniska frågor där utvecklingsområdet behöver ett beslut. För varje fråga, ange:

- vilket problem beslutet ska lösa
- vilka alternativ som finns
- vilka konsekvenser alternativen får
- vem som bör fatta beslutet
- vilken information som saknas innan beslut kan tas

## Snabb sammanfattning

- Verktyg och teknik ska beskrivas som stöd för arbetssätt, information och verksamhetsförmågor.
- Börja inte med systemval om behov, information och regelkrav fortfarande är otydliga.
- Skilj mellan verktygsbehov, systemstöd, teknisk förmåga och plattform.
- Beskriv systemlandskapet på en beslutsnära nivå, inte som fullständig detaljdesign.
- Integrationer ska beskrivas med informationsinnehåll, ansvar, säkerhet och beroenden.
- Säkerhet behöver in i börläget från början.
- Tekniska principer ska styra riktning utan att låsa lösningsdesign för tidigt.

## Quiz/reflektionsfrågor

1. Varför är det riskabelt att börja teknikdelen med systemval?
2. Vad är skillnaden mellan ett verktygsbehov och en teknisk förmåga?
3. Vilka frågor bör ställas innan en integration beskrivs som teknisk lösning?
4. Hur kan informationsarkitekturen påverka teknikval?
5. Vilka säkerhetskrav bör synas redan i börläget?
6. När bör en fråga flyttas från börlägesarbetet till separat lösningsarkitektur?

## Nästa steg

I nästa kapitel går vi vidare till regelverk och styrning. Där beskriver vi hur lagar, interna riktlinjer, beslutspunkter och arkitekturstyrning påverkar börläget. Det är särskilt viktigt eftersom teknikval, informationshantering och arbetssätt i en statlig myndighet behöver kunna motiveras, granskas och förvaltas över tid.
