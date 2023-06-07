''' Align Online
    CS5001
    Sample code -- example of implementing the Queue ADT.
                   This version uses Python's built-in list
'''


class Queue:
    def __init__(self, size):
        ''' Constructor
        Parameters:
           self -- the current object
           size -- the initialize size of our queue
        '''
        self.data = list()

    def enqueue(self, item):
        ''' enqueue -- adds something to the end of the queue
        Parameters:
           self -- the current object
           item -- the item to add to the queue
        Returns nothing
        '''
        self.data.append(item)

    def dequeue(self):
        ''' deqeuue -- removes something from the front of the queue
        Parameters:
           self -- the current object
        Returns the element of the front of the queue
        '''
        return self.data.pop(0)

    def dump(self):
        ''' dump -- debugging method for the queue
        Parameters:
           self -- the current object
        '''
        print(self.data)


def main():
    ''' 
    Driver program that uses our queue so that we can see it working
    '''
    my_queue = Queue(10)
    while True:
        cmd = input("enqueue, dequeue, dump or exit (e, d, dump or exit)? ")
        if cmd == "e":
            val = input("Data to add? ")
            my_queue.enqueue(val)
        elif cmd == "d":
            val = my_queue.dequeue()
            print("dequeue() returned --", val)
        elif cmd == "dump":
            my_queue.dump()
        elif cmd == "exit":
            break


if __name__ == "__main__":
    main()
