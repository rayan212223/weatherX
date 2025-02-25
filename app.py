#make a virtual envirnment and install all the module
#import the flask module
from flask import Flask, render_template, request
from datetime import datetime
import requests



app = Flask(__name__)

#make a route and render all the html templates in this route




@app.route("/explore")
def explore():
    return render_template("explore.html")


@app.route("/thanks")
def thanks():
    name = request.args.get('name', 'Guest')  # Get name from URL
    return render_template("thanks.html", name=name)




@app.route('/', methods=['GET', 'POST'])
def index():


#SWITZERLAND
    s = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Switzerland&appid=622de72066ed3699ef9b4a4d10145a3c')


    sjson_object = s.json()

    Shumidity = int(sjson_object['main']['humidity'])
    Spressure = int(sjson_object['main']['pressure'])
    Swind = int(sjson_object['wind']['speed'])
    Stemperature = int(sjson_object['main']['temp']-273.15)


#MANALI

    m = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Manali&appid=622de72066ed3699ef9b4a4d10145a3c')

    mjson_object = m.json()

    Mhumidity = int(mjson_object['main']['humidity'])
    Mpressure = int(mjson_object['main']['pressure'])
    Mwind = int(mjson_object['wind']['speed'])
    Mtemperature = int(mjson_object['main']['temp']-273.15)



# LONDON
    l = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London&appid=622de72066ed3699ef9b4a4d10145a3c')

    ljson_object = l.json()

    Lhumidity = int(ljson_object['main']['humidity'])
    Lpressure = int(ljson_object['main']['pressure'])
    Lwind = int(ljson_object['wind']['speed'])
    Ltemperature = int(ljson_object['main']['temp']-273.15)






    if (request.method == 'POST'):

        try:
            city_name = request.form.get('city')

            #take a variable to show the json data
            # r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=cbf1b9f6f3127d65b15aa57c0cd3d28a')
            r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=622de72066ed3699ef9b4a4d10145a3c')

            #read the json object
            json_object = r.json()

            #take some attributes like temperature,humidity,pressure of this
            temperature = int(json_object['main']['temp']-273.15) #this temparetuure in kelvin
            humidity = int(json_object['main']['humidity'])
            pressure = int(json_object['main']['pressure'])
            wind = int(json_object['wind']['speed'])
            wind_degree = int(json_object['wind']['deg'])
            lat = int(json_object['coord']['lat'])
            lon = int(json_object['coord']['lon'])
            mintemperature = int(json_object['main']['temp_min']-273.15)
            maxtemperature = int(json_object['main']['temp_max']-273.15)
            feelslike = int(json_object['main']['feels_like']-273.15)
            visibility = int(json_object['visibility'])
            last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # current date and time
            description = json_object['weather'][0]['description']
            condition_icon = json_object['weather'][0]['icon']
            feelslike = int(json_object['main']['feels_like']-273.15)
            clouds = int(json_object['clouds']['all'])







            #atlast just pass the variables

            return render_template('home.html',condition_icon=condition_icon,clouds=clouds,description=description,wind_degree=wind_degree,
            last_updated=last_updated,visibility=visibility,maxtemperature=maxtemperature,feelslike=feelslike,mintemperature=mintemperature,
            temperature=temperature,pressure=pressure,humidity=humidity,city_name=city_name,wind=wind,lat=lat,lon=lon,
            Shumidity=Shumidity,Spressure=Spressure,Swind=Swind,Stemperature=Stemperature,
            Mhumidity=Mhumidity,Mpressure=Mpressure,Mwind=Mwind,Mtemperature=Mtemperature,
            Lhumidity=Lhumidity,Lpressure=Lpressure,Lwind=Lwind,Ltemperature=Ltemperature


            )

        except KeyError:  # If an invalid location is entered, return an error message
            city_name = 'Jorhat'

            #take a variable to show the json data
            r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=622de72066ed3699ef9b4a4d10145a3c')

            #read the json object
            json_object = r.json()

            #take some attributes like temperature,humidity,pressure of this
            temperature = int(json_object['main']['temp']-273.15) #this temparetuure in kelvin
            humidity = int(json_object['main']['humidity'])
            pressure = int(json_object['main']['pressure'])
            wind = int(json_object['wind']['speed'])
            wind_degree = int(json_object['wind']['deg'])
            lat = int(json_object['coord']['lat'])
            lon = int(json_object['coord']['lon'])
            mintemperature = int(json_object['main']['temp_min']-273.15)
            maxtemperature = int(json_object['main']['temp_max']-273.15)
            feelslike = int(json_object['main']['feels_like']-273.15)
            visibility = int(json_object['visibility'])
            last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # current date and time
            description = json_object['weather'][0]['description']
            condition_icon = json_object['weather'][0]['icon']
            feelslike = int(json_object['main']['feels_like']-273.15)
            clouds = int(json_object['clouds']['all'])




            #atlast just pass the variables

            return render_template('home.html',condition_icon=condition_icon,clouds=clouds,description=description,wind_degree=wind_degree,
            last_updated=last_updated,visibility=visibility,maxtemperature=maxtemperature,feelslike=feelslike,mintemperature=mintemperature,
            temperature=temperature,pressure=pressure,humidity=humidity,city_name=city_name,wind=wind,lat=lat,lon=lon,
             Shumidity=Shumidity,Spressure=Spressure,Swind=Swind,Stemperature=Stemperature,
            Mhumidity=Mhumidity,Mpressure=Mpressure,Mwind=Mwind,Mtemperature=Mtemperature,
            Lhumidity=Lhumidity,Lpressure=Lpressure,Lwind=Lwind,Ltemperature=Ltemperature)

    else:
            city_name = 'Jorhat'

            #take a variable to show the json data
            r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=622de72066ed3699ef9b4a4d10145a3c')

            #read the json object
            json_object = r.json()

            #take some attributes like temperature,humidity,pressure of this
            temperature = int(json_object['main']['temp']-273.15) #this temparetuure in kelvin
            humidity = int(json_object['main']['humidity'])
            pressure = int(json_object['main']['pressure'])
            wind = int(json_object['wind']['speed'])
            wind_degree = int(json_object['wind']['deg'])
            lat = int(json_object['coord']['lat'])
            lon = int(json_object['coord']['lon'])
            mintemperature = int(json_object['main']['temp_min']-273.15)
            maxtemperature = int(json_object['main']['temp_max']-273.15)
            feelslike = int(json_object['main']['feels_like']-273.15)
            visibility = int(json_object['visibility'])
            last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # current date and time
            description = json_object['weather'][0]['description']
            condition_icon = json_object['weather'][0]['icon']
            feelslike = int(json_object['main']['feels_like']-273.15)
            clouds = int(json_object['clouds']['all'])


            #atlast just pass the variables

            return render_template('home.html',condition_icon=condition_icon,clouds=clouds,description=description,wind_degree=wind_degree,
            last_updated=last_updated,visibility=visibility,maxtemperature=maxtemperature,feelslike=feelslike,mintemperature=mintemperature,
            temperature=temperature,pressure=pressure,humidity=humidity,city_name=city_name,wind=wind,lat=lat,lon=lon,
             Shumidity=Shumidity,Spressure=Spressure,Swind=Swind,Stemperature=Stemperature,
            Mhumidity=Mhumidity,Mpressure=Mpressure,Mwind=Mwind,Mtemperature=Mtemperature,
            Lhumidity=Lhumidity,Lpressure=Lpressure,Lwind=Lwind,Ltemperature=Ltemperature)


if __name__ == '__main__':
    app.run(debug=True)