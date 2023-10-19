Number = int(input("Enter a number: "))  # Ask the user to enter a number

count = 10  # Start the count from 10
while count >= 1:  
    product = Number * count  
    print(Number, '*', count, '=', product)  
    count = count - 1  
