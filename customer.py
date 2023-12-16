class Customer :

    customers= []

    def __init__(self,given_name,family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.customers.append(self)

    def given_name (self):
        return self.given_name
    
    def family_name (self) :
        return self.family_name
    
    def full_name (self,given_name,family_name):
        return (f"{family_name}and {given_name}")
    
    def all (self):
        return Customer.customers
    
    

    
    

