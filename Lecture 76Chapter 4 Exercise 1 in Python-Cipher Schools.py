class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price=max(price,0)
    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}...."

class Smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        Phone.__init__(self,brand,model_name,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}...."

phone=Phone('nokia','1100',1000)
smartphone=Smartphone('oneplus','5',30000,'6GB','64GB','20MP')
print(phone.full_name())
print(smartphone.full_name())+f"and price is {smartphone._price}"