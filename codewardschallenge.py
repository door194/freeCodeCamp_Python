#Stop gninnipS My sdroW!

# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (just like the name of this kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

def spin_words(sentence):
    words = sentence.split()

    for i, word in enumerate(words):
        if len(word) >= 5:
            words[i] = word[::-1]
        
    return " ".join(words)

sentence = input("Enter the sentece of which the words you want reversed for words with character length of 5 or more: ")

print(spin_words(sentence))