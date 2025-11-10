class Customer:
    id = 1
    def __init__(self,name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email


    def get_next_id(self):
        return self.id + 1

    def __repr__(self):
        return f"Customer {self.id} {self.name}; Address: {self.address}; Email: {self.email}"

