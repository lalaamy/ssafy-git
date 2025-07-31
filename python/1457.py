# 아래 클래스를 수정하시오.
class Shape:
    def __init__ (self, width, height) :
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.calculate = ( self.width + self.height ) * 2
    
    # def calculate_area(self) :
        
    #     return self.area
    
    # def calculate_perimeter(self) :
        
    #     return self.calculate
    
    def print_info(self):
        print ("Width:", self.width)
        print ("Height:", self.height)
        print ("Area:", self.area)
        print ("Perimater:", self.calculate)


shape1 = Shape(5, 3)
shape1.print_info()
