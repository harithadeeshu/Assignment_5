#1: Square Numbers and Return Their Sum

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
         x_sq = self.x * self.x
         y_sq = self.y * self.y
         z_sq = self.z * self.z
         sum= (x_sq + y_sq + z_sq)
         return sum
        
obj = Point(1, 3, 5)
total=obj.sqSum()  
print(total)
