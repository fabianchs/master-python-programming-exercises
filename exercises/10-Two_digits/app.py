#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
    str_digit= str(digit)
    return (int(str_digit[0]),int(str_digit[1]))
   


#Invoke the function with any interger as its argument.
print(two_digits(54))
