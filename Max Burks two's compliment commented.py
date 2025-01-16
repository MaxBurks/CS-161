#Max Burks Jan 15th 2025
#This program takes a decimal int and converts it into two's complement
#first two lines are declaring variables. dec_num is user input from 127 to -128. no checks are used for simplicity
#twos_comp is the string that will be added onto when converting into two's complement
dec_num = int(input("please enter a decimal integer less than 128 and greater than or equal to -128: "))
twos_comp = ''

#the logic begins! making sure the number is within the requested peramiters and will exit if invalid.
#this is the only data validation used
if dec_num > 127 or dec_num < -128:
    exit('ERROR, INVALID NUMBER')

#this for loop iterates over num_pow from 7 to 0 incrementing by -1.
#this helps minimize the amount of code needed
for num_pow in range(7,-1,-1):
    #these if statements check what size the number is
    #if it is greater than the current placement Ex. dec_num > 2**num_pow-1 or 63, then it will subtract 64
    #as well as adding a 1 to the twos_comp variable
    #if it is smaller than 2**num_pow-1 then it will add 0 to the variable
    if dec_num > (2 ** num_pow) -1:
        twos_comp += '1'
        dec_num -= 2**num_pow
    #this is the only unique check which didn't need to be inside of the loop but made everything more simple
    #if the dec_num is negative it will fall under this check
    #the program will add 1 to the leading bit in the twos_comp variable, and add 128 or (2**num_pow) to dec_num
    #from here the program works as described starting on line 16
    elif dec_num < 0:
        twos_comp = '1'
        dec_num = (2**num_pow+dec_num)
    else:
        twos_comp += '0'
#printing the result
print(twos_comp)
