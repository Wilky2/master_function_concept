string = "Ayiti kapab avanse"

#egzesis 3
def capitalize_first_letter_of_each_word(string):
    return string.title()

print(capitalize_first_letter_of_each_word(string))

#egzesis 4        
def get_first_letter_of_each_word(string):
    words = string.split()
    first_letters = [word[0] for word in words]
    new_string = "".join(first_letters)
    return new_string

print(get_first_letter_of_each_word(string))

#egzesis 5
def replace_all_a_character(string):
    return string.replace("a","@")

print(replace_all_a_character(string))

#egzesis 6
def reverse_and_capitalize_string(string):
    return string[::-1].upper()

print(reverse_and_capitalize_string(string))

#egzesis 7
def find_index_of_first_a(string):
    return string.find("a")

print(find_index_of_first_a(string))

def list_index_word(string,word):
    list_index = []
    index=string.find(word)
    while index!=-1:
        list_index.append(index)
        index=string.find(word,index+1,len(string))
    return list_index

def sum_index_word(string,word):
    return sum(list_index_word(string,word))

#egzesis 8
def sum_index_of_a(string):
    sum_a = sum_index_word(string,"a")
    sum_A = sum_index_word(string,"A")
    return sum_a + sum_A

print(sum_index_of_a(string))

#egzesis 9
def list_index_of_a(string):
    return list_index_word(string,"a")

print(list_index_of_a(string))

#egzeis 10
def concat_string_with_his_len(string):
    string_without_space = "".join(string.split())
    string_with_his_len = string_without_space + str(len(string_without_space))
    return string_with_his_len
    
print(concat_string_with_his_len(string))
