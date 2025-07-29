# 아래 함수를 수정하시오.
def count_character(words, word):
    count_word = words.count(word)
    return count_word


result = count_character("Hello, World!", "o")
print(result)  # 2