#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
     print (counter)
     counter -= 1
    print ("Happy New Year!")

    # code goes here!
def square_integers(int_list):
     return [x ** 2 for x in int_list]

    
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
      

    # code goes here!
    