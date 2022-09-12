def wind(DogCode):
    """
    Winds dog codes back into the format the game accepts.
    Check the Readme for more detailed information.
    
    Args:
        DogCode (string): user input string containing unwound dog code.
    """
    
    workingCode = list(DogCode) #casts string to list, required for manipulation w/o errors

    for i in range(len(workingCode)): 

        indexToSwap = ord(
            workingCode[(i + 1) % len(workingCode)] #finds the numerical ASCII values for swapping calculation
        )

        workingCode[i], workingCode[(i + indexToSwap) % len(workingCode)] = \
            workingCode[(i + indexToSwap) % len(workingCode)], workingCode[i]
            
        #this takes the value in index i and swaps it with
        #the index minus the value of the next index, 
        #modded with the length of the code to allow for looping 

    workingCode = ''.join(workingCode) #join each character (now single strings) into one string, backwards

    return workingCode

def unwind(DogCode):
    """
    Unwinds dog codes for editing purposes. 
    Check the Readme for more detailed information.

    Args:
        DogCode (string): user input string containing exported dog code.
    """
    
    workingCode = list(DogCode[::-1]) #flips dog code backwards in a list to use winding code backwards (reversing steps)
    #arrays are little bitches who don't like to get strings assigned to them so we have to use a list
    
    for i in range(len(workingCode)):
        indexToSwap = ord(
            workingCode[(i - 1) % len(workingCode)] #finds the numberical values for each ASCII character for swapping calculation
        )
        
        workingCode[i], workingCode[(i - indexToSwap) % len(workingCode)] \
            = workingCode[(i - indexToSwap) % len(workingCode)], workingCode[i]
            
        #this takes the value in index i and swaps it with
        #the index minus the value of the next index, 
        #modded with the length of the code to allow for looping 

    workingCode = ''.join(workingCode[::-1]) #join each single character (now single strings) into a single string, backwards

    return workingCode
