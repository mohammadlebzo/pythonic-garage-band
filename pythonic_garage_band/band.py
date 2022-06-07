from abc import ABC, abstractmethod


class Band:
    instances = []

    def __init__(self, name, members):
        self.__class__.instances.append(self)
        self.name = name
        self.members = members

    @staticmethod
    def to_list():
        return Band.instances

    def play_solos(self):
        temp = []
        for i in self.members:
            temp.append(i.play_solo())
        return temp

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Band({self.name}, {self.members})'


class Musician(ABC):

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return 'face melting guitar solo'

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'


class Bassist(Musician):
    def __init__(self, name):
        self.name = name

    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'


class Drummer(Musician):
    def __init__(self, name):
        self.name = name

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return 'rattle boom crash'

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'

