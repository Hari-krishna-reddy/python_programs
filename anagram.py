#"listen" and "silent" are anagrams because you can rearrange the letters of one to
#form the other.
#"debit card" and "bad credit" are anagrams.
#"astronomer" and "moon starer" are anagrams.





word1=input('Enter first word:')
word2=input('Enter second word:')

#method 1
def method1(word1,word2):
    for i in word1:
        if i.isalpha():
            if word1.count(i)!=word2.count(i):
                print('not anagram')
                return
    print('an anagram')
    
method1(word1,word2)
# if there are spaces in 1st and not in 2nd word then

from collections import Counter

def method2(word1, word2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_word1 = word1.replace(" ", "").lower()
    cleaned_word2 = word2.replace(" ", "").lower()

    return Counter(cleaned_word1) == Counter(cleaned_word2)

def method3(word1, word2):
    
     # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_word1 = word1.replace(" ", "").lower()
    cleaned_word2 = word2.replace(" ", "").lower()
    
    return sorted(cleaned_word1) == sorted(cleaned_word2)

def method4(word1, word2):
     # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_word1 = word1.replace(" ", "").lower()
    cleaned_word2 = word2.replace(" ", "").lower()
    freq_map1 = {}
    freq_map2 = {}

    for char in cleaned_word1:
        freq_map1[char] = freq_map1.get(char, 0) + 1

    for char in cleaned_word2:
        freq_map2[char] = freq_map2.get(char, 0) + 1

    return freq_map1 == freq_map2


# Example with spaces
word1 = "listen"
word2 = "silent "

# Check if anagrams, considering spaces
result = are_anagrams_counting(word1, word2)

print(f"{word1} and {word2} are anagrams: {result}")

    
                
            