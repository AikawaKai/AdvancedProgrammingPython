import sys

temperature = [ "Fahren.","Kelvin", \
               "Rankine", "Delisle", "Newton", \
               "Reamur","Romer","Celsius"]


def CelsiusToOthers(celsius, num):
    return {
        0 : celsius * (9/5) + 32.00,     #fahrenheit
        1 : celsius + 273.15,            #kelvin
        2 :(celsius + 273.15)*(9/5),     #rankine
        3 : (100.00 - celsius)*(3/2),    #delisle
        4 : celsius * (33/100),          #newton
        5 : celsius * (4/5),             #reamur
        6 : celsius * (21/40) + 7.5,     #romer
        7 : celsius
    }[num]


##############################################

def OthersToCelsius(other, num):
    return {
        0 : (other - 32.00) * (5/9),     #fahrenheit
        1 : other - 273.15,              #kelvin
        2 : (other - 491.67) * (5/9),    #rankine
        3 : 100 - (other * (2/3)),       #delisle
        4 : other * (100/33),            #newton
        5 : other * (5/4),               #reamur
        6 : (other - 7.5) * (40/21),     #romer
        7 : other
    }[num]

def table(num):
    print('          {0[0]:>10}{0[1]:>10}{0[2]:>10}{0[3]:>10}{0[4]:>10}{0[5]:>10}{0[6]:>10}{0[7]:>10}\n'.format(temperature))
    for i in range (0, 8):
        print ('{0:>10}'.format(temperature[i]), end="")
        for j in range(0, 8):
            if i==j:
                print ('{0:>10.2f}'.format(num),end="")
            else:
                print ('{0:>10.2f}'.format(CelsiusToOthers(OthersToCelsius(num,i),j)),end="")
            if j==7:
                print()

def toAll(value, num):
    return ([CelsiusToOthers(OthersToCelsius(value,i),num) for i in range(0, 8)])


if __name__ == '__main__':
    table(-40)

    print("\n\n{0[0]:>10.2f}{1[0]:>10}\n"\
          "{0[1]:>10.2f}{1[1]:>10}\n"\
          "{0[2]:>10.2f}{1[2]:>10}\n"\
          "{0[3]:>10.2f}{1[3]:>10}\n"\
          "{0[4]:>10.2f}{1[4]:>10}\n"\
          "{0[5]:>10.2f}{1[5]:>10}\n"\
          "{0[6]:>10.2f}{1[6]:>10}\n"\
          "{0[7]:>10.2f}{1[7]:>10}\n".format(toAll(-40, 4), temperature))
