# 아래 함수를 수정하시오.
def sort_tuple(word):
    word_lst = list(word)
    new_tuple = tuple(sorted(word_lst))

    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
