# Inledning

Den här boken handlar om hur verksamhetsarkitekter och IT-arkitekter kan ta fram ett börläge och tillhörande arkitektur för ett utvecklingsområde i en större statlig myndighet.

Boken riktar sig till arkitekter som är relativt nya i rollen, men också till mer erfarna IT-arkitekter som behöver arbeta strukturerat med verksamhets- och informationsnära arkitektur. Den är särskilt användbar när en myndighet har delat in sin utvecklingsorganisation i flera utvecklingsområden och varje område behöver kunna beskriva sin riktning på ett jämförbart sätt.

## Varför boken behövs

I stora organisationer finns ofta många parallella initiativ, många intressenter och flera olika sätt att beskriva verksamhet och IT. Det gör att begrepp som målbild, börläge, roadmap, målarkitektur och lösningsarkitektur lätt blandas ihop.

När begreppen blir otydliga blir även besluten otydliga. Det kan leda till att utvecklingsområden:

- prioriterar utan gemensam målbild
- bygger lösningar som inte hänger ihop
- saknar tydligt informationsansvar
- har svårt att se beroenden mellan verksamhet och IT
- beskriver teknik utan att koppla den till arbetssätt och styrning
- tar fram arkitektur som inte används i beslut

Boken ger ett praktiskt arbetssätt för att undvika detta. Den visar hur börläge, arkitekturperspektiv, gap-analys och färdplan kan kopplas ihop till ett sammanhängande underlag.

## Vad boken hjälper dig att göra

Efter att ha arbetat med boken ska du kunna:

- avgränsa arkitekturarbetet för ett utvecklingsområde
- skapa en gemensam problembild
- formulera mål och principer
- beskriva börläge ur flera arkitekturperspektiv
- koppla ihop arbetssätt, resurser, information, verktyg, teknik och regelverk
- analysera gap och konsekvenser
- ta fram färdplan och övergångsarkitektur
- förankra börläget med olika målgrupper
- kvalitetssäkra arkitekturen innan beslut
- använda mallar och checklistor i praktiskt arbete

## Bokens arkitekturperspektiv

Boken använder sex återkommande perspektiv:

- **Arbetssätt:** hur verksamheten utför arbetet, samverkar och styr flöden.
- **Resurser:** roller, ansvar, kompetenser, team och organisatoriska förutsättningar.
- **Information:** begrepp, informationsobjekt, flöden, informationsägarskap och kvalitet.
- **Verktyg:** systemstöd och digitala hjälpmedel som används i arbetet.
- **Teknik:** tekniska plattformar, integrationer, API:er, säkerhet och lösningsmönster.
- **Regelverk:** lagar, interna riktlinjer, styrande krav och efterlevnad.

Perspektiven ska inte behandlas som separata dokument. De behöver kopplas ihop. Ett nytt arbetssätt kräver ofta nya roller, tydligare informationsansvar, anpassade verktyg, tekniska vägval och kontroll mot regelverk.

## Hur boken är upplagd

Boken är indelad i fem delar.

Den första delen förklarar utvecklingsområdet som kontext och reder ut vad börläge betyder.

Den andra delen beskriver hur arbetet förbereds, hur en gemensam problembild skapas och hur mål och principer formuleras.

Den tredje delen går igenom börläge ur de sex arkitekturperspektiven.

Den fjärde delen visar hur perspektiven sammanfogas, hur gap och konsekvenser analyseras, hur färdplanen tas fram och hur börläget kommuniceras och kvalitetssäkras.

Den femte delen innehåller ett sammanhållet praktiskt exempel och ett mallbibliotek.

## Hur du kan använda boken

Du kan läsa boken från början till slut som en lärobok. Det passar om du är ny i rollen eller vill bygga en gemensam metod.

Du kan också använda den som handbok. Då kan du gå direkt till det kapitel som motsvarar den situation du står i:

- börja i kapitel 3 om du ska starta ett arkitekturarbete
- gå till kapitel 4 om gruppen saknar gemensam problembild
- använd kapitel 6–10 när börläge ska beskrivas per perspektiv
- använd kapitel 12–13 när nuläge ska jämföras med börläge och omsättas till färdplan
- använd kapitel 17 när du behöver mallar och checklistor

Övningarna kan användas individuellt, i arkitektpar eller som underlag i en workshop.

## Vad boken inte försöker täcka

Boken är inte en fullständig metodhandbok för all enterprise architecture. Den ersätter inte myndighetens egna styrmodeller, portföljprocesser, säkerhetsprocesser eller projektmodeller.

Boken går inte heller djupt in i enskilda tekniska plattformar, upphandlingsfrågor, juridiska tolkningar eller detaljerad lösningsdesign. När sådana frågor uppstår ska de hanteras av rätt expertfunktioner.

Bokens fokus är den praktiska bron mellan verksamhetsbehov, arkitektur och genomförbar riktning inom ett utvecklingsområde.

## Läsråd

Läs gärna med ett verkligt utvecklingsområde i åtanke. Boken blir mest användbar när du parallellt prövar frågorna på ett konkret område.

Skriv ned:

- vilka begrepp som behöver förtydligas hos er
- vilka perspektiv som ofta glöms bort
- vilka beslut som saknar bra underlag
- vilka mallar som skulle kunna införas direkt
- vilka delar som behöver anpassas till myndighetens styrning

Boken är tänkt att hjälpa arkitekter skapa riktning, inte att skapa mer dokumentation än nödvändigt.

<div class="pagebreak"></div>

# Kapitel 1: Utvecklingsområdet som arkitekturkontext

## Varför detta kapitel finns

Ett utvecklingsområde är mer än en organisatorisk indelning. Det är en praktisk ram för prioriteringar, styrning, utveckling, förvaltning och förändring. När en större statlig myndighet delar in sin utvecklingsorganisation i flera utvecklingsområden behöver varje område kunna beskriva vart det är på väg och vilken arkitektur som krävs för att komma dit.

Det här kapitlet etablerar den kontext som resten av boken bygger på. Målet är att verksamhetsarkitekter och IT-arkitekter ska få ett gemensamt språk för uppdraget innan arbetet med börläge, arkitekturperspektiv och färdplan börjar.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara vad ett utvecklingsområde är i den här bokens sammanhang
- beskriva varför börläge och arkitektur behöver tas fram tillsammans
- skilja mellan utvecklingsområdets ansvar och arkitektens bidrag
- identifiera centrala intressenter i arbetet
- förstå hur arkitekturperspektiven hänger ihop på en övergripande nivå

## Innan vi börjar

Boken utgår från en större statlig myndighet där utvecklingsorganisationen är indelad i drygt tio utvecklingsområden. Varje utvecklingsområde ansvarar för en del av myndighetens samlade utveckling och behöver kunna fatta beslut som är lokalt användbara men samtidigt fungerar i helheten.

Det betyder att arkitekturarbetet behöver balansera två behov:

- utvecklingsområdet behöver tillräckligt konkreta svar för att kunna prioritera, planera och genomföra förändring
- myndigheten behöver tillräcklig samordning för att undvika dubbelarbete, motstridiga lösningar och lokala särlösningar

## Vad är ett utvecklingsområde?

I den här boken betyder utvecklingsområde en avgränsad del av myndighetens utvecklingsorganisation med ansvar för ett verksamhetsnära eller förmågebaserat område. Ett utvecklingsområde kan omfatta verksamhetsprocesser, informationsmängder, systemstöd, tekniska komponenter, arbetssätt och regelverk.

Ett utvecklingsområde är alltså inte bara ett IT-område. Det är inte heller bara en verksamhetsprocess. Det är en praktisk samverkansyta där verksamhet och IT behöver skapa riktning tillsammans.

Ett utvecklingsområde kan till exempel behöva svara på frågor som:

- Vilka verksamhetsförmågor ska området stärka?
- Vilka arbetssätt behöver förändras?
- Vilken information är central för området?
- Vilka system och tekniska plattformar stödjer området?
- Vilka regler, lagkrav och interna styrningar påverkar lösningarna?
- Vilka beroenden finns till andra utvecklingsområden?

## Arkitektens uppdrag i utvecklingsområdet

Arkitektens uppdrag är inte att skapa dokument för dokumentens skull. Uppdraget är att hjälpa utvecklingsområdet att fatta bättre beslut, tidigare och med större konsekvensmedvetenhet.

Verksamhetsarkitekten bidrar främst med att beskriva verksamhetens förmågor, processer, informationsbehov, ansvar, mål och förändringsbehov. IT-arkitekten bidrar främst med att beskriva system, integrationer, tekniska vägval, plattformar, säkerhet och teknisk genomförbarhet.

I praktiken överlappar rollerna ofta. Det är bra. Börläge och arkitektur blir starkare när verksamhet och IT inte arbetar i separata spår.

### Ett gemensamt ansvar

Ett vanligt misstag är att dela upp arbetet så att verksamhetsarkitekten beskriver behov och IT-arkitekten beskriver lösning. Det skapar lätt ett glapp mellan mål och genomförande.

Ett mer användbart arbetssätt är att arkitekterna gemensamt skapar spårbarhet från behov till arkitektur:

1. Vad behöver utvecklingsområdet uppnå?
2. Vilka förmågor, arbetssätt och informationsflöden påverkas?
3. Vilka lösningsprinciper och tekniska förutsättningar behövs?
4. Vilka förändringar behöver ske i vilken ordning?
5. Vilka beslut krävs för att gå vidare?

## Börläge och arkitektur hör ihop

Ett börläge beskriver ett önskat framtida läge. Arkitekturen beskriver hur detta läge hänger ihop och vilka strukturer, principer och vägval som krävs för att nå dit.

Om börläget tas fram utan arkitektur riskerar det att bli en vision utan genomförbarhet. Om arkitekturen tas fram utan ett tydligt börläge riskerar den att bli teknisk dokumentation utan riktning.

I den här boken används därför följande arbetsprincip:

> Börläget beskriver vart utvecklingsområdet ska. Arkitekturen beskriver hur helheten behöver hänga ihop för att utvecklingsområdet ska kunna ta sig dit.

## Arkitekturperspektiven

Boken använder sex arkitekturperspektiv:

- arbetssätt
- resurser
- information
- verktyg
- teknik
- regelverk

Perspektiven ska inte behandlas som isolerade dokument. De är olika sätt att förstå samma förändring.

| Perspektiv | Fråga perspektivet hjälper till att besvara |
|---|---|
| Arbetssätt | Hur ska arbetet utföras och styras? |
| Resurser | Vilka roller, kompetenser och organisatoriska förutsättningar behövs? |
| Information | Vilken information behövs, skapas, delas och förvaltas? |
| Verktyg | Vilka stöd, system och användarnära verktyg behövs? |
| Teknik | Vilka tekniska komponenter, integrationer och plattformar krävs? |
| Regelverk | Vilka lagar, policyer, riktlinjer och beslut styr området? |

### Varför perspektiven behöver kopplas ihop

Ett nytt arbetssätt kan kräva nya informationsflöden. Nya informationsflöden kan kräva ändringar i system och integrationer. Nya systemlösningar kan påverkas av säkerhetskrav, dataskydd, förvaltningsansvar och regelverk. Ett börläge blir användbart först när dessa samband är synliga.

Därför behöver arkitekterna inte bara beskriva perspektiven var för sig, utan också visa relationerna mellan dem.

## Intressenter i arbetet

Ett utvecklingsområde har ofta många intressenter. Alla behöver inte vara lika involverade hela tiden, men de behöver förstå sin roll i arbetet.

Vanliga intressenter är:

- utvecklingsområdets ledning eller produktledning
- verksamhetsexperter
- verksamhetsarkitekter
- IT-arkitekter
- lösningsarkitekter
- informationsarkitekter
- säkerhetsfunktioner
- jurister eller regelverksexperter
- produktägare och team
- förvaltningsorganisation
- andra utvecklingsområden
- centrala arkitektur- eller styrningsforum

En viktig uppgift tidigt i arbetet är att avgöra vilka som ska bidra med kunskap, vilka som ska fatta beslut och vilka som behöver förstå konsekvenserna.

## Exempel: när kontexten är otydlig

Tänk dig ett utvecklingsområde som ska modernisera handläggningsstöd. Verksamheten vill minska ledtider, IT vill minska teknisk skuld och ledningen vill öka automatiseringsgraden. Alla tre målen är rimliga, men de pekar inte automatiskt mot samma lösning.

Om arkitekturarbetet börjar direkt i teknikfrågor kan viktiga verksamhetsval missas. Om arbetet börjar direkt i processkartläggning kan tekniska begränsningar upptäckas för sent. Om arbetet börjar i målbild utan konkretisering kan utvecklingsteamen få för lite vägledning.

Ett gemensamt börläge hjälper området att formulera riktningen. Arkitekturen hjälper området att förstå vilka strukturer som behöver förändras för att riktningen ska bli möjlig.

## Vanliga misstag

- **Misstag: Att börja med lösningar innan uppdraget är tydligt.**
  - Varför det händer: Många vill snabbt komma vidare till system, teknik eller leveransplanering.
  - Hur du undviker det: Formulera först vilket problem utvecklingsområdet ska lösa och vilket beslut arkitekturen ska stödja.

- **Misstag: Att beskriva verksamhet och IT i separata spår.**
  - Varför det händer: Roller, möten och dokumentmallar är ofta uppdelade.
  - Hur du undviker det: Skapa gemensamma arbetsytor där verksamhetsbehov, information, teknik och regelverk kopplas ihop.

- **Misstag: Att göra arkitekturen för generell.**
  - Varför det händer: Man vill skapa något som passar hela myndigheten.
  - Hur du undviker det: Utgå från utvecklingsområdets konkreta beslut, men visa tydligt vilka beroenden som finns till helheten.

