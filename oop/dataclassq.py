from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    stock: int

# object তৈরি
p1 = Product("Laptop", 80000, 10)
p2 = Product("Laptop", 80000, 10)

# print করলে সুন্দরভাবে দেখাবে
print(p1)  

# equality check (default ভাবে কাজ করবে)
print(p1 == p2)  

# attribute ব্যবহার
print(f"Product: {p1.name}, Price: {p1.price}, Stock: {p1.stock}")
