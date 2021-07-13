print("Welcome to the Multiplication/Exponential Table Program")

#Gather users inputs
name = input("\nHello, what is your name: ").title().strip()
num = float(input("What number would you like to form a table on?: "))
message = name + ", Math is fun!"

#Multiplication table
print("\nMultiplication Table For " + str(num))
print("\n\t 1.0 * " + str(num) + " = " + str(round(1*num,2)))
print("\t 2.0 * " + str(num) + " = " + str(round(2*num,2)))
print("\t 3.0 * " + str(num) + " = " + str(round(3*num,2)))
print("\t 4.0 * " + str(num) + " = " + str(round(4*num,2)))
print("\t 5.0 * " + str(num) + " = " + str(round(5*num,2)))
print("\t 6.0 * " + str(num) + " = " + str(round(6*num,2)))
print("\t 7.0 * " + str(num) + " = " + str(round(7*num,2)))
print("\t 8.0 * " + str(num) + " = " + str(round(8*num,2)))
print("\t 9.0 * " + str(num) + " = " + str(round(9*num,2)))



#Exponent table
print("\nExponent Table For " + str(num))
print("\n\t 1.0 ** " + str(num) + " = " + str(round(1**num,2)))
print("\t 2.0 ** " + str(num) + " = " + str(round(2**num,2)))
print("\t 3.0 ** " + str(num) + " = " + str(round(3**num,2)))
print("\t 4.0 ** " + str(num) + " = " + str(round(4**num,2)))
print("\t 5.0 ** " + str(num) + " = " + str(round(5**num,2)))
print("\t 6.0 ** " + str(num) + " = " + str(round(6**num,2)))
print("\t 7.0 ** " + str(num) + " = " + str(round(7**num,2)))
print("\t 8.0 ** " + str(num) + " = " + str(round(8**num,2)))
print("\t 9.0 ** " + str(num) + " = " + str(round(9**num,2)))


#math is fun part of the code
print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.upper())

