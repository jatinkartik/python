class Vector2d:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j "
class Vector3d(Vector2d):
    def __init__(self,i,j,k):
        super().__init__(i,k)
        self.kcap = k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j +{self.kcap}k"


var = Vector3d(3,5,5)
var1 = Vector2d(9,8)
print(var)
print(var1)