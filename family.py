from person import Person
import random

class Family:
    infect_count=0
    def __init__(self, members):
        self.members = members

    def infect_family(self):
        for member in self.members:
            member.infect()

    def update_family(self):
        
        for member in self.members:
            if(member.infected):
                self.infect_family
            if(member.infected):
                self.infect_count +=1
            member.update()

    def is_infected(self):
        return any(member.infected for member in self.members)

