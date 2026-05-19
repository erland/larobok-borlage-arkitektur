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