- **Misstag: Att glömma andra utvecklingsområden.**
  - Varför det händer: Det egna området upplevs som mest akut.
  - Hur du undviker det: Identifiera tidigt beroenden till angränsande processer, informationsmängder, system och styrningsforum.

## Övningar

### Övning 1: Beskriv utvecklingsområdet

Välj ett utvecklingsområde du arbetar med eller känner till. Beskriv det med fem meningar:

1. Vilket verksamhetsbehov eller uppdrag står området för?
2. Vilka användare, medborgare, handläggare eller interna målgrupper påverkas?
3. Vilka större system eller verktyg är centrala?
4. Vilka informationsmängder verkar vara viktigast?
5. Vilka andra utvecklingsområden finns tydliga beroenden till?

### Övning 2: Identifiera arkitektens viktigaste bidrag

Skriv ner tre beslut som utvecklingsområdet behöver fatta det kommande året. För varje beslut, besvara:

- Vilken verksamhetskunskap behövs?
- Vilken IT- eller teknikkunskap behövs?
- Vilken arkitekturbeskrivning skulle göra beslutet bättre?

### Fördjupning

Jämför hur en verksamhetsarkitekt och en IT-arkitekt skulle beskriva samma utvecklingsområde. Markera vilka delar som överlappar. Det är ofta i överlappet som de viktigaste arkitekturfrågorna finns.

## Snabb sammanfattning

- Ett utvecklingsområde är en praktisk ram där verksamhet och IT behöver skapa riktning tillsammans.
- Arkitektens uppdrag är att stödja bättre beslut, inte att producera dokument för dokumentens skull.
- Börläge och arkitektur behöver tas fram tillsammans.
- De sex perspektiven arbetssätt, resurser, information, verktyg, teknik och regelverk beskriver olika delar av samma förändring.
- Ett användbart börläge visar både riktning, samband, beroenden och konsekvenser.

## Quiz/reflektionsfrågor

1. Varför räcker det inte att beskriva ett börläge enbart som en målbild?
2. Vad kan hända om IT-arkitekturen tas fram utan ett tydligt verksamhetsnära börläge?
3. Vilka av de sex arkitekturperspektiven är mest synliga i ditt utvecklingsområde i dag?
4. Vilka perspektiv riskerar att förbises?
5. Vilka intressenter behöver vara med tidigt för att börläget ska bli förankrat?

## Nästa steg

Nästa kapitel går djupare i vad som menas med börläge. Där skiljer vi mellan nuläge, målbild, börläge, roadmap och arkitektur så att begreppen kan användas konsekvent genom resten av boken.

<div class="pagebreak"></div>

# Kapitel 2: Vad menas med börläge?

## Varför detta kapitel finns

Ordet börläge används ofta som om alla redan vet vad det betyder. I praktiken kan olika personer mena olika saker. En beställare kan mena en övergripande framtidsbild. En verksamhetsarkitekt kan mena nya arbetssätt och ansvar. En IT-arkitekt kan mena systemstöd, integrationer och tekniska principer. En styrgrupp kan mena ett beslutsunderlag för prioritering.

Det här kapitlet skapar ett gemensamt språk. När utvecklingsområdet har en tydlig definition av börläge blir det lättare att avgränsa arbetet, välja rätt detaljeringsnivå och undvika att arkitekturen blir antingen för abstrakt eller för teknisk.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- skilja mellan nuläge, målbild, börläge, arkitektur, gap och färdplan
- förklara varför börläget behöver beskrivas ur flera perspektiv
- avgöra när ett börläge är tillräckligt konkret för att användas i styrning och genomförande
- identifiera vanliga missförstånd kring börläge
- använda en enkel struktur för att formulera ett börläge

## Innan vi börjar

I föregående kapitel placerades utvecklingsområdet i sin organisatoriska kontext. Vi beskrev också att arkitektur inte bara handlar om teknik, utan om hur verksamhet och IT tillsammans behöver förändras.

Nu går vi vidare till ett av de viktigaste begreppen i arbetet: börläge.

I den här boken betyder börläge inte en vision i största allmänhet. Det betyder ett beskrivet framtida läge som är tillräckligt konkret för att kunna vägleda prioriteringar, arkitekturbeslut, planering och genomförande.

## Nuläge, målbild och börläge

Ett vanligt problem är att nuläge, målbild och börläge blandas ihop. De hänger ihop, men de har olika funktion.

| Begrepp | Fråga det svarar på | Typiskt innehåll |
|---|---|---|
| Nuläge | Var är vi nu? | arbetssätt, system, informationsflöden, problem, begränsningar |
| Målbild | Vart vill vi på övergripande nivå? | önskade effekter, strategisk riktning, principer |
| Börläge | Hur ska det framtida läget vara utformat? | framtida arbetssätt, ansvar, information, verktyg, teknik och styrning |
| Gap | Vad skiljer nuläge från börläge? | skillnader, risker, beroenden, förmågor som saknas |
| Färdplan | Hur tar vi oss dit? | etapper, prioriteringar, beslutspunkter, genomförandesteg |

Målbilden ger riktning. Börläget gör riktningen användbar. Färdplanen beskriver vägen dit.

Ett börläge ska alltså inte bara säga att myndigheten ska bli mer sammanhållen, datadriven, effektiv eller rättssäker. Det ska visa vad detta innebär i utvecklingsområdet.

## En praktisk definition

I den här handboken använder vi följande definition:

> Ett börläge är en sammanhängande beskrivning av hur ett utvecklingsområde bör fungera i framtiden för att uppfylla verksamhetens mål, regelverkens krav och IT:s arkitekturprinciper.

Definitionen innehåller tre viktiga delar.

För det första är börläget sammanhängande. Det räcker inte att beskriva ett nytt system, ett nytt arbetssätt eller en ny process var för sig. Perspektiven måste kopplas ihop.

För det andra handlar börläget om hur området bör fungera, inte bara hur det bör se ut. Det behöver därför beskriva ansvar, flöden, beslut, information och tekniska förutsättningar.

För det tredje ska börläget vara förankrat i mål, regelverk och arkitekturprinciper. Annars riskerar det att bli en önskelista utan styrande kraft.

## Börläge och arkitektur

Börläge och arkitektur är nära kopplade, men de är inte samma sak.

Börläget beskriver det önskade framtida läget. Arkitekturen beskriver hur detta framtida läge är uppbyggt, vilka delar som ingår, hur de samverkar och vilka vägval som krävs.

Ett enkelt sätt att tänka är:

- Börläget svarar på vad som ska vara sant i framtiden.
- Arkitekturen svarar på hur detta framtida läge behöver hänga ihop.
- Färdplanen svarar på i vilken ordning förändringen bör ske.

Exempel:

- Börläge: Medborgarens ärende ska kunna följas genom hela processen.
- Arkitektur: Ärenden behöver ha gemensamma begrepp, gemensamma identifierare, tydliga informationsägare och integrationer mellan relevanta system.
- Färdplan: Först etableras begrepp och informationsansvar, därefter anpassas systemstöd och integrationer stegvis.

## De sex perspektiven

I den här boken beskriver vi börläge och arkitektur genom sex återkommande perspektiv:

- arbetssätt
- resurser
- information
- verktyg
- teknik
- regelverk

Perspektiven hjälper arkitekten att undvika blinda fläckar.

Ett börläge som bara beskriver arbetssätt kan bli svårt att genomföra om informationsflöden och systemstöd saknas. Ett börläge som bara beskriver teknik kan bli irrelevant om ansvar, roller och regelverk inte är tydliga. Ett börläge som bara beskriver regelverk kan bli korrekt på papperet men svårt att omsätta i praktiken.

Perspektiven ska inte ses som sex separata dokument. De är sex sätt att undersöka samma framtida läge.

## Hur konkret ska ett börläge vara?

Ett börläge behöver vara tillräckligt konkret för att kunna användas, men inte så detaljerat att det låser allt för tidigt.

För abstrakt:

- “Vi ska arbeta mer datadrivet.”
- “Vi ska ha en modern teknisk plattform.”
- “Vi ska säkerställa effektiv samverkan.”

Mer användbart:

- “Beslut i processen ska baseras på definierade informationsobjekt med utsedda informationsägare.”
- “Utvecklingsområdet ska använda gemensamma integrationsmönster för informationsutbyte mellan ärendehantering och analysstöd.”
- “Roller, ansvar och beslutspunkter ska vara dokumenterade för de steg där flera organisatoriska enheter samverkar.”

Det användbara börläget beskriver vad som ska förändras på ett sätt som kan diskuteras, granskas och omsättas i beslut.

## En enkel struktur för börlägesformulering

När du formulerar ett börläge kan du använda följande struktur:

1. Beskriv vilken förmåga eller funktion som ska förbättras.
2. Beskriv varför förändringen behövs.
3. Beskriv vad som ska vara sant i framtiden.
4. Beskriv vilka arkitekturperspektiv som påverkas.
5. Beskriv vilka beslut eller vägval som krävs.
6. Beskriv hur börläget kan följas upp.

Exempel:

| Del | Exempel |
|---|---|
| Förmåga | Hantera inkommande ärenden på ett enhetligt sätt |
| Varför | Nuläget skapar dubbelarbete och svår spårbarhet |
| Framtida läge | Ärenden klassificeras enligt gemensamma begrepp och följs genom hela processen |
| Perspektiv | arbetssätt, information, verktyg, teknik, regelverk |
| Vägval | gemensam ärendeidentitet, informationsägarskap, integrationsprincip |
| Uppföljning | minskad manuell komplettering och bättre spårbarhet i processen |

## Börläget som beslutsunderlag

Ett börläge är inte bara en beskrivning. Det är också ett beslutsunderlag.

När börläget är tydligt kan utvecklingsområdet fatta bättre beslut om:

- vilka initiativ som bör prioriteras
- vilka beroenden som måste hanteras
- vilka system eller komponenter som behöver förändras
- vilka arbetssätt som behöver införas eller avvecklas
- vilka regelverkskrav som måste styra lösningen
- vilka delar som kan genomföras tidigt och vilka som kräver mer analys

Ett bra börläge minskar risken för att varje initiativ optimerar sin egen del utan att bidra till helheten.

## Sambandet mellan nuläge, börläge och färdplan

Sambandet kan beskrivas så här: den grundläggande rörelsen från nuläge till genomförande.

beskrivningen är medvetet enkelt. I praktiken sker arbetet ofta iterativt. När gap analyseras kan börläget behöva justeras. När färdplanen tas fram kan vissa vägval visa sig vara för stora, för dyra eller beroende av beslut utanför utvecklingsområdet.

## Vanliga misstag

- **Misstag: Börläget blir en vision utan arkitektur.**
  - Varför det händer: Gruppen vill skapa energi och riktning, men undviker svåra detaljer.
  - Hur du undviker det: Koppla varje viktig formulering till minst ett arkitekturperspektiv och ett konkret vägval.

- **Misstag: Börläget blir en teknisk lösningsbeskrivning.**
  - Varför det händer: IT-arkitekturen är ofta mer etablerad än verksamhetsarkitekturen.
  - Hur du undviker det: Beskriv först arbetssätt, ansvar och information innan tekniska lösningar låses.

- **Misstag: Börläget beskriver allt på samma detaljnivå.**
  - Varför det händer: Man försöker skapa komplett dokumentation i stället för ett användbart styrunderlag.
  - Hur du undviker det: Lägg mest detaljer där beslut, beroenden och risker är störst.

- **Misstag: Börläget saknar koppling till genomförande.**
  - Varför det händer: Arkitekturarbetet avslutas när dokumentet är klart.
  - Hur du undviker det: Ta alltid fram gap, konsekvenser och färdplan som fortsättning på börläget.

## Praktisk checklista

Använd checklistan när du granskar om ett börläge är tillräckligt tydligt.

- Är det tydligt vilken del av utvecklingsområdet börläget gäller?
- Finns en tydlig koppling till verksamhetsmål eller strategisk riktning?
- Beskrivs både verksamhets- och IT-perspektiv?
- Är centrala informationsobjekt eller begrepp identifierade?
- Är ansvar och roller tillräckligt tydliga?
- Finns relevanta regelverk eller styrande principer med?
- Går det att se vilka beslut som behöver fattas?
- Går det att härleda gap mellan nuläge och börläge?
- Går börläget att omsätta i en färdplan?

## Övningar

### Övning 1: Sortera begreppen

Ta ett aktuellt initiativ i ditt utvecklingsområde och skriv tre korta formuleringar:

1. En nulägesbeskrivning.
2. En målbild.
3. Ett börläge.

Jämför formuleringarna. Är börläget mer konkret än målbilden? Är nuläget tydligt skilt från det framtida läget?

### Övning 2: Testa sex perspektiv

Välj en börlägesformulering och pröva den mot perspektiven:

| Perspektiv | Fråga |
|---|---|
| Arbetssätt | Vilka aktiviteter, flöden eller beslut förändras? |
| Resurser | Vilka roller, kompetenser eller ansvar påverkas? |
| Information | Vilka begrepp, objekt eller informationsflöden behövs? |
| Verktyg | Vilket verksamhetsnära stöd behövs? |
| Teknik | Vilka tekniska komponenter, integrationer eller plattformar påverkas? |
| Regelverk | Vilka lagar, riktlinjer eller interna styrprinciper måste följas? |

Markera de perspektiv där formuleringen är svag. Det är ofta där nästa analys behöver börja.

### Fördjupning

Granska ett befintligt arkitekturdokument i din organisation. Leta efter meningar som beskriver framtida läge. Är de målbild, börläge, lösningsförslag eller färdplan? Skriv om två av meningarna så att de blir tydligare börlägesformuleringar.

## Snabb sammanfattning

