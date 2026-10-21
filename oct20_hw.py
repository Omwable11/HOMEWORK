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
l4 = Laptop("Asus","16GB","1TB",90000)
l5 = Laptop("Acer","8GB","256GB",55000)

laptop_list = []
laptop_list.append(l1)
laptop_list.append(l2)
laptop_list.append(l3)
laptop_list.append(l4)
laptop_list.append(l5)

for obj in laptop_list:
    if obj.price >= 60000:
        print(f"Brand : {obj.brand}, RAM : {obj.ram}, ROM : {obj.rom}, Price : {obj.price}")


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
b4 = Bike("Apache","TVS", "45 Km/L", 140000)
b5 = Bike("FZ","Yamaha", "40 Km/L", 130000)

bike_list = []
bike_list.append(b1)
bike_list.append(b2)
bike_list.append(b3)
bike_list.append(b4)
bike_list.append(b5)

for obj in bike_list:
    if obj.mileage >= '50 Km/L':
        print(f"Name : {obj.name}, Company : {obj.company}, Mileage : {obj.mileage}, Price : {obj.price}")


# 3
class Pen:
    def __init__(self,color,type,price):
        self.inkColor = color
        self.type = type
        self.price = price

p1 = Pen("Blue","Ballpoint",10)
p2 = Pen("Black","Gel",15)
p3 = Pen("Red","Fountain",20)
p4 = Pen("Green","Ballpoint",12)
p5 = Pen("Blue","Gel",18)

pen_list = []
pen_list.append(p1)
pen_list.append(p2)
pen_list.append(p3)
pen_list.append(p4)
pen_list.append(p5)

for obj in pen_list:
    if obj.inkColor == "Blue":
        print(f"Ink Color : {obj.inkColor}, Type : {obj.type}, Price : {obj.price}")


# 4
class Watch:
    def __init__(self,company,type,price):
        self.company = company
        self.type = type
        self.price = price

w1 = Watch("Titan","Analog",2000)
w2 = Watch("Fastrack","Digital",4000)
w3 = Watch("Sonata","Digital",2100)
w4 = Watch("Casio","Analog",3500)
w5 = Watch("Timex","Digital",3000)

watch_list = []
watch_list.append(w1)
watch_list.append(w2)
watch_list.append(w3)
watch_list.append(w4)
watch_list.append(w5)

for obj in watch_list:
    if obj.type == "Digital":
        print(f"Company : {obj.company}, Price : {obj.price}")


# 5
class Shoes:
    def __init__(self, company, color, price):
        self.company = company
        self.color = color
        self.price = price

s1 = Shoes("Spark","Red",2000)
s2 = Shoes("Campus","Black",1500)
s3 = Shoes("Redtape","White",2500)
s4 = Shoes("Nike","Blue",5000)
s5 = Shoes("Adidas","Black",6000)

shoes_list = []
shoes_list.append(s1)
shoes_list.append(s2)
shoes_list.append(s3)
shoes_list.append(s4)
shoes_list.append(s5)

for obj in shoes_list:
    if obj.color == "Black":
        print(f"Company : {obj.company}, Price : {obj.price}")

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
m4 = Mobile("Realme", "8 GB", "128 GB", 15000)
m5 = Mobile("Apple", "16 GB", "256 GB", 60000)

mobile_list = []
mobile_list.append(m1)
mobile_list.append(m2)
mobile_list.append(m3)
mobile_list.append(m4)
mobile_list.append(m5)

for obj in mobile_list:
    if obj.company == "Motorola":
        print(f"Company : {obj.company}, RAM : {obj.ram}, ROM : {obj.rom}, Price : {obj.price}")

# 7

class Notebook:
    def __init__(self, s, p, c,price):
        self.size = s
        self.pages = p
        self.company = c
        self.price = price

n1 = Notebook("A4",200,"classmate",100)
n2 = Notebook("A4", 100, "classmate",70)
n3 = Notebook("A5", 150, "Camlin",80)
n4 = Notebook("A4", 250, "Prime",150)
n5 = Notebook("A5", 200, "Navneet",120)

notebook_list = []
notebook_list.append(n1)
notebook_list.append(n2)
notebook_list.append(n3)
notebook_list.append(n4)
notebook_list.append(n5)

for obj in notebook_list:
    if obj.company == "classmate":
        print(f"Size : {obj.size}, Pages : {obj.pages}, Price : {obj.price}")


# 8
class Car:
    def __init__(self,company,model,price):
        self.company = company
        self.model = model
        self.price = price

c1 = Car("Maruti","Swift",800000)
c2 = Car("Hyundai","i20",900000)
c3 = Car("Tata","Nexon",1000000)
c4 = Car("Kia","Seltos",1200000)
c5 = Car("Mahindra","XUV700",1500000)

car_list = []
car_list.append(c1)
car_list.append(c2)
car_list.append(c3)
car_list.append(c4)
car_list.append(c5)

for obj in car_list:
    if obj.price <= 1000000:
        print(f"Company : {obj.company}, Model : {obj.model}, Price : {obj.price}")