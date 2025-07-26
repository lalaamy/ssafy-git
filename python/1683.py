number_of_people = 0
name = ['김시습', '허균', '남영로', '임제', '박지원']  
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people

def create_user():
    for i in range(5) :
        print (f"{name[i]}님 환영합니다!")
create_user()

data_list = []

for i in range(5) :
    data_dict = {'name' : name[i], 'age' : age[i], 'address' : address[i]}
    data_list.append(data_dict)
print (data_list, end="")