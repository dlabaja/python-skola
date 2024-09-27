import sys


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def __iter__(self):
        return iter([task[0] for task in self.queue])

    def push(self, task_name, priority):
        for i in range(len(self.queue)):
            if self.queue[i][1] > priority:
                self.queue.insert(i, (task_name, priority))
                return
        self.queue.append((task_name, priority))

    def pop(self):
        if len(self.queue) == 0:
            raise IndexError

        return self.queue.pop(0)[0]



