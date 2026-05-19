# Kapitel 10: Beskriv börläge för regelverk och styrning

## Varför detta kapitel finns

Ett börläge som inte tar hänsyn till regelverk och styrning blir svårt att genomföra i en statlig myndighet. Arkitekturen kan se rimlig ut på papperet, men ändå falla på krav som gäller informationssäkerhet, dataskydd, arkiv, upphandling, intern styrning, ansvarsfördelning eller beslutade myndighetsprinciper.

Det här kapitlet visar hur du beskriver börläget ur perspektivet regelverk och styrning. Målet är inte att göra arkitekten till jurist, säkerhetsspecialist eller styrningsexpert. Målet är att skapa en strukturerad bild av vilka regler, styrsignaler, beslut och ansvar som påverkar utvecklingsområdet.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- identifiera vilka regelverk och styrande dokument som påverkar ett utvecklingsområde
- beskriva hur regler och styrning påverkar börläget
- skilja mellan externa krav, interna styrprinciper och lokala arbetssätt
- formulera arkitekturkonsekvenser av regelkrav
- beskriva beslutspunkter, ansvar och styrforum i börläget
- upptäcka vanliga fallgropar när regelverk hanteras för sent

## Innan vi börjar

I tidigare kapitel har börläget beskrivits genom arbetssätt, resurser, information samt verktyg och teknik. Regelverk och styrning skär igenom alla dessa perspektiv.

Ett krav på informationsklassning påverkar exempelvis både information, teknik, roller och arbetssätt. Ett krav på spårbarhet kan påverka både systemloggning, dokumentation, testning och beslutsprocesser. Ett internt arkitekturforum kan påverka när ett vägval behöver förankras och vem som får fatta beslut.

Därför bör regelverk och styrning inte beskrivas som ett separat sidospår. De ska kopplas till de andra perspektiven och visa vad som faktiskt behöver gälla i börläget.

## Vad räknas som regelverk och styrning?

I den här boken används regelverk och styrning som ett samlingsbegrepp för krav, principer, ansvar och beslut som styr hur utvecklingsområdet får och bör utformas.

### Externa regelverk

Externa regelverk är krav som kommer utifrån myndigheten. Det kan handla om lagar, förordningar, myndighetsföreskrifter, EU-reglering eller andra krav som verksamheten måste följa.

Exempel:

- dataskydd
- offentlighet och sekretess
- arkiv och informationshantering
- informationssäkerhet
- tillgänglighet
- upphandling
- säkerhetsskydd
- krav kopplade till specifik saklagstiftning

Arkitektens uppgift är inte att tolka alla juridiska detaljer själv. Arkitektens uppgift är att se till att regelkraven syns i arkitekturarbetet, att rätt kompetens involveras och att konsekvenserna dokumenteras.

### Interna styrande dokument

Interna styrande dokument är beslutade riktlinjer, principer, policys, målarkitekturer och strategier inom myndigheten.

Exempel:

- arkitekturprinciper
- IT-strategi
- informationssäkerhetspolicy
- molnstrategi
- integrationsprinciper
- data- och informationsprinciper
- riktlinjer för ärendehantering
- principer för utvecklingsområden och produktstyrning

Dessa dokument kan vara mer praktiskt styrande än externa regelverk i vardagen. De påverkar vilka lösningar som är möjliga, vilka forum som ska involveras och vilka avvikelser som behöver motiveras.

### Styrning och beslutsstruktur

Styrning handlar om hur riktning, prioriteringar och beslut tas.

Exempel:

- vilka forum som beslutar om arkitekturvägval
- vem som äger information, processer och system
- hur utvecklingsområdet samverkar med andra utvecklingsområden
- när beslut behöver lyftas till portfölj-, program- eller myndighetsnivå
- hur undantag och avvikelser hanteras
- hur arkitektur följs upp över tid

Ett börläge behöver beskriva styrningen tillräckligt tydligt för att arkitekturen ska kunna genomföras och förvaltas.

## En praktisk arbetsgång

