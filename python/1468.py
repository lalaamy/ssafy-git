# 아래 함수를 수정하시오.
def remove_duplicates(word):
    new_lst = []
    for i in range(len(word)) :
        if word[i-1] != word[i] :
            new_lst.append(word[i])
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)

