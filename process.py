import random

from utilities import trunc

class Process:
    PRIORITIES = "VeryHigh", "High", "Medium", "Low"

    def __init__(self, name):
        self.name = name
        self.name_pad = 0
        self.progress = 0
        self.deactivate()

    def activate(self, pid, quantum_rat):
        self.pid = pid
        self.priority = random.choice(self.PRIORITIES)
        self.memory = random.randint(100, 300)
        self.processor_time = random.randint(10, 50)
        self.quantum = self.processor_time / quantum_rat
        self.advance = 1 / self.quantum
        self.interaction = random.choice((True, False))

    def deactivate(self):
        self.pid = None
        self.priority = None
        self.memory = None
        self.quantum = None
        self.processor_time = None
        self.interaction = None

    def __str__(self, show_all=False):
        string = f"Process(name={self.name:<{self.name_pad}}"
        if self.pid:
            string +=  f", PID={self.pid:0>3}"
            if show_all:
                string += (
                    f", priority={self.priority:<8}"
                    f", processor_time={self.processor_time}"
                    f", quantum={round(self.quantum, 4)}"
                    f", progress={trunc(self.progress * 100, 4)}"
                    f", interaction={str(self.interaction):<5}"
                )
        return string + ")"

    def __repr__(self):
        return str(self)

    def __eq__(self, process):
        return isinstance(process, Process) and int(self.pid) == int(process.pid)
