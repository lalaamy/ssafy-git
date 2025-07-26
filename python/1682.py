user_data = {'name' : '홍길동'}

def rental_book():
   return user_data['name']

number_of_book = 100

def decrease_book():
    global number_of_book
    for i in range(3) : 
        number_of_book -= 1
    return number_of_book

print(f"남은 책의 수 : {decrease_book()}")
print(f'{rental_book()}님이 {number_of_book - decrease_book()}권의 책을 대여하였습니다.')
