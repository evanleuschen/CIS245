import requests
from pprint import pprint

def starterGrabber():
#getting the latitutde and longitude for the user so I can put it into the forecasting URL    
    
    userChoice = input("Is your location in the USA? Yes or No? ")
    
    if userChoice == "Yes":
        americanLocale = input("Enter the city and state abbreviation in format- City,US-AB ")
        americanURL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2a5b16e13753c2c4f6c4530da72b9a48&units=imperial'.format(americanLocale)
        
        #starting to communicate with API
        
        data = requests.get(americanURL)
        locGrabUSA = data.json()
        
        #grabbing coordinates from the current weather to be used in the forecast later on
        
        lat = locGrabUSA['coord']['lat']
        lon = locGrabUSA['coord']['lon']

        #retrieving the forecast
        callURL = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly&appid=2a5b16e13753c2c4f6c4530da72b9a48&units=imperial'.format(lat, lon)
        
        callData = requests.get(callURL)
        finalForecast = callData.json()

        currentTemp = finalForecast['current']['temp']
        currentFeels = finalForecast['current']['feels_like']
        day0LowTemp = finalForecast['daily'][0]['temp']['min']
        day0HighTemp = finalForecast['daily'][0]['temp']['max']
        day0WindSpeed = finalForecast['daily'][0]['wind_speed']
        day0Description = finalForecast['daily'][0]['weather'][0]['description']

        day1LowTemp = finalForecast['daily'][1]['temp']['min']
        day1HighTemp = finalForecast['daily'][1]['temp']['max']
        day1WindSpeed = finalForecast['daily'][1]['wind_speed']
        day1Description = finalForecast['daily'][1]['weather'][0]['description']

        day2LowTemp = finalForecast['daily'][2]['temp']['min']
        day2HighTemp = finalForecast['daily'][2]['temp']['max']
        day2WindSpeed = finalForecast['daily'][2]['wind_speed']
        day2Description = finalForecast['daily'][2]['weather'][0]['description']

#displaying the forecast
        print("The current temperature is ", currentTemp)
        print("It feels like ", currentFeels)
        print("Today is ", day0Description)
        print("The low is: ", day0LowTemp)
        print("The high is: ", day0HighTemp)
        print("The average wind speed is: ", day0WindSpeed)

        print("The next day will be ", day1Description)
        print("The low will be: ", day1LowTemp)
        print("The high will be: ", day1HighTemp)
        print("The average wind speed will be: ", day1WindSpeed)

        print("The following day will be ", day2Description)
        print("The low will be: ", day2LowTemp)
        print("The high will be: ", day2HighTemp)
        print("The average wind speed will be: ", day2WindSpeed)

    elif userChoice == "No":
        
        foreignLocale = input("Enter the city and ISO country abbreviation in format, City,CTY ")
        foreignURL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2a5b16e13753c2c4f6c4530da72b9a48&units=imperial'.format(foreignLocale)
        
        #starting to communicate with API
        
        data = requests.get(foreignURL)
        locGrabFor = data.json()
        
        #grabbing coordinates from the current weather to be used in the forecast later on
        
        lat = locGrabFor['coord']['lat']
        lon = locGrabFor['coord']['lon']    
        
        #retrieving the forecast
        callURL = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly&appid=2a5b16e13753c2c4f6c4530da72b9a48&units=imperial'.format(lat, lon)
        
        callData = requests.get(callURL)
        finalForecast = callData.json()

        currentTemp = finalForecast['current']['temp']
        currentFeels = finalForecast['current']['feels_like']
        day0LowTemp = finalForecast['daily'][0]['temp']['min']
        day0HighTemp = finalForecast['daily'][0]['temp']['max']
        day0WindSpeed = finalForecast['daily'][0]['wind_speed']
        day0Description = finalForecast['daily'][0]['weather'][0]['description']

        day1LowTemp = finalForecast['daily'][1]['temp']['min']
        day1HighTemp = finalForecast['daily'][1]['temp']['max']
        day1WindSpeed = finalForecast['daily'][1]['wind_speed']
        day1Description = finalForecast['daily'][1]['weather'][0]['description']

        day2LowTemp = finalForecast['daily'][2]['temp']['min']
        day2HighTemp = finalForecast['daily'][2]['temp']['max']
        day2WindSpeed = finalForecast['daily'][2]['wind_speed']
        day2Description = finalForecast['daily'][2]['weather'][0]['description']

#displaying the forecast
        print("The current temperature is ", currentTemp)
        print("It feels like ", currentFeels)
        print("Today is ", day0Description)
        print("The low is: ", day0LowTemp)
        print("The high is: ", day0HighTemp)
        print("The average wind speed is: ", day0WindSpeed)

        print("The next day will be ", day1Description)
        print("The low will be: ", day1LowTemp)
        print("The high will be: ", day1HighTemp)
        print("The average wind speed will be: ", day1WindSpeed)

        print("The following day will be ", day2Description)
        print("The low will be: ", day2LowTemp)
        print("The high will be: ", day2HighTemp)
        print("The average wind speed will be: ", day2WindSpeed)
    
    elif userChoice != "yes" or "no":
        
        print("Try again")
        starterGrabber()

starterGrabber()