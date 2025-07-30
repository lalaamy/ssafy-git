# 아래 클래스를 수정하시오.
class StringRepeater:
    
    # def __init__(self, num, string) :
    #     self.num = num
    #     self.string = string

    def repeat_string(self, num, string) :
        for _ in range(num) :
            print(string)


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
