my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.
for i in my_set :
    print(my_dict.get(i))

various = my_dict.keys()
var = tuple(various)

my_dict.setdefault((1,2,3,'A'), '변수로도 키 설정 가능')
print (my_dict)