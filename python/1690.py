import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

dummy_data = []

for data in range(1,len(parsed_data)) :
    companyname = parsed_data[data]["company"]["name"]
    lat = float(parsed_data[data]['address']["geo"]["lat"])
    lng = float(parsed_data[data]['address']["geo"]["lng"])
    name = parsed_data[data]["name"]
    data_dict = {
    "company": companyname,
    "lat": lat,
    "lng": lng,
    "name": name
    }
    if lat < 80 and lng > -80 :
        dummy_data.append(data_dict)


black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user():
    censored_user_list = {}


def censorship():
    if companyname in black_list :
        print(f'{companyname} 소속의 {name}은/는 등록할 수 없습니다.')
        return False
    else :
        print('이상 없습니다.')
        return True
    
