
def multiply_and_greet(*args, **kwargs):    
    product=1
    for i in args:
        product*=i
    print(product)

    keys = kwargs.keys()
    if "age" in keys:
        return f"Hello {kwargs['name']} you were born in {kwargs['year']}"
    elif "country" in keys:
        return f"Hello {kwargs['name']} from {kwargs['country']}"
    elif "name" in keys:
        return f"Hello {kwargs['name']}"
    else:
        return f"Hello Anonymous"
   
 

    

   
  
   
    

        
