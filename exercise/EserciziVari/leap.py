import calendar
import functools


if __name__ == '__main__':
    print (sum(list(map(calendar.isleap,[elem for elem in range(2000, 2050+1)]))))
