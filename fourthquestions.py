

# making Recursive functions 
def rec_s(n):

    if n == 1:
        
        return 1
    
    else:
        return rec_s(n - 1) + n




# Starting the implementation
while True:

    
    try:
        s = int(input("Enter number: "))

        if s == -1:
            print("Output: Finished")
            break
        elif s < 1:
            print("Please enter a number greater than 0")
        else:
            print("Output:", rec_s(s))

    except ValueError:
        print("Enter a valid number")
