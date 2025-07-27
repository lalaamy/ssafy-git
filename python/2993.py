food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.

for food in food_list :
    name_list = food['이름']
    if name_list == '토마토' :
        food['종류'] = '과일'
        print (f'{food['이름']}은/는 {food['종류']}(이)다.')
    elif name_list == '자장면' :
        print (f'{food['이름']}엔 고춧가루지')
        print (f'{food['이름']}은/는 {food['종류']}(이)다.')
    else :
        print (f'{food['이름']}은/는 {food['종류']}(이)다.')
print (food_list)

