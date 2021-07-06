#Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(k):
  array=[4,5,6,0,1,2,3]
  #cuantas veces cabe ese día en semanas
  #k-núm de semana * 7
  week_position= k-(k//7)*7-1

  return (array[week_position])



#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(1))