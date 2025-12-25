#Q1: Write a Python program that takes a sentence from the user and prints:
#Number of characters
#Number of words
#Number of vowels
#Hint: Use split(), loops, and vowel checking.


#Q1:
#Write a Python program that takes a sentence from the user and prints:
sentence = input("Enter a sentence: ")

#Number of characters
num_characters = len(sentence)

#Number of words
words = sentence.split()
num_words = len(words)
#Number of vowels
vowels = "aeiouAEIOU"
num_vowels = 0

for ch in sentence:
    if ch in vowels:
        num_vowels += 1
#Hint: Use split(), loops, and vowel checking.
# Print results
print("Number of characters:", num_characters)
print("Number of words:", num_words)
print("Number of vowels:", num_vowels)




