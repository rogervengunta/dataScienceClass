
def funcRecursive(numArg): #FINDING THE FACTORIAL (BELOW fact() FUNC)
    """[summary]

    Arguments:
        numArg {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    print("1st line of fund def")
    if(numArg > 0): #base case
        result = numArg + funcRecursive(numArg-1) #recursive case
        print("if block result:", result) #CALL STACK?? WHICH PART GOES INTO CALL STACK?
    else:
        result = 0
        print("else block result:", result)
    return result

print("\n \n Recursion example results:")
funcRecursive(3) # why the heck is this printing the numbers it's printing?!!

"""
def fact(n):
    if(n==0):
        return 1
    
    return n * fact(n-1)
"""
"""result = fact(4)
print(result)"""
