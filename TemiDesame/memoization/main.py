from memoization import *


if __name__ == "__main__":
  print("sum({0},{1})  => {2}".format(9,5,sum(9,5)))
  print("sum({0},{1})  => {2}".format(7,7,sum(7,7)))
  print("sum({0},{1}) => {2}".format(10,4,sum(10,4)))
  print("sum({0},{1}) => {2}".format(1,13,sum(1,13)))
  print("sum({0},{1}) => {2}".format(7,25,sum(7,25)))

  print("fibo({0})   => {1}".format(5,fibo(5)))
  print("fibo({0})   => {1}".format(7,fibo(7)))
  print("fibo({0})  => {1}".format(25,fibo(25)))

  print("fact({0})   => {1}".format(5,fact(5)))
  print("fact({0})   => {1}".format(7,fact(7)))
  print("fact({0})  => {1}".format(10,fact(10)))
