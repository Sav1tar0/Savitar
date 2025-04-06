my_list = ["listen", "silent", "enlist", "rat", "tar", "art", "cat", "tac"]


def find_anagram_group_number(my_list) :
    anagrams = []
    count = 0

    for word in my_list :
        anagram = ''
        for x in "qwertyuiopasdfghjklzxcvbnm" :
            anagram += str(word.count(x)) + ','

        if anagram not in anagrams : 
            anagrams.append(anagram)
            count += 1
            
    return count     

print(find_anagram_group_number(my_list))