Regelverk och styrning kan kännas stort. Därför är det bra att arbeta i en enkel följd.

### Steg 1: Samla styrande källor

Börja med att samla de källor som redan finns. Undvik att börja med tolkningar. Börja med underlag.

Exempel på källor:

- lagar, föreskrifter och externa krav som verksamheten redan känner till
- myndighetens interna policys och riktlinjer
- beslutade arkitekturprinciper
- tidigare arkitekturgranskningar
- revisionsrapporter eller riskanalyser
- informationsklassningar
- säkerhets- och dataskyddsbedömningar
- beslut från styrgrupper, portföljforum eller arkitekturforum
- beroenden till andra utvecklingsområdens styrning

Samla inte mer än du kan använda. Målet är inte ett komplett regelbibliotek, utan ett relevant beslutsunderlag för börläget.

### Steg 2: Sortera kraven

Nästa steg är att sortera kraven så att de blir hanterbara.

En enkel indelning är:

| Typ | Fråga | Exempel |
|---|---|---|
| Måstekrav | Vad är obligatoriskt? | Lagkrav, säkerhetskrav, arkivkrav |
| Styrprincip | Vad är myndighetens beslutade riktning? | Återanvändning, standardplattform, gemensamma begrepp |
| Rekommendation | Vad bör följas om inget starkt skäl finns att avvika? | Referensarkitektur, riktlinje, etablerad praxis |
| Lokal överenskommelse | Vad gäller för just utvecklingsområdet? | Roller, forum, beslutsvägar, arbetssätt |

Denna sortering hjälper gruppen att skilja på sådant som inte är förhandlingsbart och sådant som kan anpassas.

### Steg 3: Översätt krav till arkitekturkonsekvenser

Ett vanligt problem är att regelkrav dokumenteras utan att konsekvenserna blir tydliga. Skriv därför inte bara att ett regelverk gäller. Beskriv vad det betyder för börläget.

Exempel:

| Regel eller styrsignal | Arkitekturkonsekvens |
|---|---|
| Information ska klassas innan ny behandling införs | Börläget behöver innehålla informationsklassning som steg i arbetssättet |
| Personuppgifter ska hanteras enligt beslutade dataskyddsrutiner | Informationsflöden behöver visa var personuppgifter skapas, lagras och delas |
| Myndigheten ska använda gemensam integrationsplattform | Nya integrationer ska beskrivas som tjänster via den plattformen om inget undantag beslutas |
| Arkitekturbeslut ska granskas i arkitekturforum | Färdplanen behöver innehålla beslutspunkter före större tekniska vägval |

Det är denna översättning som gör regelverksarbetet användbart för arkitekturen.

### Steg 4: Beskriv ansvar och forum

Börläget behöver visa vem som ansvarar för vad. Annars riskerar viktiga frågor att hamna mellan roller.

Beskriv minst:

- vem som äger centrala informationsobjekt
- vem som beslutar om arkitekturavvikelser
- vem som ansvarar för regel- och säkerhetsbedömningar
- vilka forum som behöver involveras
- vilka beslut som kan tas inom utvecklingsområdet
- vilka beslut som behöver lyftas utanför utvecklingsområdet

Det räcker ofta med en enkel ansvarstabell i första versionen.

| Fråga | Ansvarig roll eller funktion | Beslutsforum |
|---|---|---|
| Informationsägarskap | Verksamhetsansvarig eller utsedd informationsägare | Verksamhetsledning eller motsvarande |
| Arkitekturprinciper | Arkitekturfunktion | Arkitekturforum |
| Tekniska undantag | IT-arkitekt tillsammans med plattformsansvarig | Tekniskt forum eller arkitekturforum |
| Dataskyddsfrågor | Dataskyddsfunktion och verksamhetsansvarig | Beslutsforum enligt myndighetens rutin |
| Informationssäkerhet | Säkerhetsfunktion och ansvarig chef | Säkerhets- eller riskforum |

Anpassa tabellen till myndighetens faktiska styrmodell.

## Börlägesbeskrivning för regelverk och styrning