- Ett börläge är ett konkret beskrivet framtida läge, inte bara en vision.
- Målbilden ger riktning, börläget gör riktningen användbar och färdplanen beskriver vägen dit.
- Börläge och arkitektur hänger ihop, men är inte samma sak.
- Ett användbart börläge behöver täcka både verksamhet och IT.
- De sex perspektiven hjälper arkitekten att se helheten.
- Börläget ska kunna användas som underlag för beslut, prioritering och genomförande.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan målbild och börläge?
2. Varför räcker det inte att beskriva börläget ur ett tekniskt perspektiv?
3. Vilka risker uppstår om börläget saknar koppling till färdplan?
4. När är ett börläge för abstrakt?
5. Vilket av de sex perspektiven brukar vara svagast i din organisation, och varför?

## Nästa steg

Nästa kapitel handlar om hur arbetet med börläget förbereds. Där går vi från begrepp till planering: avgränsning, intressenter, styrande dokument, arbetssätt och första struktur för arkitekturarbetet.

<div class="pagebreak"></div>

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

<div class="pagebreak"></div>

# Kapitel 4: Skapa en gemensam problembild

## Varför detta kapitel finns

Ett börläge blir sällan bättre än den problembild det bygger på. Om olika aktörer har olika uppfattningar om vad problemet är, varför det finns och vilka konsekvenser det får, kommer arkitekturen lätt att bli en samling lösningsförslag utan gemensam riktning.

Det här kapitlet visar hur verksamhetsarkitekter och IT-arkitekter kan skapa en gemensam problembild för ett utvecklingsområde. Målet är inte att dokumentera allt som är fel. Målet är att förstå vilka problem som är viktiga nog att påverka börläget och den tillhörande arkitekturen.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- skilja mellan symptom, bakomliggande orsaker och konsekvenser
- planera en enkel insamling av problembild från olika intressenter
- strukturera problem så att de kan användas i fortsatt arkitekturarbete
- formulera problem utan att låsa fast lösningar för tidigt
- identifiera när problembilden behöver förankras innan arbetet går vidare

## Innan vi börjar

I föregående kapitel förbereddes arbetet genom avgränsning, intressentbild och insamling av styrande underlag. Nu används den förberedelsen för att skapa en gemensam förståelse av varför ett börläge behövs.

En problembild är inte samma sak som en kravlista. En kravlista beskriver ofta vad någon vill ha. En problembild beskriver varför något behöver förändras.

## Vad är en gemensam problembild?

En gemensam problembild är en sammanhållen beskrivning av de viktigaste problem, behov och spänningar som utvecklingsområdet behöver hantera.

Den bör svara på fyra frågor:

1. Vad fungerar inte tillräckligt bra i dag?
2. Vem påverkas av det?
3. Vilka konsekvenser får det för verksamhet, IT, styrning eller användare?
4. Varför är problemet viktigt att hantera nu?

En bra problembild är begriplig för både verksamhet och IT. Den är tillräckligt konkret för att vägleda arkitekturarbetet, men inte så detaljerad att den blir ett register över enskilda irritationsmoment.

## Från symptom till orsak

Många samtal börjar med symptom. Ett symptom är något som märks i vardagen, till exempel att handläggning tar lång tid, att information måste dubbelregistreras eller att ett system upplevs som svårt att använda.

Symptom är viktiga, men de räcker inte. Arkitekturarbetet behöver förstå vad som ligger bakom symptomen.

| Nivå | Fråga | Exempel |
|---|---|---|
| Symptom | Vad märks i vardagen? | Samma uppgift registreras i flera system. |
| Orsak | Varför händer det? | Informationsägarskap och integrationer är otydliga. |
| Konsekvens | Vad leder det till? | Felaktig information, längre ledtider och svagare uppföljning. |
| Arkitekturrelevans | Varför påverkar det börläget? | Börläget behöver beskriva informationsansvar och informationsflöden. |

När problembilden formuleras på detta sätt blir det lättare att se vilka arkitekturperspektiv som påverkas.

## Planera insamlingen

Insamlingen bör vara enkel, men genomtänkt. Börja med de intressenter som identifierades i förberedelsekapitlet och välj en kombination av intervjuer, dokumentstudier och workshoppar.

En praktisk startpunkt är:

- **Intervjuer** med nyckelpersoner för att förstå perspektiv och exempel.
- **Dokumentstudier** för att hitta mål, beslut, risker, tidigare analyser och styrande krav.
- **Workshop** för att jämföra bilder, hitta mönster och prioritera.
- **Arkitekturanalys** för att koppla problemen till arbetssätt, resurser, information, verktyg, teknik och regelverk.

För relativt nya verksamhetsarkitekter är det ofta klokt att börja med intervjuer och en mindre workshop. För mer erfarna IT-arkitekter kan arkitekturanalysen parallellt kopplas till system, integrationer, teknisk skuld och informationsflöden.

## Intervjufrågor som öppnar upp

Intervjuer bör inte börja med frågan “vilken lösning vill du ha?”. Då riskerar samtalet att bli en lista över önskade systemfunktioner.

Bättre frågor är:

- Vad är svårt att få att fungera i dag?
- När märks problemet som tydligast?
- Vilka roller eller grupper påverkas?
- Vilken information saknas, är osäker eller kommer för sent?
- Vilka beslut blir svåra att fatta?
- Vilka regler, rutiner eller tekniska begränsningar påverkar situationen?
- Vad händer om inget förändras?
- Vad skulle vara annorlunda om problemet var löst?

Svaren bör dokumenteras kortfattat. Försök fånga konkreta exempel, men undvik att skriva långa referat.

## Workshop för gemensam förståelse

En workshop kan användas för att skapa en gemensam bild mellan verksamhet, IT och styrning. Den behöver inte vara omfattande. Det viktiga är att deltagarna ser varandras perspektiv.

Ett enkelt upplägg är:

1. Presentera syfte och avgränsning.
2. Låt deltagarna beskriva viktiga problem ur sitt perspektiv.
3. Gruppera problemen i teman.
4. Skilj symptom från orsaker och konsekvenser.
5. Koppla varje tema till berörda arkitekturperspektiv.
6. Prioritera vilka problem som bör styra börläget.
7. Dokumentera öppna frågor och oenigheter.

Det är viktigt att oenighet inte döljas. Om verksamhet och IT beskriver problemet olika kan just den skillnaden vara arkitekturrelevant.

## Strukturera problembilden

Efter insamlingen behöver materialet struktureras. En användbar struktur är att beskriva varje problemtema på samma sätt.

| Fält | Beskrivning |
|---|---|
| Problemtema | Kort namn på problemet. |
| Beskrivning | Vad problemet består av. |
| Berörda aktörer | Vilka roller, enheter eller användare som påverkas. |
| Konsekvenser | Effekter för verksamhet, IT, kostnad, kvalitet, risk eller regelefterlevnad. |
| Berörda perspektiv | Arbetssätt, resurser, information, verktyg, teknik och regelverk. |
| Indikationer | Exempel, data, observationer eller beslut som stöder problembilden. |
| Öppna frågor | Det som behöver utredas vidare. |

Den här strukturen gör problembilden användbar i senare kapitel. Den hjälper också till att undvika att varje problem genast blir ett lösningsförslag.

## Koppla problem till arkitekturperspektiv

Ett problem i ett utvecklingsområde påverkar ofta flera perspektiv samtidigt. Dubbelregistrering kan till exempel verka som ett verktygsproblem, men kan samtidigt handla om arbetssätt, informationsägarskap, integrationer och regelverk.

Ett enkelt sätt att synliggöra detta är att göra en perspektivkarta.

| Problemtema | Arbetssätt | Resurser | Information | Verktyg | Teknik | Regelverk |
|---|---|---|---|---|---|---|
| Dubbelregistrering | Ja | Delvis | Ja | Ja | Ja | Delvis |
| Otydligt ansvar | Ja | Ja | Ja | Nej | Nej | Delvis |
| Svår uppföljning | Ja | Nej | Ja | Ja | Delvis | Ja |

Tabellen behöver inte vara perfekt. Den ska hjälpa gruppen att se att börläget måste bli sammanhängande.

## Undvik att låsa lösningar för tidigt

När problembilden tas fram kommer många lösningsidéer att dyka upp. Det är bra, men de bör hållas isär från problembilden.

Skriv gärna ned lösningsidéer i en separat lista, till exempel:

- möjliga lösningsspår
- hypoteser att pröva
- frågor till kommande arkitekturarbete
- beroenden till andra utvecklingsområden

Det gör att idéerna inte försvinner, samtidigt som problembilden fortsätter vara tydlig.

## Exempel: otydligt informationsansvar

Ett utvecklingsområde upptäcker att flera team använder samma grundinformation, men tolkar den olika. Verksamheten beskriver problemet som att uppföljningen är osäker. IT beskriver problemet som att integrationerna är svåra att förvalta. Juridik beskriver problemet som att ansvar för vissa uppgifter är otydligt.

En gemensam problembild kan då formuleras så här:

| Fält | Exempel |
|---|---|
| Problemtema | Otydligt informationsansvar |
| Beskrivning | Samma information används i flera processer och system, men ansvar, definitioner och uppdateringsflöden är inte tydliga. |
| Berörda aktörer | Handläggare, produktteam, informationsägare, uppföljningsansvariga och jurister. |
| Konsekvenser | Risk för felaktiga beslut, dubbelarbete, svag spårbarhet och svårare regelefterlevnad. |
| Berörda perspektiv | Arbetssätt, information, verktyg, teknik och regelverk. |
| Indikationer | Intervjuer, tidigare incidenter och olika definitioner i befintliga dokument. |
| Öppna frågor | Vem ska äga informationen och vilka system ska vara källa? |

Denna formulering pekar inte ut en färdig lösning. Den visar däremot vad börläget måste hantera.

## Vanliga misstag

- **Misstag: Att samla in för mycket utan att strukturera.**
  - Varför det händer: Det känns tryggt att dokumentera allt.
  - Hur du undviker det: Gruppera tidigt materialet i problemteman och arkitekturperspektiv.

- **Misstag: Att skriva lösningar som problem.**
  - Varför det händer: Många intressenter uttrycker behov som önskade systemfunktioner.
  - Hur du undviker det: Fråga vilket problem lösningen ska hantera och dokumentera lösningsidén separat.

- **Misstag: Att låta en stark röst definiera hela problembilden.**
  - Varför det händer: Vissa roller har större mandat eller mer erfarenhet.
  - Hur du undviker det: Jämför flera perspektiv och markera oenighet öppet.

- **Misstag: Att glömma regelverksperspektivet.**
  - Varför det händer: Regelverk kommer ofta in sent i lösningsarbete.
  - Hur du undviker det: Ta med styrande krav och regelefterlevnad redan i problembilden.

## Övningar

### Övning 1: Sortera symptom, orsaker och konsekvenser

Välj ett känt problem i ditt utvecklingsområde. Skriv tre listor:

1. Vad märks i vardagen?
2. Vad kan ligga bakom?
3. Vilka konsekvenser får det?

Avsluta med att formulera problemet i två meningar utan att föreslå en lösning.

### Övning 2: Gör en perspektivkarta

Välj tre problemteman och markera vilka arkitekturperspektiv de påverkar:

- arbetssätt
- resurser
- information
- verktyg
- teknik
- regelverk

Fundera sedan på om något problem behandlas för smalt.

### Fördjupning

Genomför en kort workshop med två verksamhetsrepresentanter och två IT-representanter. Be dem beskriva samma problem var för sig. Jämför sedan likheter och skillnader.

## Snabb sammanfattning

- En gemensam problembild skapar riktning för börläge och arkitektur.
- Skilj på symptom, orsaker, konsekvenser och lösningsidéer.
- Använd intervjuer, dokumentstudier och workshoppar för att få flera perspektiv.
- Strukturera problemteman på ett konsekvent sätt.
- Koppla varje problem till berörda arkitekturperspektiv.
- Förankra oenighet i stället för att dölja den.

## Quiz/reflektionsfrågor

1. Varför är det riskabelt att gå direkt från problem till lösning?
2. Vad är skillnaden mellan ett symptom och en bakomliggande orsak?
3. Hur kan samma problem påverka både verksamhetsarkitektur och IT-arkitektur?
4. Vilka intressenter bör vara med när problembilden förankras?
5. Vilka problem i ditt utvecklingsområde är viktigast att förstå innan börläget formuleras?

## Nästa steg

När problembilden är tillräckligt tydlig kan arbetet gå vidare till principer och målbild. Nästa kapitel visar hur strategier, mål, regelverk och arkitekturprinciper kan omsättas till en riktning som styr börläget.

<div class="pagebreak"></div>

# Kapitel 5: Formulera principer och målbild

## Varför detta kapitel finns

När problembilden är tydlig behöver arkitekturarbetet få riktning. Det räcker inte att veta vad som skaver i nuläget. Utvecklingsområdet behöver också kunna beskriva vilka vägval som ska styra framtida lösningar och vilken målbild som börläget ska bidra till.

Det här kapitlet visar hur verksamhetsarkitekter och IT-arkitekter kan formulera principer och målbild på ett sätt som är praktiskt användbart. Principer och målbild ska inte vara slogans. De ska hjälpa utvecklingsområdet att fatta bättre beslut när kraven är många, perspektiven krockar och detaljerna ännu inte är färdiga.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- skilja mellan mål, målbild, arkitekturprincip och lösningsbeslut
- formulera principer som ger vägledning utan att bli för detaljerade
- koppla målbilden till problembild, styrande dokument och verksamhetsnytta
- pröva om en princip är användbar i praktiska beslut
- identifiera när målbilden behöver förankras innan börläget detaljeras

## Innan vi börjar

