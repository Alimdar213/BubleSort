str_input = input("Please enter numbers separated by spaces: ")
 
numbers = [int(x) for x in str_input.split()]
 
count = len(numbers)
 
for outer in range(count-1): 
    for i in range(count-outer-1):
        if numbers[i] > numbers[i+1]:
            numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
 
print(numbers)