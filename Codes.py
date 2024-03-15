def DataTypeControl(x):
    
    # check data type
    
    try:
        return int(x)
    except ValueError:
        pass
    
    try:
        return float(x)
    except ValueError:
        pass
    
    try: 
        return str(x)
    except ValueError:
        pass
    
    # For possible errors
    return "I think something's wrong"

    
int_=[]
str_=[]
float_=[]

a = int(input("How many data will you enter: "))

# any number of data input
for i in range(a):
    # data input
    x = input(f"{i+1}. Enter data: ")
    
    # send data to the function
    x = DataTypeControl(x)
    
    # sorting data by type
    if type(x) == int:
        int_.append(x)
    elif type(x) == float:
        float_.append(x)
    elif type(x) == str:
        str_.append(x)
        
    # For possible errors
    else:
        print("Escape block for possible errors")
        
    
# print data to the screen by type
print("int: ",int_,"\nfloat: ",float_,"\nstr: ",str_)