I föregående kapitel skapades en gemensam problembild. Den beskrev vad som inte fungerar tillräckligt bra, vilka konsekvenser det får och varför problemen är viktiga för utvecklingsområdet.

Nu används problembilden som underlag för riktning. Frågan är inte längre bara: vad behöver förändras? Frågan blir också: vilka vägval ska prägla förändringen?

## Vad är en målbild?

En målbild beskriver ett önskat framtida läge på en nivå som är mer konkret än en vision, men mindre detaljerad än ett färdigt börläge. Den ska hjälpa människor att förstå vad utvecklingsområdet strävar mot.

En bra målbild svarar på frågor som:

- Vilken förmåga ska utvecklingsområdet ha i framtiden?
- Vad ska fungera bättre för användare, verksamhet, IT och styrning?
- Vilka problem från problembilden ska vara lösta eller tydligt minskade?
- Vilka kvaliteter ska prägla framtida arbetssätt, information, systemstöd och teknik?
- Vilka begränsningar eller styrande krav måste respekteras?

Målbilden ska vara tillräckligt tydlig för att skapa riktning, men inte så detaljerad att den låser lösningen för tidigt.

## Vad är en arkitekturprincip?

En arkitekturprincip är en styrande regel eller riktlinje som hjälper utvecklingsområdet att fatta konsekventa beslut. Den beskriver inte exakt vilken lösning som ska byggas. Den beskriver hur man ska välja mellan möjliga lösningar.

En princip bör vara:

- tydlig
- beslutsstödjande
- möjlig att pröva
- relevant för flera situationer
- kopplad till målbild och problembild
- accepterad av de aktörer som behöver följa den

En princip som inte påverkar beslut är ofta bara en formulering. En princip som påverkar beslut men inte är förankrad kan skapa konflikt. Därför behöver principer både vara praktiska och legitima.

## Skillnaden mellan mål, målbild, princip och beslut

Det är vanligt att dessa begrepp blandas ihop. I tidiga diskussioner gör det sällan något, men när börläge och arkitektur ska dokumenteras behöver skillnaden bli tydlig.

| Begrepp | Beskriver | Exempel |
|---|---|---|
| Mål | Vad som ska uppnås | Minska ledtiden för ärendehandläggning. |
| Målbild | Hur framtida läge ska upplevas och fungera | Handläggare arbetar i ett sammanhållet flöde med korrekt och återanvändbar information. |
| Princip | Hur vägval ska göras | Information ska registreras en gång och återanvändas där det är möjligt och tillåtet. |
| Beslut | Vad som faktiskt väljs | Ärendedata ska hämtas från gemensam informationskälla via standardiserat gränssnitt. |

Målet beskriver riktningen. Målbilden gör riktningen begriplig. Principerna vägleder vägval. Besluten konkretiserar valen i arkitekturen.

## Utgå från problembilden

Målbild och principer ska inte skapas fristående. De ska svara mot verkliga problem, behov och styrande krav.

Ett enkelt arbetssätt är att gå igenom problembilden och ställa tre frågor för varje viktigt problemtema:

1. Vilken framtida förmåga behöver finnas för att problemet ska minska?
2. Vilket vägval behöver vara konsekvent över tid?
3. Vilka arkitekturperspektiv påverkas?

Exempel:

| Problemtema | Möjlig målbild | Möjlig princip |
|---|---|---|
| Dubbelregistrering | Information registreras nära källan och återanvänds i andra processer. | Information ska ha tydligt ägarskap och bara registreras flera gånger när det finns ett dokumenterat skäl. |
| Otydliga ansvar | Roller och ansvar är begripliga mellan utvecklingsområde, linjeorganisation och förvaltning. | Varje central förmåga ska ha utsedd ansvarig part för beslut, utveckling och uppföljning. |
| Svårt att följa regelverk | Regelkrav är synliga i arbetssätt, informationshantering och systemstöd. | Regelkrav ska spåras till berörda processer, informationsobjekt och tekniska kontroller. |

På det sättet blir målbilden en fortsättning på problembilden, inte ett separat visionsdokument.

## Hämta riktning från styrande underlag

I en större statlig myndighet finns ofta flera styrande underlag. Det kan handla om strategi, verksamhetsplan, rättsliga krav, säkerhetskrav, informationshanteringsprinciper, tekniska riktlinjer, digitaliseringsmål och arkitekturprinciper på myndighetsnivå.

Utvecklingsområdets målbild bör inte uppfinna en egen riktning om myndigheten redan har beslutad riktning. Samtidigt behöver den översätta övergripande styrning till det aktuella utvecklingsområdet.

Använd därför styrande underlag på tre nivåer:

- **Myndighetsnivå:** Vad måste alla utvecklingsområden följa?
- **Utvecklingsområdesnivå:** Vad betyder styrningen här?
- **Genomförandenivå:** Vad behöver projekt, produktteam och förvaltning göra annorlunda?

Det viktiga är inte att kopiera formuleringar. Det viktiga är att visa hur styrningen påverkar börläget.

## Formulera en användbar målbild

En målbild blir ofta bäst när den består av flera korta delar i stället för en lång text. Det gör den lättare att använda i workshops, beslutsunderlag och förankring.

En praktisk struktur är:

- **Sammanfattande målbild:** en kort beskrivning av önskat läge.
- **Effekter för verksamheten:** vad blir bättre i arbetssätt, ansvar och resultat?
- **Effekter för användare eller mottagare:** vad blir enklare, säkrare eller mer begripligt?
- **Effekter för IT och förvaltning:** vad blir mer hållbart, återanvändbart eller styrbart?
- **Viktiga kvaliteter:** till exempel spårbarhet, säkerhet, enkelhet, datakvalitet eller flexibilitet.
- **Avgränsningar:** vad målbilden inte försöker lösa.

Exempel på kort målbild:

> Utvecklingsområdet ska möjliggöra ett sammanhållet, regelstyrt och informationsdrivet arbetssätt där centrala uppgifter registreras nära källan, återanvänds kontrollerat och stödjer både operativ handläggning och uppföljning.

Den formuleringen är fortfarande övergripande. Den behöver kompletteras med principer, perspektivbeskrivningar och senare ett konkret börläge.

## Formulera principer med konsekvens

En användbar princip bör innehålla mer än en rubrik. Den bör också förklara varför principen finns och vad den innebär i praktiken.

Använd gärna följande mall:

| Del | Fråga |
|---|---|
| Namn | Vad kallas principen? |
| Formulering | Vilken regel eller riktlinje ska följas? |
| Motiv | Varför behövs principen? |
| Konsekvens | Vad innebär den för arbetssätt, information, verktyg, teknik eller regelverk? |
| Undantag | När kan principen frångås, och vem beslutar det? |

Exempel:

| Del | Exempel |
|---|---|
| Namn | Registrera information nära källan |
| Formulering | Information ska i första hand registreras där den uppstår och återanvändas av andra delar av verksamheten. |
| Motiv | Minskar dubbelregistrering, förbättrar datakvalitet och gör ansvar tydligare. |
| Konsekvens | Processer, informationsmodeller och integrationer behöver utformas så att återanvändning blir möjlig. |
| Undantag | Undantag kan göras vid rättsliga hinder, säkerhetsskäl eller orimlig kostnad, men ska dokumenteras. |

Den här typen av princip är möjlig att diskutera, pröva och använda i arkitekturbeslut.

## Håll principerna få och starka

Ett vanligt misstag är att skapa för många principer. Om det finns tjugo principer blir de svåra att komma ihåg och ännu svårare att använda i vardagen.

För ett utvecklingsområde är det ofta bättre att börja med fem till åtta principer som verkligen påverkar beslut.

Exempel på principområden:

- information och datakvalitet
- ansvar och ägarskap
- återanvändning
- säkerhet och integritet
- regelefterlevnad
- användbarhet
- teknisk hållbarhet
- förändringsbarhet

Principerna ska inte täcka allt. De ska täcka det som är viktigt nog att styra arkitekturen.

## Testa principerna mot verkliga val

En princip är inte färdig förrän den har testats mot konkreta vägval. Testet kan göras enkelt i en workshop.

Välj två eller tre typiska beslut som utvecklingsområdet snart behöver fatta, till exempel:

- Ska information hämtas från befintligt system eller dupliceras i ett nytt stöd?
- Ska ett arbetssätt standardiseras över hela myndigheten eller variera per verksamhetsdel?
- Ska en teknisk lösning återanvända gemensam plattform eller bygga separat funktionalitet?
- Ska ett regelkrav hanteras manuellt i processen eller byggas in i systemstödet?

Ställ sedan frågan: hjälper principen oss att välja?

Om svaret är nej behöver principen förtydligas, tas bort eller ersättas.

## Förankra målbild och principer

Målbild och principer behöver förankras innan börläget detaljeras. Annars riskerar senare arkitekturbeskrivningar att ifrågasättas på grund av oenighet om riktningen.

Förankring behöver inte alltid vara ett stort beslutsmöte. Det kan vara en serie korta avstämningar med rätt aktörer.

Särskilt viktiga aktörer är:

- ansvariga för utvecklingsområdet
- verksamhetsföreträdare
- IT-arkitekter
- verksamhetsarkitekter
- informationssäkerhet och dataskydd
- juridik eller regelverkskompetens
- produkt- eller portföljledning
- förvaltning och drift
- berörda arkitekturforum

Syftet är inte att alla ska formulera varje mening. Syftet är att de viktigaste intressenterna ska förstå, kunna invända och kunna stå bakom riktningen.

## Vanliga misstag

- **Misstag: Att formulera principer som självklara värdeord.**
  - Varför det händer: Det känns tryggt att skriva principer som alla håller med om.
  - Hur du undviker det: Fråga vilket konkret beslut principen hjälper till med.

- **Misstag: Att göra målbilden för lösningsnära.**
  - Varför det händer: Diskussionen går snabbt mot system, funktioner och projekt.
  - Hur du undviker det: Beskriv först önskat framtida arbetssätt och informationsflöde innan teknisk lösning väljs.

- **Misstag: Att skapa för många principer.**
  - Varför det händer: Alla perspektiv vill få med sina viktiga frågor.
  - Hur du undviker det: Behåll bara principer som påverkar flera beslut eller hanterar ett centralt problemtema.

- **Misstag: Att inte hantera konflikter mellan principer.**
  - Varför det händer: Varje princip ser rimlig ut var för sig.
  - Hur du undviker det: Testa principerna mot realistiska scenarier där exempelvis återanvändning, säkerhet, kostnad och snabbhet drar åt olika håll.

## Övningar

### Övning 1: Från problemtema till princip

Välj tre problemteman från problembilden. För varje tema, skriv:

1. vilket framtida läge som vore bättre
2. vilken princip som skulle styra vägval
3. vilka arkitekturperspektiv som påverkas
4. vilket första beslut principen kan testas mot

### Övning 2: Pröva en princip

Välj en föreslagen princip och testa den mot ett konkret beslut i utvecklingsområdet.

Svara på följande frågor:

1. Hjälper principen oss att välja mellan två alternativ?
2. Är principen begriplig för både verksamhet och IT?
3. Är det tydligt när principen får frångås?
4. Behöver principen förtydligas?

### Fördjupning

Skapa ett principkort för en av utvecklingsområdets viktigaste principer. Använd mallen med namn, formulering, motiv, konsekvens och undantag. Förankra principkortet med minst en verksamhetsföreträdare och en IT-arkitekt.

## Snabb sammanfattning

- Målbilden beskriver önskat framtida läge på en nivå mellan vision och detaljerat börläge.
- Arkitekturprinciper vägleder återkommande vägval.
- Målbild och principer ska kopplas till problembild, styrande underlag och verksamhetsnytta.
- Principer behöver vara få, tydliga och möjliga att testa.
- Förankring av riktningen minskar risken för konflikter när börläget detaljeras.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan målbild och börläge?
2. Varför bör en princip testas mot konkreta beslut?
3. Vad händer om målbilden blir för lösningsnära?
4. Vilka aktörer behöver förankra principerna i ditt utvecklingsområde?
5. Vilken princip skulle sannolikt få störst effekt i ditt nuvarande arbete?

## Nästa steg

Nästa kapitel går in i det första arkitekturperspektivet: arbetssätt. Där används målbilden och principerna för att beskriva hur processer, roller, ansvar och samverkan bör fungera i utvecklingsområdets framtida läge.

<div class="pagebreak"></div>

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

<div class="pagebreak"></div>

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

<div class="pagebreak"></div>

# Kapitel 8: Beskriv börläge för information

## Varför detta kapitel finns

Information är ofta den del av ett börläge som binder ihop verksamhet och IT tydligast. Arbetssätt kräver information för att kunna utföras. Roller behöver veta vem som äger, skapar, ändrar och använder information. Verktyg och teknik behöver hantera information på ett säkert, spårbart och ändamålsenligt sätt. Regelverk ställer krav på hur information får samlas in, lagras, delas och gallras.

I ett utvecklingsområde i en större statlig myndighet kan informationsfrågorna snabbt bli komplexa. Samma begrepp kan användas på olika sätt i olika delar av organisationen. Information kan finnas i flera system. Ansvar för informationskvalitet kan vara otydligt. Juridiska krav kan påverka både processer, systemstöd och tekniska lösningar.

Det här kapitlet hjälper dig att beskriva börläget för information på en nivå som är tillräckligt konkret för beslut, men inte så detaljerad att arbetet fastnar i fullständig datamodellering.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- identifiera vilken information som är central för ett utvecklingsområdes börläge
- skilja mellan begrepp, informationsobjekt, data och dokument
- beskriva informationsflöden mellan arbetssätt, roller, system och andra utvecklingsområden
- formulera krav på informationsägarskap, kvalitet, spårbarhet och livscykel
- koppla informationsarkitektur till verksamhetsmål, teknikval och regelverk
- avgöra när en enkel informationsmodell räcker och när djupare analys behövs

