#!/bin/python3

print("Here are our other 6 plants in our solar system:\n")

print(" 1. Venus  2. Mars  3. Jupiter")
print(" 4. Saturn 5. Uranus 6. Neptune\n")
 
weight = 150
planet = 6 


if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19

print("Your weight on this certain planet is:", weight)
