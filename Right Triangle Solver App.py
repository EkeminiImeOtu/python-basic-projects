import math

print("\nWelcome to the Right Triangle Solver App")

#Get users inputs
side_A = float(input("\nWhat is the value of side A?: "))
side_B = float(input("\nWhat is the value of side B?: "))

#Calculations using the formula
hypotenuse = math.sqrt(side_A**2 + side_B**2)
hypotenuse = round(hypotenuse,2)

area_of_triangle = 0.5*side_A*side_B
area_of_triangle = round(area_of_triangle,2)

#Summary
print("\nFor a triangle with value of " + str(side_A) + " and " + str(side_B) + " the hypotenuse is " + str(hypotenuse) + ".")
print("For a triangle with value of " + str(side_A) + " and " + str(side_B) + " the area of triangle is " + str(area_of_triangle)+ ".")