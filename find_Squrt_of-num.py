# This is simple program to find the suare root of a number.
import math# importing mats module   
s =""# s is a variable to store the user input value.
while s != "0":# create an ifinite loop,if user input is 0 quit the program
    s = float(input("Enter a number to find Sqrt or enter 0 for exit\n"))
    print ("Square root of ",s,"is =",math.sqrt(s))