def celsiusToCelsius(celsius):
    return celsius


def celsiusToFahrenheit(celsius):
    return (celsius * (9/5)) + 32


def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)


def celsiusToKelvin(celsius):
    return celsius + 273.15


def kelvinToCelsius(kelvin):
    return kelvin - 273.15


def celsiusToRankine(celsius):
    return (celsius + 273.15) * (9/5)


def rankineToCelsius(rankine):
    return (rankine - 491.67) * (5/9)


def celsiusToDelisle(celsius):
    return (100 - celsius) * (3/2)


def delisleToCelsius(delisle):
    return 100 - (delisle * (2/3))


def celsiusToNewton(celsius):
    return celsius * (33/100)


def newtonToCelsius(newton):
    return newton * (100/33)


def celsiusToReaumur(celsius):
    return celsius * (4/5)


def reaumurToCelsius(reaumur):
    return reaumur * (5/4)


def celsiusToRomer(celsius):
    return celsius * (21/40) + 7.5


def romerToCelsius(romer):
    return (romer - 7.5) * (40/21)


celsiusToOthers = [celsiusToCelsius, celsiusToFahrenheit, celsiusToKelvin,
                   celsiusToRankine, celsiusToDelisle, celsiusToNewton,
                   celsiusToReaumur, celsiusToRomer]
othersToCelsius = [celsiusToCelsius, fahrenheitToCelsius, kelvinToCelsius,
                   rankineToCelsius, delisleToCelsius, newtonToCelsius,
                   reaumurToCelsius, romerToCelsius]

temp = ["Celsius", "fahrenheit", "kelvin", "Rankine", "Delisle", "Newton",
        "Reaumer", "Romer"]

scale = {"Celsius": 0, "Fahrenheit": 1, "Kelvin": 2, "Rankine": 3,
         "Delisle": 4, "Newton": 5, "Reaumer": 6, "Romer": 7}


def table(pureNumber):
    header = "".join(["{:<13}".format(t) for t in temp]) + "\n"
    body = ""
    partialbody = ""
    for x in othersToCelsius:
        partialbody = "".join(["{:<13.2f}".format(y(x(pureNumber)))
                               for y in celsiusToOthers])
        body = body + partialbody + "\n"
    return header + body


def toAll(temperature, scale_str):
    numScale = scale[scale_str]
    func = othersToCelsius[numScale]
    conversion = [func(y(temperature)) for y in celsiusToOthers]
    tempconversion = [(temp[i], conversion[i])for i in range(len(temp))]
    tempconversion = sorted(tempconversion, key=lambda x: x[1])
    body = "".join(["Type: {0:<10} Temp:{1:>10.2f}\n".format(x[0], x[1])
                    for x in tempconversion])
    return body


if __name__ == '__main__':
    print(table(10))
    print(toAll(10, "Celsius"))
    print(toAll(10, "Fahrenheit"))
    print(toAll(10, "Kelvin"))
    print(toAll(10, "Rankine"))
    print(toAll(10, "Delisle"))
    print(toAll(10, "Newton"))
    print(toAll(10, "Reaumer"))
    print(toAll(10, "Romer"))
