try:  
    a=10/0
    print(a)
    raise NameError("Hello")

except NameError as e:  
        print("An exception occurred")  
        print(e)
        
except ZeroDivisionError as e1:  
        print("An exception occurred")  
        print(e1)
