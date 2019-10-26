#假如面向对象是车，写出他的性能，颜色，座位和车开动着和驻停着
class Car:
     def __init__(xinneng,yanse,zuowei,lunzi):
       self.xinneng=xinneng
       self.yanse=yanse
       self.zuowei=zuowei
       self.lunzi=lunzi

car =Car("油","good","5座",5)
xinneng=Car.yanse
print(xinneng)

  