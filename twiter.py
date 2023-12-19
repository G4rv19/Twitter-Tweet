vowels = ["a", "e", "i", "o", "u"]

def main():
    word = input("Enter a word: ")
    output = shorten(word)
    print(output)

def shorten(word):
    for vowel in vowels:
        word = word.replace(vowel, "")
    return word

if __name__ == "__main__":
    main()