## Innan vi börjar

I kapitel 6 beskrev vi börläget för arbetssätt. I kapitel 7 beskrev vi resurser och organisation. Nu fokuserar vi på den information som arbetssätten och organisationen behöver för att fungera.

Utgångspunkten är inte att skapa en komplett datamodell. Utgångspunkten är att förstå vilken information som är verksamhetskritisk, hur den rör sig, vem som ansvarar för den och vilka krav den ställer på framtida lösningar.

## Vad menas med information i börläget?

I den här boken använder vi ordet information för det innehåll som verksamheten behöver förstå, skapa, behandla, lagra, använda och dela. Information kan finnas i dokument, ärenden, register, system, meddelanden, beslutsunderlag, rapporter eller integrationer.

Det är hjälpsamt att skilja mellan fyra nivåer:

| Nivå | Fråga | Exempel |
|---|---|---|
| Begrepp | Vad menar vi? | Kund, ärende, beslut, insats |
| Informationsobjekt | Vilken informationsmängd hanteras? | Ärende, ansökan, beslut, handläggningsunderlag |
| Data | Hur representeras informationen digitalt? | Fält, kodvärden, statusar, metadata |
| Dokument eller vy | Hur presenteras informationen för människor? | Beslutsunderlag, rapport, skärmbild, utskick |

Ett vanligt misstag är att börja direkt med datafält. För börlägesarbete är det ofta bättre att börja med begrepp och informationsobjekt. Då blir det möjligt för verksamhetsarkitekter, IT-arkitekter, jurister, informationssäkerhetsspecialister och utvecklingsteam att prata om samma sak.

## Börja med verksamhetens informationsbehov

Ett informationsperspektiv ska inte vara frikopplat från verksamheten. Börja därför med att koppla informationen till de arbetssätt och förmågor som beskrivits tidigare.

Ställ frågor som:

- Vilken information behöver verksamheten för att fatta beslut?
- Vilken information skapas i arbetssättet?
- Vilken information ändras, kompletteras eller avslutas?
- Vilken information behöver delas med andra utvecklingsområden?
- Vilken information är särskilt känslig, styrande eller kvalitetskritisk?
- Vilken information saknas i dag eller är svår att lita på?

Ett bra börläge visar inte bara att information finns. Det visar varför informationen behövs och vilka konsekvenser det får om den är felaktig, otillgänglig eller otydligt definierad.

## Identifiera centrala informationsobjekt

Nästa steg är att identifiera de informationsobjekt som är viktigast för utvecklingsområdet. Ett informationsobjekt är en informationsmängd som verksamheten behöver kunna prata om som en helhet.

Exempel på informationsobjekt i en myndighetskontext kan vara:

- ärende
- ansökan
- beslut
- aktör
- organisation
- insats
- regel
- avvikelse
- uppföljningsresultat
- behörighet
- styrande dokument

För varje centralt informationsobjekt bör börläget svara på några enkla frågor:

| Fråga | Syfte |
|---|---|
| Vad betyder objektet? | Skapa gemensam förståelse |
| Var används det? | Koppla information till arbetssätt och system |
| Vem ansvarar för kvaliteten? | Synliggöra informationsägarskap |
| Var skapas eller uppdateras det? | Hitta källor och beroenden |
| Vilka regler gäller? | Koppla till juridik, säkerhet och styrning |
| Vilka problem finns i nuläget? | Motivera förändring |

Det räcker ofta med en kort text och en enkel tabell. Målet är inte att dokumentera allt. Målet är att identifiera det som påverkar börläget.

## Beskriv informationsflöden

Ett informationsflöde visar hur information rör sig mellan aktörer, arbetssätt, system och utvecklingsområden. Det är särskilt viktigt när börläget kräver samverkan över organisatoriska gränser.

Ett informationsflöde bör visa:

- vilken information som överförs
- från vem eller vad informationen kommer
- vem eller vad som tar emot informationen
- varför informationen behövs
- om informationen är manuell, halvautomatisk eller automatiserad
- vilka krav som finns på kvalitet, aktualitet, sekretess och spårbarhet

Ett enkelt flöde kan räcka långt:

```diagram
flödesbeskrivning LR
    A[Verksamhetsprocess] --> B[Informationsobjekt]
    B --> C[Systemstöd]
    C --> D[Annat utvecklingsområde]
    D --> E[Uppföljning och styrning]
```

När flödena diskuteras bör du särskilt leta efter överlämningar. Det är ofta där otydlighet, dubbelarbete, informationsförlust och ansvarsglapp uppstår.

## Beskriv informationsägarskap

Informationsägarskap handlar om vem som ansvarar för att informationen är definierad, korrekt, användbar, skyddad och hanterad enligt gällande krav. I större myndigheter kan ansvaret vara utspritt mellan verksamhet, systemförvaltning, informationssäkerhet, juridik, arkitektur och linjeorganisation.

Ett börläge bör tydliggöra minst tre ansvarsnivåer:

| Ansvar | Innebörd |
|---|---|
| Verksamhetsansvar | Vem behöver och använder informationen för att lösa uppdraget? |
| Kvalitetsansvar | Vem ansvarar för definition, korrekthet och förbättring? |
| Förvaltningsansvar | Vem ansvarar för system, lagring, ändring och teknisk hantering? |

Det betyder inte att en person måste äga allt. Det betyder att ansvarsbilden behöver vara tillräckligt tydlig för att börläget ska kunna styras och realiseras.

## Formulera informationskrav

När informationsobjekt, begrepp och flöden är identifierade behöver börläget formulera krav. Informationskrav beskriver vad informationen måste uppfylla för att vara användbar och tillåten att hantera.

Vanliga kravområden är:

- aktualitet
- korrekthet
- fullständighet
- spårbarhet
- åtkomst
- sekretess
- arkivering
- gallring
- interoperabilitet
- återanvändbarhet
- rapporterbarhet
- tillgänglighet

Skriv informationskrav som konkreta konsekvenser för arkitekturen.

Exempel:

- Beslutsunderlag ska kunna spåras till de uppgifter och regler som låg till grund för beslutet.
- Centrala begrepp ska ha beslutade definitioner innan informationsutbyte mellan utvecklingsområden automatiseras.
- Information som används för uppföljning ska ha definierad källa, uppdateringsfrekvens och kvalitetsansvar.
- Personuppgifter ska klassas innan de används i nya informationsflöden.

## Koppla information till regelverk och säkerhet

I en statlig myndighet är information nästan alltid påverkad av regelverk. Det kan handla om offentlighet och sekretess, dataskydd, arkiv, informationssäkerhet, tillgänglighet, förvaltningsrätt eller interna styrdokument.

Börläget behöver därför visa vilka informationsfrågor som kräver särskild granskning. Det är sällan arkitektens uppgift att ensam tolka alla juridiska krav, men arkitekten behöver synliggöra var kraven påverkar lösningen.

Använd gärna en enkel klassning:

| Informationsområde | Exempel på fråga | Behöver involveras |
|---|---|---|
| Personuppgifter | Behandlas personuppgifter? | Dataskydd, juridik |
| Sekretess | Finns skyddsvärda uppgifter? | Juridik, informationssäkerhet |
| Arkiv | Ska information bevaras eller gallras? | Arkivfunktion |
| Åtkomst | Vem får se eller ändra uppgifterna? | Verksamhet, säkerhet, systemägare |
| Spårbarhet | Behöver åtgärder loggas? | IT, säkerhet, revision |

Det viktiga är att börläget inte behandlar regelverk som ett sidospår. Regelverk påverkar ofta både arbetssätt, informationsmodell, systemstöd och teknik.

## Hitta informationsberoenden mellan utvecklingsområden

När myndigheten är indelad i flera utvecklingsområden uppstår informationsberoenden. Ett utvecklingsområde kan vara beroende av information som ägs, skapas eller förändras i ett annat område. Det kan också själv vara källa till information som andra områden använder.

Dokumentera beroenden tidigt. Annars riskerar börläget att bli korrekt inom den egna gränsen men fel i helheten.

En enkel beroendetabell kan se ut så här:

| Informationsobjekt | Kommer från | Används av | Kritisk fråga |
|---|---|---|---|
| Ärendestatus | Utvecklingsområde A | Utvecklingsområde B, uppföljning | Är statusdefinitionerna gemensamma? |
| Beslut | Utvecklingsområde B | Kundmöte, rapportering | Vilken version är styrande? |
| Regelreferens | Rättsligt stöd | Flera utvecklingsområden | Hur hanteras ändringar i regelverk? |

Sådana beroenden bör senare kopplas till färdplan, risker och arkitekturbeslut.

## Vanliga misstag

- **Misstag: Att hoppa direkt till databasfält.**
  - Varför det händer: IT-arkitekter och utvecklingsteam vill snabbt konkretisera lösningen.
  - Hur du undviker det: Börja med begrepp, informationsobjekt och verksamhetsbehov innan detaljerad datamodellering.

- **Misstag: Att skapa en informationsmodell utan ägare.**
  - Varför det händer: Modellen ses som dokumentation snarare än styrande arkitektur.
  - Hur du undviker det: Koppla varje centralt informationsobjekt till ansvar för definition, kvalitet och förvaltning.

- **Misstag: Att beskriva informationsflöden utan regelverksfrågor.**
  - Varför det händer: Flöden ritas ofta som tekniska överföringar.
  - Hur du undviker det: Lägg till frågor om sekretess, dataskydd, arkiv, åtkomst och spårbarhet.

- **Misstag: Att använda samma ord för olika saker.**
  - Varför det händer: Olika delar av myndigheten har lokala arbetssätt och historiska begrepp.
  - Hur du undviker det: Etablera en enkel begreppslista och markera begrepp som kräver beslut.

## Arbetsgång: ta fram informationsperspektivet

Använd följande arbetsgång när du tar fram börläget för information:

1. Utgå från arbetssätt, målbild och problembild.
2. Identifiera centrala informationsobjekt.
4. Beskriv de viktigaste informationsflödena.
5. Dokumentera informationsägarskap och kvalitetsansvar.
6. Formulera informationskrav.
7. Identifiera regelverks-, säkerhets- och arkivfrågor.
8. Synliggör beroenden till andra utvecklingsområden.
9. Beskriv konsekvenser för verktyg, teknik och organisation.
10. Markera frågor som kräver beslut eller fördjupning.

## Exempel: från behov till informationskrav

Anta att utvecklingsområdet arbetar med ett nytt arbetssätt för handläggning. Problembilden visar att handläggare i dag saknar gemensam bild av ärendestatus och att uppföljningen bygger på manuella sammanställningar.

Ett börläge för information kan då innehålla:

- ett gemensamt begrepp för ärendestatus
- en beslutad uppsättning statusvärden
- tydligt ansvar för vem som får ändra status
- krav på loggning av statusändringar
- koppling mellan status och uppföljningsrapportering
- krav på att andra utvecklingsområden kan tolka status på samma sätt
- regelverksfråga om vilka uppgifter som får visas för olika roller

Det här är mer användbart än att bara skriva att “ärendedata ska vara tillgänglig”. Det visar vad informationen betyder, hur den används och vilka krav som följer av användningen.

## Leverabler från informationsarbetet

Ett färdigt informationsperspektiv i börläget kan bestå av:

- kort text om informationsperspektivets roll i börläget
- lista över centrala informationsobjekt
- begreppsbild eller begreppslista
- en eller flera informationsflödesbilder
- tabell över informationsägarskap och kvalitetsansvar
- lista över informationskrav
- identifierade regelverks- och säkerhetsfrågor
- beroenden till andra utvecklingsområden
- beslutspunkter och frågor för fördjupning

Det behöver inte vara långt. Det behöver vara begripligt, spårbart och användbart i fortsatt arkitekturarbete.

## Övningar

### Övning 1: Identifiera informationsobjekt

Välj ett arbetssätt från ditt utvecklingsområde. Lista de fem viktigaste informationsobjekten som arbetssättet behöver.

För varje informationsobjekt, skriv:

- kort definition
- var det skapas
- var det används
- vem som bör ansvara för kvaliteten
- vilken risk som uppstår om informationen är fel

### Övning 2: Rita ett informationsflöde

Välj ett informationsobjekt som delas mellan minst två roller, system eller utvecklingsområden. Rita ett enkelt flöde som visar var informationen uppstår, hur den används och vilka överlämningar som finns.

Markera särskilt:

- manuell hantering
- beroenden till andra utvecklingsområden
- risk för olika tolkningar
- krav på spårbarhet eller sekretess

### Fördjupning

Välj ett begrepp som ofta används otydligt i organisationen. Skriv tre möjliga definitioner som olika aktörer skulle kunna ha. Diskutera vilken definition som bör gälla i börläget och vilka konsekvenser den får.

## Snabb sammanfattning

- Informationsperspektivet binder ihop verksamhet, IT, regelverk och styrning.
- Börja med begrepp och informationsobjekt innan du går in på datafält.
- Beskriv informationsflöden där information skapas, ändras, delas eller används.
- Tydliggör informationsägarskap, kvalitetsansvar och förvaltningsansvar.
- Formulera informationskrav som påverkar arkitektur och genomförande.
- Synliggör beroenden till andra utvecklingsområden tidigt.
- Regelverk, säkerhet, arkiv och dataskydd ska vara integrerade delar av informationsperspektivet.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan ett begrepp och ett informationsobjekt?
2. Varför är informationsägarskap viktigt i ett börläge?
3. Vilka risker uppstår om olika utvecklingsområden använder samma begrepp på olika sätt?
4. När räcker en enkel begreppsbild och när behövs en mer detaljerad informationsmodell?
5. Hur kan informationskrav påverka teknikval och systemstöd?

