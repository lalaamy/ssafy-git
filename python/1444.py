# 아래 함수를 수정하시오.
def even_elements(word):
    word_lst = []
    for i in range(len(word)-1,-1,-1) :
        if word[i] % 2 == 0 :
            word_lst.extend([word.pop(i)])
    word_lst.reverse()
    return word_lst


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)

