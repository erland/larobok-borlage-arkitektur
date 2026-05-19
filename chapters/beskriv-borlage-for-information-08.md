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
