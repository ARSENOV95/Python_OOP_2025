
class Account:
    def __init__(self,owner:str,amount:int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: list = []


    def handle_transaction(self,transaction_amount):
        curr_bal = self.balance()
        if curr_bal - transaction_amount >= 0:
            self._transactions.append(transaction_amount)
            return None
        raise ValueError("sorry cannot go in debt!")


    def add_transaction(self,amount):
        try:
            self.handle_transaction(amount)
            return None

        except ValueError:
            return  "please use int for amount"

    def balance(self):
        return  self.amount + sum(self._transactions)

    def __str__(self):
        return  f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return self._transactions

    def __len__(self):
        return len(self._transactions)

    def __reversed__(self):
        rev = reversed(self._transactions)
        return rev

    def __gt__(self, other):
        return self.amount > other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __add__(self, other):
        name = self.owner + '&' + other.owner
        bal = self.amount + other.amount
        return Account(name,bal)





acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))

for transaction in acc:
    print(transaction)

print(acc[1])

print(list(reversed(acc)))

acc2.add_transaction(10)

acc2.add_transaction(60)

print(acc > acc2)

print(acc >= acc2)

print(acc < acc2)

print(acc <= acc2)

print(acc == acc2)

print(acc != acc2)

acc3 = acc + acc2

print(acc3)

print(acc3._transactions)