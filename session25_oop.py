
# customer id
# name
# balance

# deposit
# withdrawal

class Account:
	def __init__(self,customer_id,name,initial_balance=0):
		self.id = customer_id
		self.name = name
		self.balance = initial_balance

customer1 = Account("101","Test Testinger")
print(customer1.id,customer1.name,customer1.balance)
customer2 = Account("102","Demo Testinger")
print(customer2.id,customer2.name,customer2.balance)
customer3 = Account("103","Fry Testinger")
print(customer3)
	