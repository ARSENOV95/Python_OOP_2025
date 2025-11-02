class Account:
    def __init__(self,id_ :int,balance :float | int, pin: int):
        self.__id = id_
        self.balance = balance
        self.__pin = pin

    def __validate_pin(self,pin):
       correct_pin = (pin == self.__pin)
       return correct_pin



    def get_id(self,pin :int) -> int | str:
        if self.__validate_pin(pin):
            return self.__id
        return "Wrong pin"

    def change_pin(self,old_pin,new_pin) -> str:
        if self.__validate_pin(old_pin):
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"

a = Account(1234, 44, 4444)
res = a.get_id(1234)
print(res)
res = a.get_id(4444)
print(res)
res = a.balance
print(res)
res = a.change_pin(4444, 1234)
print(res)

