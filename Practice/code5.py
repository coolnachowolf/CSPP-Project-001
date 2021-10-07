cities = [ ["Pittsburgh", "Allegheny", 302407],
           ["Philadelphia", "Philadelphia", 1584981],
           ["Allentown", "Lehigh", 123838],
           ["Erie", "Erie", 97639],
           ["Scranton", "Lackawanna", 77182] ]

def total(a):    
    sum = 0
    for row in range(len(a)): 
        for col in range(len(a[row])): 
            if(col == 2):
                for row in range(len(a)):
                    sum = sum + a[row][2]
                return sum
                
print(total(cities))

'''To display all the elements in the 2D list'''

cities = [ ["Pittsburgh", "Allegheny", 302407],
           ["Philadelphia", "Philadelphia", 1584981],
           ["Allentown", "Lehigh", 123838],
           ["Erie", "Erie", 97639],
           ["Scranton", "Lackawanna", 77182] ]

def total(a):    
    for row in range(0,len(a)): 
        for col in range(0,len(a[row])): 
            print(cities[row][col])
                            
print(total(cities))


'''To display 2D list elements in the form of a box''' 
cities = [ ["Pittsburgh", "Allegheny", 302407],
           ["Philadelphia", "Philadelphia", 1584981],
           ["Allentown", "Lehigh", 123838],
           ["Erie", "Erie", 97639],
           ["Scranton", "Lackawanna", 77182] ]

def total(a):    
    for row in range(0,len(a)): 
        for col in range(0,len(a[row])): 
            print(cities[row][col], end=' ')
        print()
                          
print(total(cities))