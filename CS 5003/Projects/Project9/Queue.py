# File which will hold a stack data strcture
# Created by Lindsay Jamieson
# 4/4/2023
# Implemented by Michael Mills



class Queue:
    def __init__(self, size):
        ''' Constructor
        Parameters:
           self -- the current object
           size -- the initialize size of our queue
        '''
        self.data = ["<EMPTY>"] * size
        self.end = 0
        self.start = 0

    def enqueue(self, item):
        ''' enqueue -- adds something to the end of the queue
        Parameters:
           self -- the current object
           item -- the item to add to the queue
        Returns nothing
        '''
        if (self.end + 1) % len(self.data) == self.start:
            print("Full!")
            return
        self.data[self.end] = item
        self.end = (self.end + 1) % len(self.data)

    def dequeue(self):
        ''' deqeuue -- removes something from the front of the queue
        Parameters:
           self -- the current object
        Returns the element of the front of the queue
        '''
        if self.start == self.end:
            print("Empty!")
            return
        item = self.data[self.start]
        self.data[self.start] = "<EMPTY>"
        self.start = (self.start + 1) % len(self.data)
        return item

    def dump(self):
        ''' dump -- debugging method for the queue
        Parameters:
           self -- the current object
        '''
        print(self.data, "Start:", self.start, ", End:", self.end)


def main():
    ''' 
    Driver program that uses our queue so that we can see it working
    '''
    my_queue = Queue(10)
    while True:
        cmd = input("enqueue, dequeue, dump or exit (e, d, dump or exit)?")
        if cmd == "e":
            val = input("Data to add? ")
            my_queue.enqueue(val)
        elif cmd == "d":
            val = my_queue.dequeue()
            print("dequeue() returned", val)
        elif cmd == "dump":
            my_queue.dump()
        elif cmd == "exit":
            break


if __name__ == "__main__":
    main()
