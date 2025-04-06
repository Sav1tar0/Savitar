word = input("Enter a word: ")
vowels = "aeiuoAEIOU"
                                                  

def count_vowels(s):
    list = []
    for i in s :
        if i in vowels:
             list.append(i)
    return len(list)

print(count_vowels(word))