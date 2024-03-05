# Reading the Input Number from User and convert into Interger datatype.
rows = int(input())

# Given the range values from 1 to input number value. (Including the input number)
for i in range(1, rows+1):
    
    # Calculate the Left Side Spaces of the pyramid pattern.
    left_side_spaces = (rows-i) * " "
    
    # Calculate the Number of Stars to print on each line of the pattern.
    number_of_stars = "* " * i 
    
    # By combining the Left Side Spaces and Number of Stars we get the required pattern.                         
    each_line = left_side_spaces + number_of_stars 
    print(each_line)


    



