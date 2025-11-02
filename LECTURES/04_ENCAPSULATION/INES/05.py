class Account:
    def __init__(self,id_,balance,pin):
        self.__id = id_
        self.balance = balance
        self.__pin = pin

    def get_id(self,pin):
        if self.__pin == pin:
            return self.__id
        return "Wrong pin"


    def change_pin(self,old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"