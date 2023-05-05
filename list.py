# . Write a Python program to get a single string from two given strings, 
# separated by a space, and swap the first two characters of each string

string1 = input("employment")
string2 = input("Job ")
y, x = string1[:2], string2[:2]
new_string1 = y + string1[2:]
new_string2 = x + string2[2:]
result = f"{new_string1} {new_string2}"
print("Result:", result)

#   Write a Python function that takes a
# list of words and returns the longest word and the length of the longest one
def longest_word_length(words):
    longest_word = ""
    longest_length = 0
    for word in words:
        if len(word) > longest_length:
            longest_word = word
            longest_length = len(word)
    return longest_word,longest_length

print(longest_word_length(["Nancy","ELizabeth","saru"]))


# 3. Write a Python program that accepts a comma-separated sequence
# of words as input and prints the distinct words in sorted form (alphanumerically).
# Take a comma-separated sequence of words as input from the user
# Take a comma-separated sequence of words as input from the user
words = input("Enter a comma-separated sequence of words: ")
word_list = words.split(",")
sorted_words = sorted("saru")
print( ", ".join(sorted_words))



# . Write a Python function that takes two lists and
# returns True if they have at least one common member.
def two_data(list1,list2):
    results = False
    for x in list1:
        for y in list2:
            if x == y:
                results = True
            return results
print(two_data([2,4,5,6,7,8,9], [2,4,5,3,7,8,9]))        

#  Write a Python program to convert a list to a list of dictionaries.
color_name = ["Black","Red","maroon"]
color_code = ["#00000","#FF000","HF000"]


#  Write a Python program to check whether all dictionaries in a list are empty or no
my_list = [{},{},{}]
my_list1 = [{5},{},{}]
print(all(not d for d in my_list))
print(all(not d for d in my_list1))

# . Given a list of numbers, use list comprehension to remove all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]
numbers = [3,5,45,97,32,22,10,19,39,43]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# 8. Find the common numbers in two lists (without using a tuple or set) 
list_a = 1, 2, 3, 4, 
list_b = 2, 3, 4, 5,
common = [a for a in list_a if a in list_b]
print(common)


# . Use a nested list comprehension to find all of the 
# numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
result = [number for number in range (1,1000) if True in[True for x in range(2,9) if number % x == 0]]
print(result)


# Python program to remove vowels from a string
# Function to remove vowels
def remove_vowel(word):
	vowels = ['a','e','i','o','u']
	result = [letter for letter in word if letter.lower() not in vowels]
	result = ''.join(result)
	print(result)

word = "beautifull"
remove_vowel(word)

