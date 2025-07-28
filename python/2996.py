data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.

data_alpha = []

for i in data_1 : 
    if i.isupper() or i.isspace() :
        data_alpha.append(i)
print(''.join(data_alpha))


data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.

for j in ['내', '힘', '들', '다'] :
    arr.append(data_2.find(j))
print (arr)

arr.sort()
print(arr)

for k in arr :
    string = data_2[k]
    print (string, end='')