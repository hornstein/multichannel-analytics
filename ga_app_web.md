# Google Analytics App + Web

Under sommaren 2019 annonserade Google en ny version av Google Analytics som kallas Google Analytics App + Web, med avsikten att få ett gemensamt sätt att samla in och hantera data från både mobila appar och webben: 

https://blog.google/products/marketingplatform/analytics/new-way-unify-app-and-website-measurement-google-analytics/

Denna finns nu tillgänglig i en Beta-version och innehåller en hel del som är intressant, särskilt för de som vill samordna analysen av trafik från en mobil app och en webbsida, men även för de som enbart har en webbsida. Google Analytics App + Web grundar sig på Firebase så vi kommer att känna igen det mesta av gränssnittet från Firebase analytics, och kan nu dra nytta av den enklare hanteringen av händelser/events, samt möjligheten att exportera rådata till BigQuery. Detta var något som tidigare enbart var möjligt från Google Analytics för de med 360-konto. Samtidigt saknas en del saker i Google Analytics App + Web som finns i den vanliga versionen av Google Analytics. T.ex. så saknas det ett reporting API, så precis som för Firebase kan vi inte direkt läsa över data i Data Studio eller Google Sheets, utan måste gå omvägen till BigQuery. Även i analysdelen saknas en del rapporter från Universal Analytics som E-commerce och site search. Den allmänna rekommendationen i nuläget är därför att inte direkt gå över till Google Analytics App +  Web, utan istället köra båda parallellt. Använder man Tag Manager är det som tur var väldigt enkelt att skicka sin Web-data till två (eller fler) olika analysverktyg. Nedan går vi igenom hur man sätter upp Google Analytics App + Web.

## Skapa projekt

Det första man skall göra är att skapa upp ett nytt projekt i Firebase:

![firebase app + web](images/firebase.png)

Här skapar vi upp ett projekt som heter Multichannel:

![firebase app + web](images/firebase_multi2.png)

Vi får då möjligheten att koppla detta till Google Analytics, vilket vi väljer att göra:

![firebase app + web](images/firebase_multi3.png)

I nästa steg får vi välja vilket Google Analytics konto vi vill använda:

![firebase app + web](images/firebase_multi4.png)

I nästa steg skall vi skapa upp en app. Det bästa verkar vara att välja att antingen en iOS app eller en Android app även om vi inte har en sådan. Detta för att loggningen av rådata till BigQuery skall fungera. 

![firebase app + web](images/firebase_multi5.png)

Vi behöver sedan klicka förbi alla stegen tills vi kommer till att verifiera vår app. Eftersom vi inte har någon iOS-app väljer vi "Skip this step":

![firebase app + web](images/firebase_multi6.png)

Vi kan nu gå in i Google Analytics och hittar den nya propertyn som skapats upp för Google Analytics App + Web. Notera att det inte finns några vyer för den här propertyn så vi kan inte filtrera bort trafik direkt från vyn utan vill vi filtrera bort trafik får detta göras direkt från rapporterna.

Vi vill nu få propertyn att samla data från både vår app och vår webbsida. Detta konfigureras under Data Streams. Här kan vi lägga till en ny stream för Web:

![ga app + web](images/gav2.png)

En kul feature är att vi kan automatiskt kan logga events som Scroll och utgående länkar, vilket tidigare krävde manuell taggning från Tag Manager. 

![ga app + web](images/gav22.png)

Det enda vi behöver göra för att få igång datainsamligen är att lägga in taggnings-scriptet på hemsidan. Vi kommer att göra detta från Tag Manager, men för att inte missa några events i rådatan till BigQuery går vi först tillbaka till Firebase och slår på integrationen till BigQuery. Detta görs under settings - integrations, genom att välja BigQuery och klicka på link: 

![firebase app + web](images/firebase_multi7.png)

Precis som för vanliga Firebase behöver vi dock uppgradera vår faktureringsplan till Blaze för att kunna exporta events:

![firebase app + web](images/firebase_multi8.png)


