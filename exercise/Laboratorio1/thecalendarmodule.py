from calendar import isleap
from calendar import weekday

dayoftheweek = {0: "monday", 1: "tuesday", 2: "wednesday", 3: "thursday",
                4: "friday", 5: "saturday", 6: "sunday"}

if __name__ == '__main__':
    # anni bisestili
    print(isleap(2000))
    print(len(list(filter(isleap, [x for x in range(2000, 2051)]))))
    print(len([x for x in range(2000, 2051) if isleap(x)]))
    # which day of the week July 20 2016 will be
    print(dayoftheweek[weekday(2016, 7, 29)])
