#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):
    solved_num= int((num*100//10))
    str_num= str(solved_num)
    return int(str_num[-1])



#Invoke the function with a positive real number. ex. 34.33
print(first_digit(6.24))