class PriorityQueue:
    def __init__(self):
        self.elements = []

    def __len__(self):
        return len(self.elements)

    def __iter__(self):
        return iter(self.elements)

    def push(self, item, priority):
        self.elements.append((item, priority))
        self.elements.sort(key=lambda x: x[1])

    def pop(self):
        if not self.elements:
            raise IndexError("Trying to pop from an empty priority queue")
        return self.elements.pop(0)[0]

# Příklad použití
priority_queue = PriorityQueue()
priority_queue.push("Task 1", 3)
priority_queue.push("Task 2", 1)
priority_queue.push("Task 3", 2)

print("Priority Queue Length:", len(priority_queue))

print("Tasks in Priority Order:")
for task in priority_queue:
    print(task)

print("Processing tasks in Priority Order:")
while len(priority_queue) > 0:
    task = priority_queue.pop()
    print("Processing:", task)