## Nästa steg

I nästa kapitel går vi vidare till verktyg och teknik. Där använder vi informationsperspektivet som underlag för att förstå vilka systemstöd, integrationer, plattformar och tekniska vägval som krävs för börläget.

<div class="pagebreak"></div>

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

<div class="pagebreak"></div>

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

<div class="pagebreak"></div>

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

<div class="pagebreak"></div>

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

<div class="pagebreak"></div>

# Kapitel 13: Ta fram färdplan och övergångsarkitektur

## Varför detta kapitel finns

Ett börläge blir användbart först när det kan omsättas i genomförbara steg. När arkitekturen beskriver vart utvecklingsområdet ska, behöver färdplanen beskriva hur området kan röra sig dit utan att tappa styrning, leveransförmåga eller regelefterlevnad.

Det här kapitlet visar hur verksamhetsarkitekter och IT-arkitekter kan ta fram en färdplan och en eller flera övergångsarkitekturer. Fokus ligger på att skapa en praktiskt användbar bro mellan nuläge och börläge.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara skillnaden mellan börläge, färdplan och övergångsarkitektur
- dela upp förändringen i etapper som är möjliga att genomföra
- identifiera beroenden, beslutspunkter och risker i genomförandet
- formulera övergångslägen som ger nytta utan att kräva att allt är klart
- använda färdplanen som underlag för prioritering, styrning och förankring

## Innan vi börjar

I föregående kapitel analyserades gap och konsekvenser. Där blev det tydligare vad som skiljer nuläge från börläge och vilka områden som kräver förändring. Färdplanen använder den analysen som startpunkt.

En färdplan ska inte vara en detaljerad projektplan. Den ska visa förändringens logik: vilka steg som behöver tas, varför de kommer i en viss ordning och vilka förutsättningar som måste finnas på plats.

## Huvudförklaring

### Färdplanens roll

Färdplanen beskriver vägen från nuläge till börläge. Den ska hjälpa utvecklingsområdet att fatta bättre beslut om prioritering, beroenden och genomförande.

En bra färdplan svarar på frågor som:

- Vad behöver göras först?
- Vilka förändringar måste hänga ihop?
- Vilka delar kan genomföras oberoende av varandra?
- Var finns viktiga beslutspunkter?
- När uppstår verksamhetsnytta?
- Vilka risker behöver hanteras innan nästa steg tas?

Färdplanen ska vara tillräckligt konkret för att styra arbetet, men inte så detaljerad att den snabbt blir inaktuell.

### Övergångsarkitektur

En övergångsarkitektur beskriver ett mellanläge på vägen mot börläget. Den visar hur verksamhet, information, arbetssätt, system och teknik ska hänga ihop under en period då allt ännu inte är färdigt.

Övergångsarkitektur behövs ofta när:

- gamla och nya lösningar behöver samexistera
- ett regelverk införs stegvis
- information flyttas från en struktur till en annan
- arbetssätt förändras innan alla verktyg är på plats
- tekniska beroenden gör att börläget inte kan införas direkt

Utan övergångsarkitektur finns risk att genomförandet skapar nya otydligheter. Då kan utvecklingsområdet få flera parallella tillfälliga lösningar som inte leder mot samma mål.

### Från gap till genomförbara steg

Ett praktiskt sätt att ta fram färdplanen är att börja med gapen från föregående kapitel och gruppera dem i förändringspaket.

Ett förändringspaket är en samlad del av förändringen som har ett tydligt syfte. Det kan till exempel vara att etablera informationsägarskap, införa ett gemensamt arbetssätt för prioritering eller modernisera en integration.

För varje förändringspaket bör arkitekterna beskriva:

- vilken nytta förändringen ska ge
- vilka arkitekturperspektiv som påverkas
- vilka beroenden som finns
- vilka beslut som krävs
- vilka risker som behöver hanteras
- vilket övergångsläge som kan vara acceptabelt

### Etapper och ordningsföljd

Alla förändringar kan inte göras samtidigt. Därför behöver färdplanen delas in i etapper. En etapp bör vara tillräckligt liten för att kunna styras, men tillräckligt stor för att ge tydlig verksamhetsnytta.

En vanlig indelning är:

- Etapp 1: skapa förutsättningar
- Etapp 2: etablera grundläggande förmågor
- Etapp 3: skala upp och integrera
- Etapp 4: stabilisera och optimera

Det viktiga är inte vad etapperna heter, utan att varje etapp har ett tydligt syfte och en tydlig koppling till börläget.

### Beslutspunkter

Färdplanen bör innehålla beslutspunkter. En beslutspunkt är ett tillfälle där utvecklingsområdet behöver välja riktning, godkänna nästa steg eller ompröva tidigare antaganden.

Exempel på beslutspunkter är:

- godkännande av målbild eller principer
- beslut om informationsägarskap
- val av teknisk lösningsriktning
- beslut om avveckling av äldre systemstöd
- prioritering mellan två förändringspaket
- beslut om att gå från pilot till bredare införande

Beslutspunkter gör färdplanen användbar i styrning. De visar var arkitekturen behöver möta planering, ekonomi, portföljstyrning och ledningsbeslut.

## Exempel

Ett utvecklingsområde har tagit fram ett börläge där ärendeinformation ska hanteras mer enhetligt. Gap-analysen visar att nuläget består av flera olika begreppsmodeller, delvis överlappande systemstöd och otydliga informationsägare.

Arkitekterna grupperar förändringen i fyra förändringspaket:

| Förändringspaket | Syfte | Viktigt beroende |
|---|---|---|
| Gemensam begreppsmodell | Skapa gemensamt språk | Verksamhetsförankring |
| Informationsägarskap | Tydliggöra ansvar | Beslut i styrforum |
| Integrationsprinciper | Minska speciallösningar | Teknisk målarkitektur |
| Successiv avveckling | Fasa ut dubblerat stöd | Finansiering och tidplan |

Utifrån detta föreslås tre etapper.

Etapp 1 etablerar begreppsmodell och informationsägarskap. Etapp 2 inför integrationsprinciper i nya initiativ. Etapp 3 avvecklar äldre lösningar när beroenden och finansiering är hanterade.

Övergångsarkitekturen beskriver hur gamla och nya informationsflöden får samexistera under etapp 2, men också vilka regler som gäller för att undvika att nya speciallösningar byggs.

## Vanliga misstag

- **Misstag: Att göra färdplanen till en projektplan.**
  - Varför det händer: Det finns ofta en förväntan på detaljerade aktiviteter, tidpunkter och ansvar.
  - Hur du undviker det: Håll färdplanen på arkitektur- och förändringsnivå. Länka till projektplaner där detaljstyrning behövs.

- **Misstag: Att hoppa direkt från nuläge till börläge.**
  - Varför det händer: Börläget känns tydligt på papperet.
  - Hur du undviker det: Beskriv minst ett realistiskt övergångsläge där gamla och nya arbetssätt kan samexistera.

- **Misstag: Att sakna beslutspunkter.**
  - Varför det händer: Färdplanen skrivs som en lista med aktiviteter.
  - Hur du undviker det: Markera var styrning, finansiering, arkitekturgranskning eller verksamhetsbeslut krävs.

- **Misstag: Att underskatta organisatoriska beroenden.**
  - Varför det händer: Teknik och system är ofta lättare att beskriva än ansvar, mandat och arbetssätt.
  - Hur du undviker det: Pröva varje etapp mot perspektiven arbetssätt, resurser, information, verktyg, teknik och regelverk.

## Övningar

### Övning 1: Gruppera gap till förändringspaket

Utgå från en gap-analys för ett utvecklingsområde. Gruppera gapen i tre till sex förändringspaket.

Beskriv för varje paket:

- syfte
- berörda arkitekturperspektiv
- viktigaste beroende
- möjlig första åtgärd
- förväntad nytta

### Övning 2: Skapa en enkel färdplan

Välj tre förändringspaket och placera dem i en föreslagen ordning.

Besvara:

1. Vad behöver komma först?
2. Vad kan göras parallellt?
3. Var uppstår första tydliga nyttan?
4. Vilka beslut krävs innan nästa etapp?
5. Vilket övergångsläge behöver beskrivas?

### Fördjupning

Granska en befintlig roadmap eller portföljplan. Identifiera om den innehåller arkitekturmässiga övergångslägen eller om den främst beskriver aktiviteter.

Notera:

- vilka arkitekturberoenden som är synliga
- vilka som saknas
- vilka beslutspunkter som borde läggas till
- om färdplanen tydligt leder mot börläget

## Snabb sammanfattning

- Färdplanen beskriver vägen från nuläge till börläge.
- Övergångsarkitektur beskriver fungerande mellanlägen.
- Gap bör grupperas till förändringspaket.
- Etapper ska ha tydlig nytta och rimlig genomförbarhet.
- Beslutspunkter gör färdplanen användbar i styrning.
- Färdplanen ska vara mer än en aktivitetslista och mindre detaljerad än en projektplan.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan ett börläge och en färdplan?
2. När behövs en övergångsarkitektur?
3. Varför är förändringspaket ofta mer användbara än en lång lista med gap?
4. Vilka beslutspunkter skulle behövas i ett utvecklingsområde du känner till?
5. Hur kan en färdplan bli för detaljerad?

## Nästa steg

När färdplanen finns behöver den kommuniceras och förankras. Nästa kapitel handlar om hur börläge, arkitektur och färdplan kan presenteras för olika målgrupper så att de leder till förståelse, beslut och faktisk användning.

<div class="pagebreak"></div>

# Kapitel 14: Kommunicera och förankra börläget

## Varför detta kapitel finns

Ett börläge får bara effekt om andra förstår det, använder det och fattar beslut utifrån det. Arkitekturarbete kan vara väl genomfört men ändå få svagt genomslag om resultatet presenteras på fel nivå, med fel språk eller utan koppling till mottagarens ansvar.

Det här kapitlet handlar om hur verksamhetsarkitekter och IT-arkitekter kan kommunicera och förankra börläge, arkitektur och färdplan. Fokus ligger på att anpassa budskapet till olika målgrupper utan att förlora arkitekturens innehåll.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- identifiera vilka målgrupper som behöver förstå börläget
- anpassa arkitekturbudskap till ledning, verksamhet, produktledning, team och arkitekturforum
- skilja mellan information, förankring och beslut
- använda vyer och berättelser för att göra börläget begripligt
- planera för återkoppling och justering utan att tappa riktning

## Innan vi börjar

I föregående kapitel togs färdplan och övergångsarkitektur fram. Det gav en väg från nuläge till börläge. Nästa utmaning är att göra vägen begriplig för de som ska besluta, finansiera, prioritera, genomföra eller leva med förändringen.

Kommunikation är inte ett sista steg efter arkitekturarbetet. Den behöver ske löpande. Tidig förankring minskar risken att börläget blir en skrivbordsprodukt.

## Huvudförklaring

### Börläget har flera mottagare

Ett utvecklingsområde i en större myndighet har ofta många intressenter. Alla behöver inte förstå allt, men varje målgrupp behöver förstå det som påverkar deras ansvar och beslut.

Typiska målgrupper är:

- ledning och styrgrupper
- produktledning eller portföljstyrning
- verksamhetsföreträdare
- utvecklingsteam
- förvaltnings- och driftorganisation
- informationssäkerhet, juridik och dataskydd
- andra utvecklingsområden
- arkitekturforum eller design authority

Samma börläge behöver därför kunna beskrivas med flera vyer. Ledningen behöver förstå riktning, nytta, risker och beslut. Team behöver förstå konsekvenser för lösningar, gränssnitt och arbetssätt. Verksamheten behöver förstå hur arbetssätt, ansvar och informationsflöden påverkas.

### Skillnaden mellan information, förankring och beslut

Det är lätt att säga att något ska förankras utan att definiera vad det innebär. I praktiken finns minst tre olika kommunikationssyften.

| Syfte | Vad det betyder | Exempel |
|---|---|---|
| Information | Mottagaren ska känna till innehållet | Genomgång av målbild i ett områdesmöte |
| Förankring | Mottagaren ska förstå och kunna ge återkoppling | Workshop med verksamhetsrepresentanter |
| Beslut | Mottagaren ska ta ställning till vägval | Styrgruppsbeslut om princip eller färdplan |

När syftet är otydligt uppstår missförstånd. En presentation som var tänkt som information kan uppfattas som ett beslut. En workshop som borde ge återkoppling kan bli en ensidig genomgång.

### Anpassa budskapet utan att förenkla bort innehållet

Att anpassa budskapet betyder inte att ta bort svåra frågor. Det betyder att börja i mottagarens perspektiv.

För ledning kan budskapet struktureras kring:

- varför förändringen behövs
- vilka effekter börläget ger
- vilka risker som minskar eller uppstår
- vilka beslut som krävs
- vilka konsekvenser det får att inte agera

För verksamhetsföreträdare kan budskapet struktureras kring:

- hur arbetssätt och ansvar förändras
- vilken nytta det ger i vardagen
- vilka roller som påverkas
- vilka begrepp och informationsobjekt som blir gemensamma
- vilka frågor som behöver förtydligas

För IT- och utvecklingsteam kan budskapet struktureras kring:

- tekniska vägval
- beroenden
- integrationsprinciper
- informationsflöden
- övergångslägen
- vad teamen ska börja eller sluta göra

### Använd vyer

En vy är en avgränsad beskrivning av arkitekturen för ett särskilt syfte. En vy ska inte visa allt. Den ska visa det som behövs för en fråga eller målgrupp.

Exempel på vyer är:

