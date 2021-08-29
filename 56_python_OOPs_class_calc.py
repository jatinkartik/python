class Calculator:
    square = 5
    cube = 5
    def __init__(self,square,cube):
        print("hey welcome to calculator in objected oriented programming")
        self.square = square
        self.cube = cube
    def getSquareRoot(self):
        print((self.square)**(1/2))
    def getCubeRoot(self):
        print((self.cube)**(1/3))
    def getSquare(self):
        print((self.square)**2)
    def getCube(self):
        print((self.cube)**3)

var = Calculator(625,15625)
var.getSquareRoot()
var.getCubeRoot()
var.getSquare()
var.getCube()
print("i am checking, is i can access the elemet of calculator class ",Calculator.square,Calculator.cube)
Calculator.cube = 935345
print(Calculator.cube)
