class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.cur = 0

    def get(self):
        return self.data

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        elif len(self.data) == self.capacity:
            self.data[self.cur] = item
            self.cur = (self.cur+1) % self.capacity