import uuid
from infection_group import InfectionGroup


class Person:
    def __init__(self, env):
        self._id = uuid.uuid1()
        self._env = env
        self._interactions = {}
        self._sick = None

    def infection_groups_at_day(self, date):
        return {group
                for day, infection_group in self._interactions.items()
                if day <= date
                for group in infection_group}

    def is_red(self):
        return self._sick == True

    def is_green(self):
        return self._sick == False

    def is_yellow(self):
        return self._sick is None

    def set_yellow(self):
        self._interactions = {self._env.day(): {InfectionGroup()}}
        self.quarintine_days = 15
        self._sick = None

    def set_green(self):
        self._interactions = {}
        self.quarintine_days = 0
        self._sick = False

    def set_red(self):
        if self._interactions == {}:
            self._interactions = {self._env.day(): {InfectionGroup()}}
        self.quarintine_days = 15
        self._sick = True

    def new_day(self):
        self._quarintine_days --
        if self._quarintine_days == 0:
            self.set_green()

    @classmethod
    def interact(cls, personA, personB, date):
        infection_groups_A = personA.infection_groups_at_day(date)
        infection_groups_B = personB.infection_groups_at_day(date)

        if infection_groups_A != infection_groups_B:
            self.quarintine_days = 15
            personA.add_interaction(infection_groups_B - infection_groups_A)
            personB.add_interaction(infection_groups_A - infection_groups_B)
            self._sick = None

