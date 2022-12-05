lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:
                print ("The Composite Numbers in the range are: ",number)
                break

                  
        else:
            print ("The Prime Numbers in the range are: ",number)

 
