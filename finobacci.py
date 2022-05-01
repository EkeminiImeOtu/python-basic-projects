def fibonacci(n):

    #The base cases of 0 and 1
    if n <= 1:
        return n

    # showing other conditions for fibonacci numbers
    first_back = fibonacci(n-1)
    second_back = fibonacci(n-2)

    #The results

    return first_back + second_back


#Calling the program into the main program

n = int(input("Enter n: "))
result = fibonacci(n)
print("Fib(n) =",result)
