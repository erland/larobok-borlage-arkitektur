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
