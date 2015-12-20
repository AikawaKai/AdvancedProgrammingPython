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


def table(pureNumber):
    for t in temp:
        print("{:<13}".format(t), end="")
    print("\n")
    for x in othersToCelsius:
        for y in celsiusToOthers:
            print("{:<13.2f}".format(y(x(pureNumber))), end="")
        print("\n")


if __name__ == '__main__':
    table(10)
