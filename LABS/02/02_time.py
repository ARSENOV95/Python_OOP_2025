class Time:
    max_hours  =23
    max_minutes = max_seconds = 59


    def __init__(self,hours :int, minutes :int,seconds :int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self,hours :int,minutes :int,seconds :int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'


    def next_second(self):
        new_seconds = self.seconds + 1
        if  new_seconds <= Time.max_seconds:
            self.seconds = new_seconds
            return Time.get_time(self)

        self.seconds = '00'
        if self.minutes + 1 > Time.max_minutes:
            self.minutes = '00'
            self.hours += 1
            if self.hours > Time.max_hours:
                self.hours == '00'






time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())




