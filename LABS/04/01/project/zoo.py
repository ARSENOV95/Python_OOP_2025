from project.animal import Animal
from project.worker import Worker

class Zoo:

    def __init__(self,name :str,budget :int,animal_capacity :int,workers_capacity :int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []


    def add_animal(self,animal :Animal, price :int) -> str:
        if self.__budget >= price:
            if self.__animal_capacity:
                self.animals.append(animal)
                self.__budget -= price
                self.__animal_capacity -= 1
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough space for animal"
        return "Not enough budget"


    def hire_worker(self,worker : Worker) -> str:
        if self.__workers_capacity:
            self.workers.append(worker)
            self.__workers_capacity -= 1
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self,worker_name :str)  -> str:
        worker = next((n for n in self.workers if n.name == worker_name),None)

        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        salaries = sum(w.salary for w in self.workers)

        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        expenses = sum(a.money_for_care for a in self.animals)

        if self.__budget >= expenses:
            self.__budget -= expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self,amount:int) -> None:
        self.__budget += amount


    def animals_status(self):
        result = [f'You have {len(self.animals)} animals']

        for a in self.animals:
            result.append(f'{a.__repr__()}')

        return '\n'.join(result)
