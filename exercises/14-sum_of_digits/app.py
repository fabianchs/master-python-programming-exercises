#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  str_num= str(num)
  return (int(str_num[0])+int(str_num[1])+int(str_num[2]))


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))