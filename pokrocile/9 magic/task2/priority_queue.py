import sys


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def __iter__(self):
        return iter(self.queue)

    def push(self, task_name, priority):
        lowest_priority = sys.maxsize
        best_i = 0

        for i in range(len(self.queue)):
            if self.queue[i][1] < lowest_priority:
                lowest_priority = self.queue[i][1]
                best_i = i

        self.queue.insert(best_i, (task_name, priority))

    def pop(self):
        if len(self.queue) == 0:
            raise IndexError

        return self.queue.pop()[0]



