class Calculator:
    def __init__(self,cuberoot):
        self.cuberoot = cuberoot

    def getCubeRoot(self):
        print((self.cuberoot)**(1/3))
var = Calculator(15625)
var.getCubeRoot()
print((15625)**(1/3))