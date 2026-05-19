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
