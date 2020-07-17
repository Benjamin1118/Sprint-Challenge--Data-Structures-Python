class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity
        self.point = 0

    def append(self, item):
        
        #if adding item to buffer > capacity overwrite oldest
        if self.point < self.capacity:
            old = self.storage.pop(self.point)
            self.storage.insert(self.point, item)
            print("After:", self.storage, "Remove item:", old)
            self.point += 1

            if self.point == self.capacity:
                self.point = 0

            #list[point]
            #append to place of pointer
            #when capacity is reached start index over

    def get(self):

        return [c for c in self.storage if c is not None]
        pass