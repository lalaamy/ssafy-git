
def increase_user(name):
    for i in name:
        print(f"{i}님 환영합니다.")



def rental_books(age, name, number_of_book):
    rental_lst = []
    remain_lst = []
    for a in age:
        book = a//10  #권수 세기
        number_of_book -= book
        rental_lst.append(book)
        remain_lst.append(number_of_book)
    return remain_lst, rental_lst
  


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

increase_user(name)
result = rental_books(age, name, 100)


for i in range(1):
    for j in range(5):
        print(f"남은 책의 수 : {result[i][j]}")
        print(f"{name[j]}님이 {result[i+1][j]}권의 책을 대여하였습니다.")
    


