#Complete the function to return how many hrs and min are displayed on the 24th digital clock.
def digital_clock(n):
    #cantidad de horas= n//60
    #cantidad de minutos (n//60)*60-n

    return (n//60,(n-((n//60)*(60))))

#Invoke the function with any interger (seconds after midnight)
print(digital_clock(150))
