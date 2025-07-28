# 아래 함수를 수정하시오.
def reverse_string(word):
    arr = []
    for i in range(len(word)) :
        arr.append(word[i])
    arr.reverse()
    reverse_word = "".join(arr)
    print (reverse_word)

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH