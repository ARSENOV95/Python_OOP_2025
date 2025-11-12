from project.animals.animal import Animal
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
        if self.__budget - price >= 0:
            if self.__animal_capacity > 0:
                self.animals.append(animal)
                self.__budget -= price
                self.__animal_capacity -= 1
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough space for animal"
        return "Not enough budget"


    def hire_worker(self,worker : Worker) -> str:
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            self.__workers_capacity -= 1
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self,worker_name :str)  -> str:
        worker = next((n for n in self.workers if n.name == worker_name),None)

        if worker:
            self.workers.remove(worker)
            self.__workers_capacity += 1
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        salaries = sum(w.salary for w in self.workers)

        if self.__budget -salaries >= 0:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        expenses = sum(a.money_for_care for a in self.animals)

        if self.__budget - expenses >= 0:
            self.__budget -= expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self,amount:int) -> None:
        self.__budget += amount


    def animals_status(self):
        result = [f'You have {len(self.animals)} animals']
        animal_types = dict()

        for a in self.animals:
            if a.__class__.__name__ not in animal_types.keys():
                animal_types[a.__class__.__name__] = []
            animal_types[a.__class__.__name__].append(a.__repr__())

        for type_,animals in animal_types.items():
            result.append(f'----- {len(animals)} {type_}')
            for animal in animals:
                result.append(animal.__repr__())

        return '\n'.join(result)

    def workers_status(self):
        result = [f'You have {len(self.workers)} workers']
        worker_types = dict()

        for w in self.workers:
            if w.__class__.__name__ not in worker_types.keys():
                worker_types[w.__class__.__name__] = []
            worker_types[w.__class__.__name__].append(w.__repr__())

        for type_,workers_ in worker_types.items():
            result.append(f'----- {len(workers_)} {type_}')
            for worker in workers_:
                result.append(worker.__repr__())

        return '\n'.join(result)






