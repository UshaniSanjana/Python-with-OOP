import random

class Person:
    def __init__(self, age_group, infected=False):
        self.age_group = age_group
        self.infected = infected
        self.days_infected = 0
        self.days_to_symptoms = 5
        self.immunity_duration = random.randint(180, 210)  # 6 to 7 months

    def infect(self):
        if not self.infected:
            self.infected = True

    def update(self):
        if self.infected:
            self.days_infected += 1
            if self.days_infected == 11:
                self.infected = False
                self.days_infected = 0

    def is_symptomatic(self):
        return self.days_infected >= self.days_to_symptoms
