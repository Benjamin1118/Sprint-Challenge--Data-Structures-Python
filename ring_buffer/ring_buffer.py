class RingBuffer:
    def __init__(self, capacity, buffer = None):
        self.capacity = capacity
        self.buffer = []

    def append(self, item):
        #buffer = []
        #if adding item to buffer > capacity overwrite oldest
        if buffer.capacity == capacity:
            buffer.replace(c in capacity, item) #go to front of buffer again
        buffer.append(item)

        pass

    def get(self):
        return self.buffer
        pass