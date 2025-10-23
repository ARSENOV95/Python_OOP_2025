x = "global" 

def outer(): 
    x = "local"  
    
    def inner(): 
        nonlocal x #takes the enclosed value of x "local" and changes it ot  nonlocal 
        x = "nonlocal" 
        print("inner:", x) 
    
    def change_global(): 
        global x #takes the value of x "global" ans sets it ot global changed
        x = "global: changed!" 
        
    print("outer:", x)  #prints the first value of outer x 
    inner()  #inner is
    print("outer:", x) 
    change_global() 
    
print(x)  #first it will print global
outer()  # then it will print out the output from the outer function
#1 prints outer x = 'local
#2 it prints the value for x in the inner function and changes the outer value to nonlocal
#3 prints non local
print(x) #prints the value for x after the change, the change happens after execution of inner and call of the change global it takes the global and changes it to the new val