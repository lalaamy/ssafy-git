class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author) :
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author

class Other_Model(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at) :
        super().__init__(data_type, title, content, created_at, updated_at)

    def save(self):
        print('데이터를 다른 장소에 저장합니다.')

class ExtendedModel(Novel, Other_Model) :
    TYPE = 'Other Model'
    def __init__(self, data_type, title, content, created_at, updated_at, author, extended_type):
        super().__init__(data_type, title, content, created_at, updated_at, author)
        self.extended_type = extended_type

    def display_info(self) :
        print (f"PK: {self.PK}, TYPE: {self.TYPE}, Extended Type: {self.extended_type}")
    
    def save(self):
        print('데이터를 확장해서 저장합니다.')

extended = ExtendedModel(
    data_type='extended',
    title='제목',
    content='내용',
    created_at='2025-07-30',
    updated_at='2025-07-31',
    extended_type='Extended Type',
    author = '작가'
)

extended.display_info()
extended.save()

# hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
# chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
# print('Novel 모델 인스턴스의 PK와 save 메서드')
# print(hong.PK)
# print(chun.PK)
# hong.save()
# chun.save()
# print(hong.author)
# print(chun.author)
# print('---')

# company = Other_Model('회사', '회사명', '회사 설명', 2000, 2023)
# print('Other 모델 인스턴스의 PK와 save 메서드')
# print(company.PK)
# company.save()

# print('---')
# print('모델 별 타입')
# print(Novel.TYPE)
# print(Other_Model.TYPE)

