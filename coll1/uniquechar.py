my_list = ["apple", "orange", "abc", "hello", "world", "xyz"]


final_list = []
def unique_char_strings_average(my_list):
    for i in my_list:
        i = set(i)
        final_list.append(len(set(i)))
    return sum(final_list) / len(final_list)

print(int(unique_char_strings_average(my_list)))

