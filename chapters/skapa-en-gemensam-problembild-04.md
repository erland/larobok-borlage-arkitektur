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
