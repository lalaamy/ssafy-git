number_of_people = 0

print("현재 가입 된 유저 수 :", number_of_people)

def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people

def create_user():
    user_data = {'name' : '홍길동', 'age' : '30', 'address' : '서울'}    
    print (f"{user_data['name']}님 환영합니다!")
create_user()

print ("현재 가입 된 유저 수 :", increase_user())