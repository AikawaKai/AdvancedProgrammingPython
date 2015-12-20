from calendar import isleap

if __name__ == '__main__':
    # anni bisestili
    print(isleap(2000))
    print(len(list(filter(isleap, [x for x in range(2000, 2051)]))))
    print(len([x for x in range(2000, 2051) if isleap(x)]))
