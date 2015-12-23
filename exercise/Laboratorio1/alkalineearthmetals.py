alkaline_earth_metals = [("barium", 56), ("beryllium", 4), ("calcium", 20),
                         ("magnesium", 12), ("radium", 88), ("strontium", 38)]

noble_gases = {"helium": 2, "neon": 10, "argon": 18, "krypton": 36,
               "xenon": 54, "radon": 86}

if __name__ == '__main__':

    print(max([y for (x, y) in alkaline_earth_metals]))
    print(sorted(alkaline_earth_metals, key=(lambda x: x[1])))
    alkaline_earth_metals_dict = {x: y for (x, y) in alkaline_earth_metals}
    print(alkaline_earth_metals_dict)
    merged_list = alkaline_earth_metals_dict.copy()
    merged_list.update(noble_gases)
    print(merged_list)
    print(sorted(merged_list.items(), key=lambda x: x[1], reverse=False))
