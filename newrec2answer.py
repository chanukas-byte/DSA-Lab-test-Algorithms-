
# creating  recursive relationship


def res(n):

    if(n==1):


        return 2

    else:

        return  res(n-1)/2



    # implement the functions using getting user inputs as well

while True:
    try:
        x = int(input("Please enter the input: "))
        
        if x == -1:
            print("Output: Finished")
            break
        elif x < 1:
            print("Please enter a valid input greater than 0.")
        else:
            print("Output:", res(x))
    
    except ValueError:
        print("Please input a valid integer.")





    