När analysen är gjord bör resultatet sammanfattas i en börlägesbeskrivning.

En användbar struktur är:

1. styrande regelverk och dokument
2. viktigaste styrprinciper
3. arkitekturkonsekvenser
4. beslutspunkter
5. ansvar och forum
6. kända avvikelser eller öppna frågor

### Styrande regelverk och dokument

Lista bara det som påverkar börläget på ett konkret sätt. För varje källa bör du ange varför den är relevant.

Exempel:

| Källa | Relevans för börläget | Påverkar perspektiv |
|---|---|---|
| Informationssäkerhetspolicy | Styr klassning, behörighet och riskhantering | Information, teknik, arbetssätt |
| Arkitekturprinciper | Styr återanvändning, standardisering och integration | Verktyg, teknik, styrning |
| Dataskyddsrutin | Styr behandling av personuppgifter | Information, arbetssätt, regelverk |
| Riktlinje för digital tillgänglighet | Styr utformning av digitala tjänster | Arbetssätt, verktyg, teknik |

### Styrprinciper

Styrprinciper bör vara få, tydliga och användbara.

Exempel:

- Utvecklingsområdet ska återanvända myndighetens gemensamma tjänster där sådana finns.
- Informationsägarskap ska vara tydligt innan nya informationsflöden etableras.
- Nya integrationer ska beskrivas med ansvar, informationsinnehåll, tekniskt gränssnitt och beroenden.
- Avvikelser från målarkitektur ska dokumenteras, motiveras och tidsättas.
- Arkitekturbeslut ska vara spårbara till behov, regelkrav eller strategisk riktning.

En bra styrprincip hjälper gruppen att fatta beslut. En svag styrprincip låter bra men påverkar inget.

### Beslutspunkter

Börläget bör visa när beslut behöver tas. Det gör färdplanen mer realistisk.

Exempel på beslutspunkter:

- beslut om avgränsning av utvecklingsområdet
- beslut om informationsägarskap
- beslut om principer för informationsdelning
- beslut om integrationsmönster
- beslut om tekniska undantag
- beslut om införandeordning
- beslut om riskacceptans
- beslut om förvaltningsansvar

Beslutspunkter bör kopplas till färdplanen. Då blir det tydligt när arkitekturarbetet behöver vara färdigt och vilka frågor som inte kan skjutas upp.

## Exempel: regelverk blir arkitektur

Anta att utvecklingsområdet ska ta fram ett börläge för ett nytt digitalt stöd där både interna handläggare och externa aktörer ska dela information.

Under arbetet identifieras tre styrande krav:

- informationen kan innehålla personuppgifter
- vissa uppgifter kan omfattas av sekretess
- myndigheten har en beslutad integrationsprincip som säger att externa informationsutbyten ska gå via en gemensam integrationsförmåga

Det räcker inte att skriva att dessa krav finns. De behöver omsättas till arkitektur.

Möjliga arkitekturkonsekvenser:

- informationsmodellen ska markera vilka informationsobjekt som kan innehålla personuppgifter
- informationsflöden ska visa var information lämnar myndigheten
- behörighetsmodellen ska skilja mellan interna och externa användare
- integrationer ska beskrivas som tjänster via den gemensamma integrationsförmågan
- färdplanen ska innehålla en beslutspunkt för säkerhets- och dataskyddsbedömning
- arkitekturbeslut om eventuella undantag ska dokumenteras

På så sätt blir regelverket en del av börläget, inte en bilaga som läses i efterhand.

## Vanliga misstag

- **Misstag: Regelverk samlas in men kopplas inte till arkitektur.**
  - Varför det händer: Gruppen vill visa att man tagit hänsyn till reglerna, men hinner inte analysera konsekvenserna.
  - Hur du undviker det: Dokumentera alltid minst en arkitekturkonsekvens per relevant regel eller styrsignal.

