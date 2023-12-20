# Weather And Forecast Checker

Hi! This code can check the Weather and Forecast of any city, in a very simplistic way. 



# What libs do I need?
>Apart from main ones, none


## Main code has 3 functions

```
def  fullPrint(*): # to print every detail from the API

def  printDescription(*): # to print only the weather description

def  printTemperature(*): # to print only the temperature
```

### Hard coded - where you need to inform the city and ==YOUR== API
So just replace these *API* key and *city* _(by input)_.
```
API_Key = '************'

city = input("Enter the city you want to check the Waeather and Forecast: ")
```


> **Tip:** you will need to access the Open Weather Website to login and request an API key, which will be provided under 10m.


## Testing ! 👨‍💻
```
def  fullPrint(*): # to print every detail from the API

def  printDescription(*): # to print only the weather description

def  printTemperature(*): # to print only the temperature
```
**Returns**: 
![WeatherResult](https://i.imgur.com/iQT5Q7p.png)
-------------

Here I searched for "Rio de Janeiro City" and used the language as **"pt_br"**, so the API's response is in **Portuguese** for me, but I also can select **"en"** to return the **English** response from the API call.
