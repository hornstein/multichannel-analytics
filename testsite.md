# Skapa testsajt på github

Om man vill laborera med olika metoder för att tagga en hemsida så kan det vara praktiskt att ha en egen sajt att testa med.

## Skapa en sajt

Här kommer vi att använda oss av färdig template för en onepage-sajt:

http://bootstrapmade.com/demo/Squadfree/

Ladda ner denna och packa upp filerna.


## Hosta webbsajten

För att göra sajten tillgänglig från Internet behöver den hostas.

Ett enkelt och gratis sätt att göra detta är att använda GitHub Pages:

https://pages.github.com/

Skapa ett konto på github och följ instruktionerna oven för att:

- Skapa en repository
- Installera git på datorn
- Använda git för att skicka upp vår sajt till repositoryn


### Skapa en repository

Skapa ett nytt repository och ge det namnet ```username.github.io```, i mitt fall ```hornstein.github.io```:

![git repository](images/github_repository.png)

### Installera git på datorn

Nu behöver vi antingen installera git eller Github Desktop (https://desktop.github.com/) för att kunna hämta hem vårt repository till vår lokala dator. På lektionen gick vi igenom hur man använder Github Desktop. Här tänkte jag istället visa hur man installerar git. En fördel med att installera git är att man då kan göra sina commits och pusha koden till repositoryn på Github direkt från Visual Studio Code om man nu använder det för att editera sina filer. 

Kör ni Linux har ni redan git installerat. Kör ni mac är det bara att öppna en terminal och skriva ```git``` så öppnas automatiskt en dialogruta om att installera detta:

![git mac](images/git_mac.png)

Kör ni Windows behöver ni ladda hem och installera git från https://git-scm.com/download/win 

När vi installerat git hämtar vi hem vårt repository från github genom att öppna en terminal och använda git clone:

```
git clone https://github.com/hornstein/hornstein.github.io.git
```

Vi har nu fått ett nytt directory där vi kan lägga vår kod. 

![git clone](images/git_clone.png)

Kopiera koden som laddades hem från http://bootstrapmade.com/demo/Squadfree/ till det nya directoryt.

Lägg till filerna till git, gör en commit, och pusha denna till Github med följande kommandon:

```
git add --all
git commit -m "Initial commit"
git push -u origin master
```


Vår sajt skall nu vara online:

![Squad Free website](images/site.png)


## Lägga till Google Analytics tracking kod

Vi behöver nu skapa en ny property i Google Analytics och hämta hem tracking koden. Använder du Tag Manager behöver enbart skapa upp propertyn och kopiera ditt Google Analytics id och kan hoppa över det här avsnittet och istället kolla hur man lägger till Tag Manager på siten...

```html
<!-- Global site tag (gtag.js) - Google Analytics --> 
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-114519476-
1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-114519476-1');
</script>
```

Denna kod lägger vi in i index.html-filen direkt under <head> taggen. Spara filen och pusha denna till repositoryn i github.

Vi skall nu ha en fungerande tracking i Google Analytics.

Med standard-taggen fångar vi PageView-data, men eftersom vi har en onepage-sajt så aktiveras denna 
bara en gång när användaren kommer in till hemsidan och det genereras inga nya PageViews när 
användarna navigerar på hemsidan, och vi får heller någon data om användarna t.ex. fyller i 
kontaktformuläret eller klickar på e-mail-länken.

Nedan går vi igenom hur man själv kan lägga till tracking-kod för att fånga dessa händelser.


### Lägga till PageView-taggar

Vi börjar med att titta på hur man lägger till egna PageView-hits för fånga när användaren navigerar på 
hemsidan. Dokumentation om detta hittas på:

https://developers.google.com/analytics/devguides/collection/gtagjs/single-page-applications

Den tag vi behöver lägga till är:

```javascript
gtag('config', 'GA_TRACKING_ID', {'page_path': '/new-page.html'});
```

där GA_TRACKING_ID är vår tracking kod, i mitt fall UA-114519476-1. Under page_path anger vi 
pathen till den del av sidan som vi vill tracka. En onepage-sajt är ofta uppdelad i olika sektioner som 
man kan navigera till via menyn. Vill man t.ex. komma till About-sektionen så gör man t.ex. det via 
addressen /index.html#about. Den kompletta taggen för About-sektionen på min sida blir alltså:


```javascript
gtag('config', 'UA-114519476-1', {'page_path': '/index.html#about'});
```

Hur lägger vi in denna på hemsidan? Enklaste sättet är kanske att använda en onclick-funktion och 
koppla denna till att någon klickar i menyn (rad 63 i index.html-filen):

```html
<li>
    <a href="#about" onclick="gtag('config', 'UA­114519476­1', {'page_path': '/index.html#about'});">About</a>
</li>
```

Motsvarande kan naturligtvis göras även för övriga menyalternativ. Problemet med detta sätt är att 
PageView-taggen endast aktiveras om någon faktiskt klickar i menyn. Om användaren istället scrollar 
nedåt på hemsidan till respektive sektion så kommer data inte att skickas till Google Analytics. 

Ett bättre, men lite mer komplicerat, sätt att tagga upp sidan är att fånga scroll-event och skicka data när användaren scrollat ner till en viss sektion. Detta fungerar både om användaren använder menyn 
eller om användaren själv scrollar ner till sektionen. Bootstrap ramverket som vår sida bygger på 
innehåller kod för att känna av när man scrollat till en viss sektion så vi kan utnyttja denna för att lägga till vår PageView-tag. Vi hittar koden i filen bootstrap.js under katalogen js. Lägg till PageView-taggen precis ovanför active.trigger('activate.bs.scrollspy') på rad 1653 i filen:

```javascript
gtag('config', 'UA­114519476­1', {'page_path': '/index.html'+target});
```

Här har vi dessutom utnyttjat att det finns en variabel (target) som innehåller namnet på den aktuella 
sektionen (#intro, #about, #services, ...), så vi behöver bara lägga till en enda rad för att generera 
PageViews för samtliga sektioner.

Vi behöver också ändra i index.html så att denna använder sig av filen bootstrap.js istället för den 
minifierade versionen bootstrap.min.js genom att byta ut raden:

```html
 <script src="js/bootstrap.min.js"></script>
```

mot 

```html
 <script src="js/bootstrap.js"></script>
```

Pusha ändringarna till repon för att få in de nya PageView-taggarna på hemsidan.

### Lägga till Event-taggar

Våra hemsidor är framför allt utformade för att få besökarna intresserade av våra tjänster så att de 
kontaktar oss via e-mail eller via det kontaktformulär som ligger på hemsidan.
För att kunna lägga upp dessa som mål i Google Analytics och mäta t.ex. konverteringsgrad, så behöver
vi lägga in tracking-kod som känner av om någon klickar på mailadressen eller på ”Send message” 
knappen. I det här fallet är det inte frågan om någon PageView, utan det vi vill fånga är en specifik 
händelse (event) på hemsidan. Dokumentation om hur man trackar events finns på:

https://developers.google.com/analytics/devguides/collection/gtagjs/events

Detta görs med följande tracking-kod:

```javascript
gtag('event', <action>, {'event_category': <category>,'event_label': <label>,'value': <value>});
```

I den senaste versionen av Google Analytics tracking-kod (gtag) är det endast action som är 
obligatoriskt att fylla i när man genererar ett event. Action är en textsträng som egentligen kan 
innehålla vilken text som helst, men Google rekommenderar att man i första hand använder de Event 
names som finns i dokumentationen ovan. Där hittar man t.ex. generate_lead som kan vara passande 
som action när personer kontaktar oss. Vi får då följande tag:

```javascript
gtag(’event’, ’generate_lead’);
```

Om vi lägger in denna på både kontaktformuläret och e-mail adressen så kan vi dock inte skilja på vilka
användare som använt vilken metod för att kontakta oss. Vill vi göra detta kan vi välja att använda olika kategorier för dessa:

```javascript
gtag('event', 'generate_lead', {'event_category':'Contact us form'}); 
gtag('event', 'generate_lead', {'event_category':'Contact us email'}); 
```

Precis som våra PageView-taggar kan vi lägga in dessa på hemsidan via onclick-funktionen på 
respektive href-tag:

```html
<button type="submit" class="btn btn­skin pull­right" id="btnContactUs" 
onclick="gtag('event', 'generate_lead', {'event_category':'Contact us 
form'});">Send Message</button>
<a href="mailto:#" onclick="gtag('event', 'send_mail', {'event_category':'Contact 
us email'});">email.name@example.com</a>
```

Ett problem med att använda onclick är att events skickas så snart någon klickar på Send Message 
knappen, oavsett om formuläret är korrekt ifyllt eller inte. Helst skulle vi vilja att vi endast får ett event när meddelandet faktiskt skickas. För att åstadkomma detta behöver vi istället lägga till vår event-tag i det javascript som verifierar att formuläret är korrekt ifyllt. Denna hittar vi under 
contactform/contactform.js. Här kan vi lägga till vår gtag under ”else var str = $(this).serialize();” (rad 81):

```javascript
gtag('event', 'generate_lead', {'event_category':'Contact us form'});
```

För vårt email-event finns det tyvärr inget bra sätt att fånga att användaren verkligen skickar mailet 
utan där får vi helt enkelt nöja oss med att fånga de som klickat på email-länken.


## Lägga till Tag Manager

Ett alternativ till att direkt skicka data till Google Analytics är att använda sig av Tag Manager. I det här avsnittet går vi igenom hur man taggar upp sajten med hjälp av Tag Manager.

Det första vi behöver göra är att skapa upp en container för vår site: 

![tag manager container](images/tag_manager_container.png)

När vi gör detta får vi en tracking code som skall läggas in på hemsidan.

![tag manager tracking code](images/tag_manager_tracking_code.png)

Vi lägger till denna i filen index.html. Detta kan göras med valfri texteditor, t.ex. notepad i Windows, men jag rekommenderar att man installerar Visual Studio Code och editerar filerna i denna då den är gjord specifikt för att editera kod. Du hittar Visual Studio Code på:

https://code.visualstudio.com/

I Visual Studio Code öppnar man upp det directory man vill jobba med, i det här fallet det directory där vi clonat hem vårt repository från Github.

Vi klistrar in första delen av trackingkoden direkt under head-taggen i index.html.

```javascript
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-P37S9DS');</script>
<!-- End Google Tag Manager -->
```

och den andra delen av trackingkoden direkt under body-taggen.

```javascript
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-P37S9DS"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
```

Resultatet bör se ut som nedan:

![visual studio code](images/visual_studio_code.png)

Har du installerat git kan du nu commita dina ändringar och pusha dessa till github direkt från Visual Studio Code. Annars får du gå in i Github Desktop och göra detta därifrån.

![added tag manager](images/added_tag_manager.png)

### Page View tag

Vi har nu satt upp tag manager för vår site och kan börja tagga upp hemsidan från tag manager och skicka data till Google Analytics. Det första vi gör är att skapa en Page View tag:

![ga tag](images/ga_tag.png)

Surfa in på hemsidan och kontrollera att data kommer in i Google Analytics realtime view:

![ga realtime view](images/ga_realtime_view.png)

Ett problem med att bara använda en Page View tag på onepage-sajt är att vi får en bounce rate på 100% och en time on site på 0s även om användaren stannar kvar och läser allt innehåll på sajten (förutsatt att de inte laddar om sidan innan sessionstiden tajmat ut).

![bounce rate 100](images/bounce_rate_100.png)

För att komma runt detta bör vi lägga till events när användaren scrollar ner på sidan eller klickar på någon av menyknapparna som leder till olika sektioner på sidan.