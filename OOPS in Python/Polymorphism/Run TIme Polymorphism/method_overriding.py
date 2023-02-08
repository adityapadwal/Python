class Father: # parent class 
    def bike(self):
        print("Harley Davidson!")

    def laptop(self):
        print("Laptop with 20GB RAM and 500GB HDD I3 processor")

class Son(Father):
    def laptop(self):
        print("As per my programming requirement, this is not cool for me")
        print("Laptop with 8GB RAM and 1TB SSD I7 processor")

obj = Son()
obj.bike()
obj.laptop()