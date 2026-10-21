# 1
class Laptop:
    def __init__(self,brand,ram,rom,price):
        self.brand = brand
        self.ram = ram
        self.rom = rom
        self.price = price

l1 = Laptop("Lenovo","8GB","512GB",60000)
l2 = Laptop("Dell","12GB","1TB",80000)
l3 = Laptop("HP","8GB","512GB",65000)


# 2
class Bike:
    def __init__(self,name,company,mileage,price):
        self.name = name
        self.company = company
        self.mileage = mileage
        self.price = price

b1 = Bike("Hunter 350","Royal Enfield", "30 Km/L", 200000)
b2 = Bike("Unicorn","Honda", "60 Km/L", 150000)
b3 = Bike("Pulsar","Bajaj", "50 Km/L", 150000)


# 3
class Notebook:
    def __init__(self, s, p, c):
        self.size = s
        self.pages = p
        self.company = c

n1 = Notebook("A4",200,"classmate")
n2 = Notebook("A4", 100, "classmate")


# 4
class Watch:
    def __init__(self,company,type,price):
        self.company = company
        self.type = type
        self.price = price

w1 = Watch("Titan","Analog",2000)
w2 = Watch("Fastrack","Digital",4000)
w3 = Watch("Sonata","Digital",2100)


# 5
class Flat:
    def __init__(self,room,area,price):
        self.rooms = room
        self.area = area
        self.price = price

f1 = Flat(4,"900 sq ft",2500000)
f2 = Flat(3,"700 sq ft", 1900000)


# 6
class Mobile:
    def __init__(self, company, ram, rom, price):
        self.company = company
        self.ram = ram
        self.rom = rom
        self.price = price

m1 = Mobile("Motorola","8 GB","256 GB", 25000)
m2 = Mobile("Samsung", "8 GB", "128 GB", 21000)
m3 = Mobile("Vivo", "4 GB", "64 GB", 12000)


# 7
class Shoes:
    def __init__(self, company, color, price):
        self.company = company
        self.color = color
        self.price = price

s1 = Shoes("Spark","Red",2000)
s2 = Shoes("Campus","Black",1500)
s3 = Shoes("Redtape","White",2500)


# 8
class WaterTank:
    def __init__(self,capacity,color):
        self.capacity = capacity
        self.color = color

w1 = WaterTank("1000 L", "blue")
w2 = WaterTank("500 L", "White")


# 9
class Pen:
    def __init__(self,color,type,price):
        self.inkColor = color
        self.type = type
        self.price = price

p1 = Pen("Blue","Ballpoint",10)
p2 = Pen("Black","Gel",15)
p3 = Pen("Red","Fountain",20)


# 10
class Car:
    def __init__(self,company,model,price):
        self.company = company
        self.model = model
        self.price = price

c1 = Car("Maruti","Swift",800000)
c2 = Car("Hyundai","i20",900000)
c3 = Car("Tata","Nexon",1000000)