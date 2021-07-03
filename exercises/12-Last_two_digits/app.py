#Complete the function to print the last two digits of an interger greater than 9. 
def last_two_digits(num):
    str_num= str(num)
    return (int(str_num[-2])*10+int(str_num[-1]))

#Invoke the function with any interger greater than 9.
print(last_two_digits(1234))
