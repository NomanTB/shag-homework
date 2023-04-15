from logging import *
import random

basicConfig(level=DEBUG,filename="logs.log", filemode="a")

warning("========== New log =====================================================================")



class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            debug("I have bought fuel for my car")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            debug("I have bought some food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            debug("Wow! It was truly delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        debug(f"{day:=^50}")
        human_indexes = self.name + "'s indexes"
        debug(f"{human_indexes:^50}")
        debug(f"Money – {self.money}")
        debug(f"Satiety – {self.satiety}")
        debug(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        debug(f"{home_indexes:^50}")
        debug(f"Food – {self.home.food}")
        debug(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        debug(f"{car_indexes:^50}")
        debug(f"Fuel – {self.car.fuel}")
        debug(f"Strength – {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            debug("Depression…")
            return False
        if self.satiety < 0:
            debug("Died of starvation…")
            return False
        if self.money < -500:
            debug("Bankrupt…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            debug("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            debug(f"I bought a new car {self.car.brand}")
        if self.job is None:
            self.get_job()
            debug(f"I don't have a job, looks like I have to get a job {self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)

        dice = random.randint(1, 4)
        if self.satiety < 20:
            debug("Damn, I`m hungry, I will go and eat something")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                debug("I want to chill, but there is so much mess… So I will clean the house")
                self.clean_home()
            else:
                debug("Let`s have a rest!")
                self.chill()
        elif self.money < 0:
            debug("It`s time to work!")
            self.work()
        elif self.car.strength < 15:
            debug("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            debug("Let`s have a rest!")
            self.chill()
        elif dice == 2:
            debug("It`s time to work!")
            self.work()
        elif dice == 3:
            debug("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            debug("Time for treats!")
            self.shopping(manage="delicacies")

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            debug("The car is out of fuel OR needs repairing")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
    "Motion designer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 55, "gladness_less": 3},
    "SMM manager": {"salary": 80, "gladness_less": 25},
    "3D designer": {"salary": 70, "gladness_less": 1},
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

nick = Human(name="Liam")
for day in range(1, 366):
    if nick.live(day) == False:
        break
