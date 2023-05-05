# Write a Python function that takes two arguments (a and b) and returns their sum.

def additing_numbers (a,b):
    return a + b
print(additing_numbers(6,7))

# Write a Python function that takes a string as input and returns the string reversed.
def student(name):
    return "".join(reversed(name))
print(student("malaika"))


# Write a Python function that takes a list of integers as input and returns the sum of all the integers in the list.
def number(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum
print(number([2,3,4,5]))
# Write a Python function that takes a list of integers as input and returns a new list with all the even numbers removed.
def remove_even_numbers(numbs):
    new_number = []
    for i in numbs:
        if i %2 !=0:
            new_number.append(i)
    return new_number
print(remove_even_numbers([2,5,6,8,9,4]))      
    
# Write a Python function that takes a list of 
# integers as input and returns the highest value in the list.
def highest_value (number):
    i = max(number)
    return(i)
print(highest_value([5,8,9,1,12,11,16]))

# Write a Python function that takes a list of strings as input and returns a new list with all the strings capitalized.x
def capitalize_words(name):
    new_words = []
    for i in name:
        new_words.append(i.capitalize())
    return new_words
print(capitalize_words("nancy"))


