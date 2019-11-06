# CRM data

För laboration 1 finns kunddata tillgängligt via ett CRM-system.

## Läsa data från databas

Från Power-BI kan man ansluta direkt till CRM-systemets databas. Använd user id och password från nedanstående connection string för att ansluta till databasen.

Tyvärr tillåter inte IHM's brandvägg att man ansluter via deras wifi-nätverk, så för att göra detta behöver man koppla upp datorn via mobilen.


```
DataConnectionString: Data Source=bluebottlesurfboards.database.windows.net;Initial Catalog=nopCommerce;Integrated Security=False;Persist Security Info=False;User ID=bluebottle;Password=KingKong123
```

Den kunddata vi är intresserad av ligger utspridd i flera tabeller. Antingen kan man läsa över samtliga dessa till Power-BI och koppla ihop dem där, eller så kan man göra det direkt via följande SQL-sats:

```sql
select a.EntityId CustomerID, a.[value] Gender, b.[value] DateOfBirth, d.ZipPostalCode from [dbo].[GenericAttribute] a
inner join [dbo].[GenericAttribute] b on a.EntityId=b.EntityId
left outer join [dbo].CustomerAddresses c on c.Customer_Id=b.EntityId
left outer join [dbo].[Address] d on d.Id=c.Address_Id
where a.[key] = 'Gender' and b.[Key] = 'DateOfBirth'
```


## Läsa data från BigQuery

Både Power-BI and Data Studio kan läsa data från BigQuery. För att ansluta ni skall kunna ansluta till BigQuery behöver jag tilldela er rättigheter i Googles Cloud Console (https://console.cloud.google.com).

När ni fått rättigheter är det bara att ansluta till BigQuery från Power BI / Data Studio och via respektive verktygs BigQuery-connector och får då tillgång till tabellen customer_data som innehåller samma data som fås via SQL-satsen ovan.


## Läsa data via CSV-fil

Den som är lat kan istället hämta hem filen customerdata.csv från kursens github-sida...
