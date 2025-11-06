from project.customer import Customer
from project.dvd import DVD

class MovieWorld:
    def __init__(self,name :str):
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @property
    def dvd_capacity(self):
        return 15

    @property
    def customer_capacity(self):
        return 10

    #=================MY DO NOT REPEAT YOURSELF SOLUTION
    def __get_cust(self,customer_id :int):
        return next((c for c in self.customers if c.id == customer_id),None)

    def __get_dvd(self,dvd_id :int):
        return next((d for d in self.dvds if d.id == dvd_id), None)



    def add_customer(self,customer: Customer):
        if len(self.customers) < self.customer_capacity:
            self.customers.append(customer)

    def add_dvd(self,dvd: DVD):
        if len(self.dvds) < self.dvd_capacity:
            self.dvds.append(dvd)

    def rent_dvd(self,customer_id: int, dvd_id: int):
       customer = self.__get_cust(customer_id)
       dvd = self.__get_dvd(dvd_id)

       if customer and dvd:
           if customer.age < dvd.age_restriction:
               return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

           if dvd in customer.rented_dvds:
               return f"{customer.name} has already rented {dvd.name}"

           if dvd not in customer.rented_dvds and dvd.is_rented:
               return "DVD is already rented"

           if dvd not in customer.rented_dvds and not dvd.is_rented:
               customer.rented_dvds.append(dvd)
               dvd.is_rented = True
               return f"{customer.name} has successfully rented {dvd.name}"
       return  None

    def return_dvd(self,customer_id, dvd_id):
        customer = self.__get_cust(customer_id)
        dvd = self.__get_dvd(dvd_id)
        if dvd_id in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = self.customers + self.dvds
        return '\n'.join(el.__repr__() for el in result)
