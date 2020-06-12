class RingBuffer:
    def __init__(self, capacity):
        #the capacity will be equal to the value passed in
        #in this test case it will be 5
        self.capacity = capacity
        self.current = 0 #sets current to 0
        self.storage = [None]*capacity # Sets items in storage to None
    

    def append(self, item):
        #append if current < capacity
        if self.current < self.capacity:
            #gets rid of oldest number after current = capacity
            old = self.storage.pop(self.current)
            self.storage.insert(self.current, item)
            print("After:", self.storage, "Remove item:", old)
            self.current += 1
            
            if self.current == self.capacity:
                self.current = 0



    def get(self):
        list = []
        for item in self.storage:
            if item != None:
                list.append(item)
        return list