- effektvy: vilka effekter börläget ska ge
- förmågevy: vilka förmågor som stärks eller förändras
- processvy: hur arbetssätt påverkas
- informationsvy: centrala begrepp, objekt och flöden
- systemvy: berörda system, integrationer och ansvar
- färdplansvy: etapper, beroenden och beslutspunkter
- riskvy: risker, osäkerheter och åtgärder

En god vy har en tydlig rubrik, ett tydligt syfte och en kort förklaring av vad mottagaren ska titta efter.

### Berätta förändringens logik

Börläget blir lättare att förstå om det presenteras som en sammanhängande berättelse.

En enkel struktur är:

1. Det här är problemet eller möjligheten.
2. Det här visar nuläget.
3. Det här är riktningen.
4. Det här är börläget.
5. Det här är konsekvenserna.
6. Det här är vägen dit.
7. Det här behöver vi besluta eller göra härnäst.

Denna struktur hjälper mottagare att förstå varför arkitekturen ser ut som den gör. Den gör också att diagram och modeller inte står ensamma.

### Förankring som tvåvägskommunikation

Förankring handlar inte bara om att få andra att acceptera arkitekturen. Det handlar också om att pröva om arkitekturen håller.

Bra förankring kan visa:

- att ett antagande är fel
- att ett beroende saknas
- att en målgrupp påverkas mer än väntat
- att ett regelverk behöver tolkas annorlunda
- att färdplanen är för snabb eller för långsam
- att ett övergångsläge behöver beskrivas tydligare

Därför bör arkitekterna planera hur återkoppling tas emot, bedöms och dokumenteras. Alla synpunkter behöver inte leda till ändring, men de behöver hanteras transparent.

## Exempel

Ett utvecklingsområde har tagit fram ett börläge för mer enhetlig informationshantering. Arkitekterna behöver förankra detta med fyra målgrupper.

| Målgrupp | Huvudbudskap | Format | Önskad effekt |
|---|---|---|---|
| Styrgrupp | Beslut krävs om informationsägarskap och etappindelning | Beslutsunderlag | Tydligt vägval |
| Verksamhetsrepresentanter | Nya roller och begrepp påverkar arbetssätt | Workshop | Återkoppling och acceptans |
| Utvecklingsteam | Nya integrationsprinciper påverkar lösningsdesign | Teknisk genomgång | Gemensam riktning |
| Arkitekturforum | Börläge och övergångsarkitektur behöver granskas | Arkitekturgenomgång | Kvalitetssäkring |

Arkitekterna använder samma övergripande berättelse, men olika vyer. För styrgruppen visas färdplan, risker och beslutspunkter. För verksamheten visas roller, informationsobjekt och arbetssätt. För teamen visas tekniska beroenden och övergångslösningar.

## Vanliga misstag

- **Misstag: Att visa samma material för alla.**
  - Varför det händer: Arkitekterna vill vara konsekventa och undvika dubbelarbete.
  - Hur du undviker det: Använd samma grundinnehåll men skapa olika vyer för olika målgrupper.

- **Misstag: Att börja med modeller i stället för problem.**
  - Varför det händer: Modellerna är arkitekternas huvudsakliga arbetsprodukt.
  - Hur du undviker det: Börja med varför börläget behövs och vilken fråga modellen besvarar.

- **Misstag: Att kalla information för förankring.**
  - Varför det händer: En presentation känns som att budskapet har nått fram.
  - Hur du undviker det: Planera aktiv återkoppling, frågor och dokumenterad hantering av synpunkter.

- **Misstag: Att tona ned osäkerheter.**
  - Varför det händer: Arkitekterna vill skapa trygghet och framdrift.
  - Hur du undviker det: Beskriv osäkerheter öppet och koppla dem till beslutspunkter eller utredningsbehov.

## Övningar

### Övning 1: Målgruppskarta

Välj ett börläge eller en förändring i ett utvecklingsområde. Lista de målgrupper som behöver förstå eller påverka arbetet.

För varje målgrupp, beskriv:

- vad de behöver förstå
- vilket beslut eller beteende som påverkas
- vilken vy som passar bäst
- vilket format som bör användas
- vilken återkoppling som behövs

### Övning 2: Anpassa ett budskap

Skriv en kort presentation av samma börläge för tre målgrupper:

1. ledning
2. verksamhetsrepresentanter
3. utvecklingsteam

Jämför texterna. Vad är samma? Vad skiljer sig? Finns det något som riskerar att förenklas för mycket?

### Fördjupning

Ta en arkitekturmodell som redan finns i organisationen. Bedöm om den är begriplig för en person som inte varit med i arbetet.

Undersök:

- om syftet med modellen framgår
- om viktiga begrepp är förklarade
- om målgruppen är tydlig
- om modellen visar för mycket eller för lite
- om modellen leder till en fråga, ett beslut eller en handling

## Snabb sammanfattning

- Börläget behöver kommuniceras olika till olika målgrupper.
- Information, förankring och beslut är olika kommunikationssyften.
- Vyer gör arkitekturen begriplig utan att visa allt samtidigt.
- En berättelse om nuläge, riktning, börläge och väg framåt hjälper mottagaren.
- Förankring är också ett sätt att testa arkitekturen.
- Återkoppling behöver dokumenteras och hanteras öppet.

## Quiz/reflektionsfrågor

1. Vilka målgrupper behöver förstå ett börläge i ditt utvecklingsområde?
2. Vad är skillnaden mellan att informera och att förankra?
3. Vilken vy skulle vara mest användbar för en styrgrupp?
4. Vilken vy skulle vara mest användbar för ett utvecklingsteam?
5. Hur kan arkitekter visa osäkerheter utan att skapa onödig oro?

## Nästa steg

När börläge, arkitektur och färdplan är kommunicerade behöver de kvalitetssäkras. Nästa kapitel handlar om granskningsfrågor, definition of done, spårbarhet, konsistens och vanliga fallgropar.

<div class="pagebreak"></div>

# Kapitel 15: Kvalitetssäkra arkitekturen

## Varför detta kapitel finns

Ett börläge och en tillhörande arkitektur behöver vara mer än välformulerade texter och snygga diagram. De behöver vara begripliga, spårbara, konsekventa och användbara som stöd för beslut och genomförande.

Det här kapitlet visar hur verksamhetsarkitekter och IT-arkitekter kan kvalitetssäkra arkitekturen innan den används som underlag för styrning, prioritering och utveckling.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva vad kvalitet betyder i ett börläge och en arkitektur
- använda granskningsfrågor för olika arkitekturperspektiv
- kontrollera spårbarhet mellan behov, mål, principer, börläge, gap och färdplan
- identifiera inkonsekvenser mellan arkitekturvyer
- formulera en praktisk definition of done för arkitekturleverabler
- undvika vanliga kvalitetsbrister i arkitekturarbete

## Innan vi börjar

I föregående kapitel behandlades kommunikation och förankring. Förankringen ger ofta viktig återkoppling, men återkoppling räcker inte som kvalitetssäkring. Arkitekturen behöver också granskas systematiskt.

Kvalitetssäkring handlar inte om att göra materialet perfekt. Det handlar om att göra det tillräckligt tydligt, sammanhängande och beslutsbart.

## Huvudförklaring

### Vad betyder kvalitet i arkitektur?

Kvalitet i arkitektur kan beskrivas med fem frågor.

1. Är arkitekturen begriplig?
2. Är den spårbar?
3. Är den konsekvent?
4. Är den genomförbar?
5. Är den användbar för beslut och genomförande?

Om svaret är nej på någon av frågorna behöver materialet justeras eller kompletteras.

En arkitektur kan vara tekniskt korrekt men ändå ha låg kvalitet om den inte går att använda i praktiken. Den kan också vara lättläst men otillräcklig om viktiga beroenden, risker eller beslut saknas.

### Spårbarhet

Spårbarhet innebär att det går att följa en röd tråd från behov och problem till målbild, principer, börläge, gap, färdplan och beslut.

En enkel spårbarhetskedja kan se ut så här:

| Del | Fråga |
|---|---|
| Behov | Vilket problem eller vilken möjlighet adresseras? |
| Mål | Vilken effekt ska uppnås? |
| Princip | Vilken riktning styr lösningen? |
| Börläge | Hur ska området fungera när förändringen är genomförd? |
| Gap | Vad saknas i nuläget? |
| Färdplan | Hur tas stegen mot börläget? |
| Beslut | Vad behöver beslutas för att gå vidare? |

När spårbarheten saknas blir det svårt att veta varför en viss rekommendation finns. Då blir arkitekturen också svårare att försvara när prioriteringar ändras.

### Konsistens mellan perspektiv

Börläget täcker flera perspektiv: arbetssätt, resurser, information, verktyg, teknik och regelverk. Kvalitetssäkring behöver kontrollera att dessa perspektiv hänger ihop.

Exempel på konsistensfrågor är:

- Stödjer verktygen det arbetssätt som beskrivs?
- Finns resurser och roller för det ansvar som börläget kräver?
- Är informationsägarskap kopplat till arbetssätt och styrning?
- Är tekniska vägval förenliga med regelverk och säkerhetskrav?
- Är färdplanens etapper rimliga utifrån organisatoriska beroenden?
- Finns konflikter mellan principer, mål och föreslagna lösningar?

Om perspektiven inte är konsistenta riskerar börläget att bli en samling fristående önskelistor.

### Granskning på rätt nivå

Allt behöver inte granskas av alla. Kvalitetssäkring blir bättre om olika delar granskas av rätt personer.

Exempel:

- verksamhetsrepresentanter granskar arbetssätt, ansvar och nytta
- informationsägare granskar begrepp, informationsobjekt och kvalitet
- IT-arkitekter granskar teknik, integrationer och systemberoenden
- juridik, dataskydd och informationssäkerhet granskar regelverksfrågor
- styrning eller ledning granskar beslut, prioritering och konsekvenser
- arkitekturforum granskar helhet, principer och konsistens

Arkitekterna behöver samordna granskningen så att återkoppling inte behandlas som separata kommentarer utan vägs mot helheten.

### Definition of done för arkitektur

En definition of done beskriver när arkitekturleveransen är tillräckligt klar för sitt syfte. Den behöver vara praktisk och kopplad till hur materialet ska användas.

En möjlig definition of done för ett börläge är:

- syfte och målgrupp är tydliga
- nuläge och behov är sammanfattade
- börläge är beskrivet för relevanta perspektiv
- centrala begrepp är definierade
- viktiga beroenden och risker är identifierade
- gap och konsekvenser är analyserade
- färdplan och övergångslägen är beskrivna
- beslutspunkter är tydliga
- materialet är granskat av relevanta roller
- återkoppling är dokumenterad och hanterad
- öppna frågor är tydligt markerade

Definition of done ska inte användas som byråkratisk spärr. Den ska hjälpa utvecklingsområdet att veta när arkitekturen är tillräckligt stabil för nästa steg.

## Exempel

Ett utvecklingsområde har tagit fram ett börläge för en ny informationshantering. Materialet består av målbild, informationsmodell, systemöversikt, gap-analys och färdplan.

Vid granskning upptäcks tre kvalitetsbrister.

| Brist | Konsekvens | Åtgärd |
|---|---|---|
| Informationsägare saknas i modellen | Oklart ansvar i börläget | Lägg till ansvarsvy och beslutspunkt |
| Färdplanen saknar övergångsläge | Risk för parallella lösningar | Beskriv samexistens mellan gamla och nya flöden |
| Regelverkskrav är nämnda men inte kopplade till lösningsval | Svag spårbarhet | Lägg till spårbarhet från krav till arkitekturprincip |

Efter åtgärderna blir arkitekturen lättare att använda i styrgruppen. Den visar inte bara vad som ska förändras, utan också varför och vilka beslut som krävs.

## Vanliga misstag

- **Misstag: Att granska stavning i stället för arkitektur.**
  - Varför det händer: Språkliga fel är lätta att hitta.
  - Hur du undviker det: Börja med spårbarhet, konsistens, beslutbarhet och genomförbarhet.

- **Misstag: Att allt skickas till alla.**
  - Varför det händer: Arkitekterna vill vara inkluderande.
  - Hur du undviker det: Rikta granskningen. Olika roller ska granska olika frågor.

- **Misstag: Att öppna frågor döljs.**
  - Varför det händer: Materialet ska kännas färdigt.
  - Hur du undviker det: Markera öppna frågor tydligt och koppla dem till beslut eller fortsatt analys.

- **Misstag: Att definition of done blir för tung.**
  - Varför det händer: Organisationen vill säkra kvalitet genom många kontrollpunkter.
  - Hur du undviker det: Gör definitionen kort, praktisk och kopplad till leveransens syfte.

## Övningar

### Övning 1: Granska spårbarhet

Välj en arkitekturleverans eller ett börläge. Försök följa kedjan:

1. behov
2. mål
3. princip
4. börläge
5. gap
6. färdplan
7. beslut

Markera var kedjan är stark och var den bryts.

### Övning 2: Kontrollera konsistens mellan perspektiv

Välj två perspektiv, till exempel information och teknik. Svara på:

- stödjer de varandra?
- finns begrepp eller objekt i ett perspektiv som saknas i det andra?
- finns beroenden som inte är beskrivna?
- finns målkonflikter?

Gör sedan samma sak för arbetssätt och resurser.

### Fördjupning

Skapa en egen definition of done för börläge i din organisation. Den ska rymmas på en sida och kunna användas i ett arkitekturforum eller vid intern kvalitetssäkring.

Testa definitionen på ett befintligt material. Notera vilka punkter som hjälper och vilka som känns onödiga.

## Snabb sammanfattning

