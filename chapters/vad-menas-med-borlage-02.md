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
