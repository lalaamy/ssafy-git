# 아래 함수를 수정하시오.
def union_sets(set1, set2):
    return set1 | set2

    #방법 1
    #return set1.union(set2)

    #방법 2
    #result = set()

    #방법 3
    # result.update(set1)
    # result.update(set2)
    # return result


def union_multiple_sets(*sets):
    if len(sets) == 1 :
        print ("최소 두 개의 셋이 필요합니다.")
    else :
        sets_union = set()
        for i in sets :
            sets_union = sets_union.union(i)
        return sets_union


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
# 출력 : 최소 두 개의 셋이 필요합니다