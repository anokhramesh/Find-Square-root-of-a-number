# This is simple program to find the suare root of a number.
import math# importing mats module   
s =""# s is a variable to store the user input value.
while s != "q":# create an ifinite loop,if user input is q quit the program
    s = float(input("Enter a number to find Sqrt or enter q for quit\n"))
    print ("Square root of ",s,"is =",math.sqrt(s))