- Kvalitet i arkitektur handlar om begriplighet, spårbarhet, konsistens, genomförbarhet och beslutbarhet.
- Spårbarhet gör det möjligt att förstå varför rekommendationer finns.
- Perspektiven arbetssätt, resurser, information, verktyg, teknik och regelverk behöver granskas tillsammans.
- Rätt roller bör granska rätt delar.
- Definition of done hjälper arkitekterna att veta när materialet är tillräckligt klart.
- Öppna frågor ska synliggöras, inte döljas.

## Quiz/reflektionsfrågor

1. Vad betyder spårbarhet i ett börläge?
2. Vilka perspektiv behöver oftast granskas tillsammans?
3. Varför är det riskabelt att skicka allt material till alla granskare?
4. Vad bör ingå i en definition of done för arkitektur?
5. Hur kan öppna frågor hanteras utan att skapa osäkerhet?

## Nästa steg

När arkitekturen är kvalitetssäkrad är det dags att visa hur alla delar kan användas tillsammans. Nästa kapitel innehåller ett sammanhållet praktiskt exempel där ett utvecklingsområde går från start till börläge.

<div class="pagebreak"></div>

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

<div class="pagebreak"></div>

# Kapitel 17: Mallbibliotek och checklistor

## Varför detta kapitel finns

Den här boken har beskrivit hur verksamhetsarkitekter och IT-arkitekter kan ta fram börläge och tillhörande arkitektur för ett utvecklingsområde. För att arbetssättet ska bli användbart i vardagen behövs praktiska mallar, checklistor och stödfrågor.

Det här kapitlet samlar återanvändbara mallar som kan användas när ett utvecklingsområde ska planera, genomföra, förankra och kvalitetssäkra arkitekturarbetet.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- använda enkla mallar för att starta arkitekturarbetet
- planera intervjuer och workshops
- dokumentera mål, principer, börläge, gap och färdplan
- kontrollera att olika arkitekturperspektiv hänger ihop
- förbereda beslutsunderlag och granskning
- anpassa mallarna till den egna myndighetens arbetssätt

## Innan vi börjar

Mallarna i kapitlet är inte tänkta att användas mekaniskt. De ska ses som startpunkter. Varje utvecklingsområde behöver anpassa dem efter uppdrag, styrning, mognad och vilka beslut som ska fattas.

En bra mall hjälper arbetet framåt. En dålig användning av en mall skapar dokumentation utan tydlig nytta.

## Mall 1: Uppdragsbeskrivning

Använd denna mall när arkitekturarbetet startar.

| Fråga | Svar |
|---|---|
| Vilket utvecklingsområde gäller uppdraget? | |
| Varför behövs ett börläge? | |
| Vilka beslut ska börläget stödja? | |
| Vilka arkitekturperspektiv omfattas? | |
| Vilka perspektiv är särskilt viktiga? | |
| Vilka avgränsningar gäller? | |
| Vilka beroenden finns till andra områden? | |
| Vilka roller deltar i arbetet? | |
| När behöver första användbara resultat finnas? | |

## Mall 2: Intressentkarta

Använd denna mall för att identifiera vilka som behöver bidra, förstå eller fatta beslut.

| Intressent | Roll i arbetet | Behöver bidra med | Behöver förstå | Beslut eller påverkan |
|---|---|---|---|---|
| | | | | |
| | | | | |

Exempel på intressenter:

- verksamhetsföreträdare
- produktägare
- teamrepresentanter
- informationsägare
- IT-arkitekt
- verksamhetsarkitekt
- säkerhetsfunktion
- juridik eller dataskydd
- förvaltningsansvariga
- styrgrupp
- arkitekturforum

## Mall 3: Intervjuguide

Använd intervjuer för att förstå nuläge, problem, behov och beroenden.

### Startfrågor

1. Vilken roll har du i eller nära utvecklingsområdet?
2. Vilka delar av arbetet fungerar bra i dag?
3. Vilka problem återkommer ofta?
4. Vilka beslut eller vägval är otydliga?
5. Vilka informationsflöden är viktiga?
6. Vilka system eller verktyg är centrala?
7. Vilka regelverk eller interna riktlinjer påverkar arbetet?
8. Vilka beroenden finns till andra områden?
9. Vad skulle ett bättre läge göra möjligt?
10. Vad får inte tappas bort i förändringen?

### Avslutande frågor

1. Vem mer bör vi prata med?
2. Finns dokument, modeller eller beslut vi bör läsa?
3. Vilken risk är störst om inget förändras?
4. Vilken förändring skulle ge mest nytta först?

## Mall 4: Workshop för gemensam problembild

### Syfte

Skapa en gemensam bild av nuläge, problem, konsekvenser och prioriterade behov.

### Föreslagen agenda

| Tid | Moment | Resultat |
|---|---|---|
| 10 min | Syfte och avgränsning | Gemensam start |
| 20 min | Individuell probleminsikt | Lista med observationer |
| 30 min | Klustring av problem | Teman |
| 30 min | Konsekvensdiskussion | Förståelse för påverkan |
| 20 min | Prioritering | Viktigaste problemområden |
| 10 min | Nästa steg | Tydliga åtgärder |

### Stödfrågor

- Vilka problem hindrar utvecklingsområdet mest?
- Vilka problem påverkar flera team eller funktioner?
- Vilka problem beror på otydliga begrepp, ansvar eller beslut?
- Vilka problem är symptom på större strukturella frågor?
- Vilka problem behöver lösas först för att annat ska bli möjligt?

## Mall 5: Mål och principer

Använd mallen när målbild och vägledande principer formuleras.

| Mål | Varför målet behövs | Hur vi märker att vi närmar oss målet |
|---|---|---|
| | | |
| | | |

| Princip | Innebörd | Konsekvens | Undantag |
|---|---|---|---|
| | | | |
| | | | |

Kontrollfrågor:

- Är målen kopplade till verkliga behov?
- Är principerna vägledande nog för svåra beslut?
- Finns konflikter mellan principerna?
- Är undantag möjliga att hantera?
- Behöver principerna beslutas eller bara användas som arbetsstöd?

## Mall 6: Börläge per arkitekturperspektiv

Använd mallen för att strukturera börläget.

| Perspektiv | Frågor att besvara | Leverabler |
|---|---|---|
| Arbetssätt | Hur ska arbetet fungera? Vilka flöden, roller och ansvar behövs? | Processvy, ansvarsvy |
| Resurser | Vilka kompetenser, team och mandat krävs? | Rollkarta, ansvarsfördelning |
| Information | Vilka begrepp, objekt och flöden är centrala? | Informationsvy, begreppslista |
| Verktyg | Vilket systemstöd behövs för arbetssättet? | Verktygskarta, användningsvy |
| Teknik | Vilka tekniska mönster, integrationer och plattformar behövs? | Systemvy, integrationsvy |
| Regelverk | Vilka lagar, riktlinjer och styrkrav påverkar börläget? | Regelverkskarta, kontrollpunkter |

## Mall 7: Gap-analys

Använd mallen efter att nuläge och börläge är tillräckligt beskrivna.

| Område | Nuläge | Börläge | Gap | Konsekvens | Prioritet | Möjlig åtgärd |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |

Kontrollfrågor:

- Är gapet beskrivet konkret?
- Är konsekvensen tydlig?
- Är gapet kopplat till ett mål eller en princip?
- Finns beroenden till andra gap?
- Är åtgärden rimlig för utvecklingsområdet?

## Mall 8: Förändringspaket

Använd mallen för att gruppera gap till genomförbara delar.

| Förändringspaket | Syfte | Berörda perspektiv | Beroenden | Risker | Första steg |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |

Stödfrågor:

- Vilka gap hör naturligt ihop?
- Vilka förändringar behöver genomföras i samma etapp?
- Vilka förändringar kan vänta?
- Vilka paket ger tidig nytta?
- Vilka paket kräver beslut eller finansiering?

## Mall 9: Färdplan

Använd mallen för att beskriva vägen mot börläget.

| Etapp | Fokus | Viktiga leverabler | Beslutspunkt | Nytta | Risker |
|---|---|---|---|---|---|
| Etapp 1 | | | | | |
| Etapp 2 | | | | | |
| Etapp 3 | | | | | |

Kontrollfrågor:

- Leder etapperna mot börläget?
- Finns tydliga beslutspunkter?
- Finns övergångslägen där de behövs?
- Är organisatoriska beroenden synliga?
- Är färdplanen tillräckligt konkret utan att bli projektplan?

## Mall 10: Övergångsarkitektur

Använd mallen när gamla och nya arbetssätt, system eller informationsflöden behöver samexistera.

| Fråga | Svar |
|---|---|
| Vilket övergångsläge beskrivs? | |
| Varför behövs övergångsläget? | |
| Vilka delar av nuläget finns kvar? | |
| Vilka delar av börläget införs? | |
| Vilka regler gäller under övergången? | |
| Vilka undantag är tillåtna? | |
| Vilka risker behöver följas? | |
| När ska övergångsläget avvecklas? | |
| Vilka beslut krävs? | |

## Mall 11: Beslutsunderlag

Använd mallen när börläge, princip, färdplan eller vägval ska beslutas.

| Del | Innehåll |
|---|---|
| Beslut som efterfrågas | |
| Bakgrund | |
| Rekommendation | |
| Alternativ | |
| Konsekvenser | |
| Risker | |
| Beroenden | |
| Påverkan på verksamhet | |
| Påverkan på IT | |
| Påverkan på regelverk eller säkerhet | |
| Nästa steg | |

Kontrollfrågor:

- Är beslutet tydligt formulerat?
- Är alternativen ärligt beskrivna?
- Är konsekvenser och risker begripliga?
- Framgår vad som händer om beslutet inte tas?
- Är underlaget anpassat till beslutsfattaren?

## Mall 12: Kommunikationsplan

Använd mallen för att planera förankring.

| Målgrupp | Budskap | Vy eller material | Format | Syfte | Återkoppling |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |

Stödfrågor:

- Ska målgruppen informeras, förankras eller fatta beslut?
- Vilken vy behöver målgruppen?
- Vilka frågor kommer målgruppen sannolikt att ställa?
- Hur dokumenteras återkoppling?
- Vem ansvarar för att återkoppling hanteras?

## Mall 13: Kvalitetsgranskning

Använd mallen före beslut eller bredare förankring.

| Kontrollområde | Fråga | Status | Kommentar |
|---|---|---|---|
| Syfte | Är syftet med börläget tydligt? | | |
| Målgrupp | Är mottagare och användning tydliga? | | |
| Spårbarhet | Går det att följa behov till beslut? | | |
| Konsistens | Hänger perspektiven ihop? | | |
| Genomförbarhet | Är färdplanen realistisk? | | |
| Regelverk | Är styrande krav beaktade? | | |
| Beslut | Är beslutspunkter tydliga? | | |
| Risker | Är risker och osäkerheter synliga? | | |
| Öppna frågor | Är öppna frågor dokumenterade? | | |

## Checklista: Definition of done för börläge

Ett börläge är tillräckligt klart när:

- syfte och avgränsning är tydliga
- målgrupper och användning är beskrivna
- behov och problembild är sammanfattade
- mål och principer är formulerade
- relevanta arkitekturperspektiv är beskrivna
- centrala begrepp är definierade
- gap och konsekvenser är analyserade
- färdplan och beslutspunkter finns
- övergångsarkitekturer finns där de behövs
- risker och beroenden är synliga
- materialet är förankrat med relevanta roller
- kvalitetssäkring är genomförd
- öppna frågor är dokumenterade
- nästa steg är tydligt

## Checklista: Vanliga varningssignaler

Var extra uppmärksam om:

- börläget bara beskriver teknik
- verksamhetsnytta är otydlig
- informationsansvar saknas
- regelverk nämns men inte påverkar vägval
- färdplanen saknar beslutspunkter
- övergångslägen saknas trots stora beroenden
- målgruppen för materialet är oklar
- arkitekturvyer visar olika sanningar
- gap-analysen är en lista utan konsekvenser
- allt material skickas till alla utan tydligt granskningssyfte

## Övningar

### Övning 1: Välj rätt mall

Utgå från en situation där ett utvecklingsområde behöver skapa ett börläge. Välj de fem mallar som ger mest nytta först.

Motivera valet utifrån:

- uppdragets tydlighet
- målgrupp
- tidspress
- kända problem
- beslut som behöver fattas

### Övning 2: Anpassa en mall

Välj en mall i kapitlet och anpassa den till din organisation.

Ta bort sådant som inte behövs. Lägg till sådant som ofta saknas. Skriv en kort instruktion för hur mallen ska användas.

### Fördjupning

Skapa ett komplett minimipaket för arkitekturarbete i ett utvecklingsområde.

Paketet ska innehålla:

- en uppdragsmall
- en workshopmall
- en börlägesmall
- en gap-analysmall
- en färdplansmall
- en kvalitetssäkringschecklista

Beskriv hur mallarna används i ordning.

## Snabb sammanfattning

- Mallar ska stödja tänkande, inte ersätta det.
- Börja med uppdrag, intressenter och problembild.
- Beskriv börläget per perspektiv men kvalitetssäkra helheten.
- Gap-analys och förändringspaket skapar bro till färdplanen.
- Beslutsunderlag och kommunikationsplan gör arkitekturen användbar.
- Checklistor hjälper arkitekterna att upptäcka brister innan materialet används.

## Quiz/reflektionsfrågor

1. Vilka mallar behövs först i ett otydligt uppdrag?
2. När är en mall mer till skada än nytta?
3. Vilken checklista skulle hjälpa mest i din organisation?
4. Hur kan mallarna anpassas utan att tappa jämförbarhet?
5. Vilka delar bör vara obligatoriska innan ett börläge beslutas?

## Nästa steg

Boken är nu komplett som första utkast. Nästa arbete är att granska progression, terminologi, exempel, diagram och exportkvalitet. Därefter kan projektet förberedas för EPUB, PDF eller intern remiss.
