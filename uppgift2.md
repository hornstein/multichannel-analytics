# Uppgift 2 – Produktanalys

I den här laborationen skall ni kombinera data från flera källor och analysera en specifik produkt och dess prestation.

Vi kommer att använda oss av data från Kaggle tävlingen Corporación Favorita Grocery Sales Forecasting. Favorita är en livsmedelskedja i Ecuador med hundratals affärer och över 200000 olika produkter. Kaggle-tävlingen går ut på att prognostisera framtida försäljning av respektive produkt för varje affär. 

Då prognostisering inte ingår i den här kursen kommer målet för laborationen enbart vara att göra en EDA (Exploratory Data Analysis) där ni utforskar försäljningsresultatet dels sammanlagt för samtliga produkter dels för en valfri produkt. 

Utforska hur de olika parametrarna i datakällorna som t.ex. helgdagar, oljepris, och kampanjer påverkat försäljningen. Utforska även  inverkan från säsongsbaserade parametrar som t.ex. veckodag, månad, år, och lönedagar. 

Ni behöver endast undersöka hur parametrarna påverkar den totala försäljningen från samtliga butiker och inte för varje enskild butik.

Data och information om denna finns på https://www.kaggle.com/c/favorita-grocery-sales-forecasting. Jag har också lagt upp datakällorna i BigQuery för enklare åtkomst, samt i Google Sheets:

- Total försäljning per datum: https://docs.google.com/spreadsheets/d/1ad6oHKKvOlCiipw5P5ZCuw01vIbKxRWpESJYL3Vzdjk/edit?usp=sharing
- Total försäljning av artikel 323013 per datum: https://docs.google.com/spreadsheets/d/18X5-NuaVNDZYWDoU4in91rSFW8HL0YMI5zM4K5WvZro/edit?usp=sharing
- Holiday events: https://docs.google.com/spreadsheets/d/1EL4iuP-bre1G0LiaIxCJT7eWRwfHFf8UUMCO1uQj42A/edit?usp=sharing
- Items: https://docs.google.com/spreadsheets/d/1Qj0FhPY_72na88t7BE3v2Cvo5zM7QalJ91pvSPI-EHc/edit?usp=sharing
- Oil: https://docs.google.com/spreadsheets/d/1JBHJRTpqI6xdpjeAw7hIgkwUPYWXrNiPAiBMiuaLePw/edit?usp=sharing
- Stores: https://docs.google.com/spreadsheets/d/1-H5NJ85hoCdUJpL58n4zgYY4C8cPASUCunSbvEf43wY/edit?usp=sharing


Uppgiften är alltså att visualisera hur de olika parametrarna påverkar försäljningen och att ta fram insikter om hur, och i vilken utsträckning, de olika parametrarna påverkar försäljningen. 

## Inlämning:

Inlämningen skall göras i form av en rapport på max 5 sidor. Bifoga också en länk till Data Studio eller Jupyter notebook där det framgår vilken underliggande data som använts för de olika visualiseringarna.

Sista inlämningsdag är söndag 1 december.
