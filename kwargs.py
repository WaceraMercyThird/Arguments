# Write a function that accepts any number of integers as positional arguments and any number of a student's attributes as keyword arguments and prints the result of multiplying all of the integers with a customized greeting based on the keyword arguments. Name the function multiply_and_greet.
 


def multiply_and_greet(*args, **kwargs):    
    product=1
    for i in args:
        product*=i
    print(product)

    keys = kwargs.keys()
    if "age" in keys:
        return f"Hello {kwargs['name']} you were born in {'year'}"
    elif "country" in keys:
        return f"Hello {kwargs['name']} from {kwargs['country']}"
    elif "name" in keys:
        return f"Hello {kwargs['name']}"
    else:
        return f"Hello Anonymous"
   
 

    

   
  
   
    

        
