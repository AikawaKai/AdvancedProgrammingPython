import functools
import operator

alkaline_earth_metals = [('beryllium', 4), ('magnesium' ,12), ('calcium', 20), ('strontium', 38), ('barium', 56), ('radium', 88)]
noble_gases = {'helium':2, 'neon':10, 'argon':18, 'krypton':36, 'xenon': 54, 'radon':86,}

if __name__ == '__main__':
    print(max([y for x,y in alkaline_earth_metals]))
    print(sorted(alkaline_earth_metals, key=lambda element: element[1]))
    alkaline_earth_metals_dict = {x:y for x,y in alkaline_earth_metals}
    print (alkaline_earth_metals_dict)
    alkaline_earth_metals_dict.update(noble_gases)
    print(alkaline_earth_metals_dict)
    print(sorted(alkaline_earth_metals_dict.items(), key=operator.itemgetter(1)))
    print(sorted([(x,y) for x,y in alkaline_earth_metals_dict.items()], key =lambda element: element[1]))
