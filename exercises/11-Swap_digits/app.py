#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
    str_num= str(num)
    return (int(str_num[1])*10+int(str_num[0]))
   
   
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(79))

