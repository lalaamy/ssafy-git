class Myth :
    type_of_myth = 0

    def __init__ (self, name) :
        self.type_of_myth += 1
        self.name = name
        

    @staticmethod
    def description() :
        print ("신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.")

n1 = Myth('dangun')
n2 = Myth('greek & rome')

print(n1.name)
print(n2.name)

n1.type_of_myth()
print(n1.type_of_myth)