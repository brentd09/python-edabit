import math

def fact_of_fact(val):
    result = [math.factorial(i) for i in range(1,val+1)]
    return math.prod(result)

print(fact_of_fact(4) )  
