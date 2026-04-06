#Create a function get range that accepts real numbers as arguments and returns  s
#the difference between the maximum and minimum values.

def get_range(*numbers):
    if len(numbers)==0:
        return "no numbers"
    max=numbers[0]
    min=numbers[0]
    
    for num in numbers:
        if num <min:
            min=num
        if num>max:
             max-num
             
    return  max - min

result=get_range(1.0,3.4,3.4,5.6) 
print(result)       