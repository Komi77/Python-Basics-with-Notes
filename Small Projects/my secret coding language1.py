import random
import string

all_words = [] 

while True:

    word = input("Enter your word: ")
    wordlist = list(word)
    
    if word.lower() == "quit":
        break

    def generate_random_word(length=3):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(length))


    if len(wordlist) >= 3:
        
        
        waterloo = wordlist.pop(0)
        wordlist.append(waterloo)
        wordlist.insert(0, generate_random_word(3) )
        wordlist.append(generate_random_word(3) )
        wordfinal = ''.join(wordlist)
        all_words.append((word, wordfinal))
        print("Encoded:", wordfinal)

    elif len(wordlist) < 3:
        wordlist.reverse()
        wordlol =''.join(wordlist)
        all_words.append((word, wordfinal))
        print("Encoded:", wordfinal)
    



print("Do you want to decode it")
would = input("Yes or No: ")


if would.lower() == "yes":
    print("\nFull Decoding History:")
    for original, processed in all_words:
        if len(original) >= 3:
            # For encoded words (length ≥ 3)
            print(f"Encoded: {processed} → Original: {original}")
        else:
            # For reversed short words
            print(f"Reversed: {processed} → Original: {original}")
else:
    print("Okay, exiting without decoding.")

print("\nGoodbye!")

    





