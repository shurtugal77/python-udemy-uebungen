def to_camel_case(text):
    
    # storage for the indices of all occurrences 
    indices = []
    # counter variable. Starts with 0 to look for the first occurence at the beginning of the string
    i = 0
    currentElement = 0

    # Check for empty string
    if text == "":
        print("An empty string was provided - but will not be returned")
    else:
        # Look for all occurences of "_"
        while i < len(text):
            
            # Look for the underscore in the current loop
            currentElement = text.find("_", i)
            
            # Break if no more element is found
            if currentElement == -1:
                break
            # Break if the list is empty
            elif indices == True and str(currentElement) == str(indices[i-1]):
                print("Works")
            else:
                indices.append(currentElement)
                i += 1
                

    return indices


# Call the function
print(to_camel_case("the_stealth_warrior"))