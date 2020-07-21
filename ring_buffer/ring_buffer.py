class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.size = 0
        self.overloadedCount = 0

    def append(self, item):
        if self.size < self.capacity:
            self.storage.append(item)
            self.size += 1
        else:
            if self.overloadedCount > self.capacity - 1:
                self.overloadedCount = self.overloadedCount % (self.capacity)
            self.storage[self.overloadedCount] = item
            self.overloadedCount += 1

    def get(self):
        return self.storage