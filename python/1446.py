# 아래 함수를 수정하시오.
def find_min_max(lst):
    lst_result = []
    lst_result.append(min(lst))
    lst_result.append(max(lst))

    return tuple(lst_result)

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
