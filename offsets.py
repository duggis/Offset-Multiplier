# This is a quick calculator for electrical offset bend calculations
import math
angle = int(input("Enter the number of degrees of bend, between 1-89 "))
if 89 < angle or angle < 1:
    print("That is not a valid whole number bend angle.")
rad = math.radians(angle) # This line will convert the user input to radians for future use
o_m = math.sin(rad)
o_mf = 1 / o_m  # This line performs the cosecant conversion of the new radian angle
print("The offset multiplier is: ", o_mf) 
