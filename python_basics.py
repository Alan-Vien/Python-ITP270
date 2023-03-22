#!/bin/python3

name = input("Enter your first and last name: ")

age = int(input("Enter your current age: "))

degree_program = input("Enter your current degree program: ")


remaining_age = (age * 3) // 2


print("Greetings! My name is " + name + ". My current remaining age is " + str(remaining_age) + ", and my current degree program is " + degree_program + "!")
