word = input("Enter a word: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for letter in word:
    if letter.isalpha():
        if letter in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
