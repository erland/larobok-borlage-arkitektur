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
