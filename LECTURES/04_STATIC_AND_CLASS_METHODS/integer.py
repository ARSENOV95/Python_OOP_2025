from math import  floor

class Integer:
    def __init__(self,value :int):
        self.value = value

    @classmethod
    def from_float(cls,float_value):

        if not type(float_value) == float:
            return "value is not a float"
        return  cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        integer = 0
        prev_value = 0
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for char in value:
            curr_value = romans[char]
            integer += (curr_value - 2 * prev_value) if (curr_value > prev_value) else curr_value
            prev_value = curr_value

        return cls(integer)

    @classmethod
    def from_string(cls,value : str):
        if not isinstance(value,str):
            return "wrong type"

        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"




first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))