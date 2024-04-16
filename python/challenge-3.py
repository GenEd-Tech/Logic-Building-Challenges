str_1 = input("First Word: ")
str_2 = input("Second Word: ")


def anagram_check(str_1, str_2):

    print("Before" , str_2)

    for char in str_1:
        if char in str_2:
            str_2 = str_2.replace(char, "", 1)
        else:
            return False
        
    print("After" , str_2)
    return True if not str_2 else False

if anagram_check(str_1, str_2):
    print(f"{str_1} and {str_2} are anagrams")
else:
    print(f"{str_1} and {str_2} are not anagrams")


