# initialized the recursive function

# Recursive function to generate the sequence



def recursive_sequence(n):
    
    if n == 1:
        return 1
    else:
        return 2 * recursive_sequence(n - 1) + 1

# Start getting user inputs




while True:
    try:
        num = int(input("Enter number: "))
        if num == -1:
            print("Output: Finished")

            
            break
        
        elif num < 1:
            print("Please enter a valid input greater than 0.")
        else:
            print("Output:", recursive_sequence(num))
    except ValueError:
        print("Enter a valid integer, please.")
