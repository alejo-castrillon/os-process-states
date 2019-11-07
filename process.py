import random


class Process:
    def __init__(self, name):
        self.name = name
        self.deactivate()

    def activate(self, pid):
        self.pid = pid
        self.priority_level = random.choice(
            ['VeryHigh', 'High', 'Medium', 'Low']
        )
        self.memory = random.randint(100, 300)
        self.quantum = random.randint(10, 50)
        self.progress = 0
        self.interaction = random.choice([True, False])

    def deactivate(self):
        self.pid = None
        self.priority_level = None
        self.memory = None
        self.quantum = None
        self.progress = None
        self.interaction = None

    def __str__(self):
        string = f'Process(name={self.name}'
        if self.pid:
            string += (
                f', pid={self.pid}, '
                f'priority_level={self.priority_level}, '
                f'memory={self.memory}, '
                f'quantum={self.quantum}, '
                f'interaction={self.interaction}'
            )
        return string + ')'

    def __repr__(self):
        return str(self)