- **Misstag: Allt behandlas som lika obligatoriskt.**
  - Varför det händer: Skillnaden mellan lagkrav, intern riktlinje och lokal rekommendation blir otydlig.
  - Hur du undviker det: Sortera krav i måstekrav, styrprinciper, rekommendationer och lokala överenskommelser.

- **Misstag: Juridik, säkerhet och dataskydd involveras för sent.**
  - Varför det händer: Arkitekturarbetet drivs framåt tills någon upptäcker ett krav sent i processen.
  - Hur du undviker det: Identifiera tidiga kontrollpunkter i färdplanen.

- **Misstag: Ansvar beskrivs inte.**
  - Varför det händer: Gruppen fokuserar på system, information och processer men glömmer beslutsmandat.
  - Hur du undviker det: Lägg till ansvarstabell för viktiga styrfrågor.

- **Misstag: Avvikelser från målarkitektur blir osynliga.**
  - Varför det händer: Undantag hanteras muntligt eller i separata forum.
  - Hur du undviker det: Dokumentera avvikelse, motiv, giltighetstid, risk och beslutande forum.

## Övningar

### Övning 1: Skapa en styrkarta

Välj ett utvecklingsområde. Lista fem till tio styrande källor som påverkar området.

För varje källa, skriv:

- vad källan är
- varför den är relevant
- vilket arkitekturperspektiv den påverkar
- vilken person eller funktion som bör involveras

### Övning 2: Översätt krav till konsekvenser

Välj tre regelkrav eller styrprinciper från övning 1. Skriv minst två arkitekturkonsekvenser per krav.

Använd formen:

| Krav eller styrprincip | Konsekvens för börläget | Berört perspektiv |
|---|---|---|

### Övning 3: Identifiera beslutspunkter

Utgå från en preliminär färdplan. Markera var följande beslut behöver tas:

- informationsägarskap
- tekniskt vägval
- säkerhetsbedömning
- dataskyddsbedömning
- arkitekturgranskning
- beslut om eventuellt undantag

Diskutera vilka beslut som kan tas inom utvecklingsområdet och vilka som behöver lyftas.

## Checklista för regelverk och styrning

Använd checklistan när kapitlets perspektiv ska kvalitetssäkras.

- Finns relevanta externa regelverk identifierade?
- Finns relevanta interna styrdokument identifierade?
- Är det tydligt vilka krav som är obligatoriska?
- Är styrprinciper formulerade som praktiskt användbara beslutshjälpmedel?
- Är regelkrav översatta till arkitekturkonsekvenser?
- Finns ansvariga roller eller funktioner beskrivna?
- Finns beslutspunkter kopplade till färdplanen?
- Är avvikelser och undantag synliga?
- Har rätt specialistkompetenser involverats?
- Är kopplingen till information, teknik, arbetssätt och organisation tydlig?

## Snabb sammanfattning

- Regelverk och styrning ska inte hanteras som ett separat sidospår.
- Börläget behöver visa hur externa krav, interna styrdokument och lokala beslut påverkar arkitekturen.
- Det viktigaste arbetet är att översätta krav till arkitekturkonsekvenser.
- Beslutspunkter, ansvar och forum gör börläget genomförbart.
- Tidig involvering av juridik, säkerhet, dataskydd och andra styrfunktioner minskar risken för sena omtag.

## Quiz och reflektionsfrågor

1. Vad är skillnaden mellan ett externt regelverk och ett internt styrdokument?
2. Varför räcker det inte att bara lista relevanta lagar och riktlinjer?
3. Ge ett exempel på hur ett informationssäkerhetskrav kan påverka arbetssätt, information och teknik samtidigt.
4. Vilka beslutspunkter bör finnas i en färdplan när börläget innehåller nya informationsflöden?
5. Hur kan arkitekten undvika att undantag från målarkitektur blir osynliga?

## Nästa steg

I nästa kapitel ska vi sammanfoga arkitekturen. Då kopplas perspektiven arbetssätt, resurser, information, verktyg, teknik samt regelverk och styrning ihop till en gemensam helhet. Målet är att undvika att börläget blir flera separata beskrivningar som inte går att använda tillsammans.
