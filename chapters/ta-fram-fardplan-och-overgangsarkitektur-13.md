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
