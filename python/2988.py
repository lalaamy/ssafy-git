def my_multi(number_1, number_2):
    result_1 = number_1 * number_2
    
    return result_1
print(my_multi(2, 3))
# my_multi(2, 3) 결과 : 6
# 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.


def is_negative(number):
    if number <= 0 :
        return True
    else :
        return False
result_2 = is_negative(3)
print(result_2)
# is_negative(3) 결과 : False
# 함수를 수정하고 호출 결과를 result_2 변수에 할당하여 출력하시오.


def default_arg_func(result_3 = '기본 값'):
    return result_3
print(default_arg_func())

def default_arg_func(result_4 = '다른 값'):
    return result_4
print(default_arg_func())
