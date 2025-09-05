numbers = [10, 50, 30, 40, 25]
# list method 
numbers.append(4)
numbers.insert(0,1)
numbers.remove(50)
numbers.pop()     
numbers.sort() 
numbers.reverse() 
print(numbers)

# Traversing a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print( fruits[i])


# Membership check

numbers = [10, 50, 30]
if 20 in numbers:
    print("20 is present")
else:
    print("Not found")



# problem solve


# Sum, Max, Min Create list → print sum, max, min
nums  = [10, 20, 50,59.50]
print(sum(nums))
print(max(nums))
print(min(nums))
    
        
# Filter strings List of strings → print strings length > 3
fruits=["asss","s",'s',"d"]
for f in fruits:
    if(len(f) > 3):
        print(f)

# Reverse list


# User input list → print reversed list
n= int(input("enter:"))
numbers=[]
for i in range(n):
    num= int(input(f" enter lement {i+1}: "))
    numbers.append(num)


print(list(reversed(numbers)))
numbers.reverse()
print(numbers)
# Check number exists
