# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion():    
    miles = 0.0
    ######################
    miles = kilometers * 0.6214
    return miles
    ######################    


#### This piece of the code has been done for you,
#### you only need to worry about the actual temp 
#### conversion logic in the temp_conversion function
if __name__ == '__main__':
    # Get User Input
    print('in main')
    # Call kilometer_conversion
    kilometers = float(input("Enter distance in kilometers: "))
    final = kilometer_conversion()
    print(f"The distance in miles is: {final:.2f}")
    # Display the miles
