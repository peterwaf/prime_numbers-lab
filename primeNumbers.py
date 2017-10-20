def primeNumbers(number):
    the_list = []
    
    for i in range(2, number+1):
      prime = True
    
      for x in range(2,i):
        if i % x == 0:
          prime = False
        
      if prime == True:
            
        the_list.append(i)
        
    return the_list
    
print(primeNumbers(20))