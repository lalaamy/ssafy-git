number_of_people = 0
number_of_book = 100

def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user():
    for i in range(5) :
        print (f"{name[i]}님 환영합니다!")
create_user()


many_user = []

for i in range(5) :
    user_dict = {'name' : name[i], 'age' : age[i], 'address' : address[i]}
    many_user.append(user_dict)

print(many_user)


def decrease_book():
    dec_lst = []
    for i in range(len(name)) : 
        decrease_num = many_user[i]['age'] // 10
        dec_lst.append(decrease_num)
    return dec_lst
print(decrease_book())

keys = ["name", "age"]
new_dict = dict(map(lambda k: (k, many_user[k]), keys))
print()