def hello(*names):
    for name in names:
        print(f"Hello{name}")
        
def sum(*numbers):
    answer=0
    for number in numbers:
        answer+=number
        return answer
    # write a function that accepts any number of intergers and returns all of them
    
def multiply(*numbers):
    answer=1
    for number in numbers:
        anwser*=number
        return answer
def student(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
def my_country(country="burundi"):
    print (f"Hello from {country}")
    
    # A function named concatenate_args that takes any number of string arguments in positional arguments format and concatenates them into a single string
def concatenate_args(*names):
    for name in names:
        print(f"Hello +{name}")
        
#  A function named concatenate_kwargs that takes any number of string arguments in keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")       
