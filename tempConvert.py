def celcFahr():
    
    tempF = eval(input("Enter your Fahrenheit Temperature: "))
    tempC = (5.0/9.0)*(tempF-32.0)

    print("Your Temperature in Celcius is ", format(tempC,'.2f'), "deg", sep='' )
    print("")

celcFahr()



def fahrCelc():

    tempC = eval(input("Enter your Celcius Temperature: "))
    tempF = (9.0/5.0)*(tempC)

    print("Your Temperature in Celcius is ", format(tempF,'.2f'), "deg", sep='' )
    print("")

fahrCelc()
