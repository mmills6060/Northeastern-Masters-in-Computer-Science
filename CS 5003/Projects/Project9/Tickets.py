# File which will hold a stack data strcture
# Created by Lindsay Jamieson
# 4/4/2023
# Implemented by Michael Mills

import random
from queue import Queue


def ticket_line(num_people_list):
    queue = Queue()
    num_entered = 0
    for i in range(100):
        num_people = random.randint(0, 2)
        for j in range(num_people):
            queue.put(num_entered)
            num_entered += 1
        if not queue.empty():
            served_customer = queue.get()
            print(f"Served customer {served_customer}.")
            num_people_list.append(num_people)
    num_remaining = queue.qsize()
    print(f"{num_remaining} people are still in the queue.")
    return num_remaining,num_people_list
def main():
    num_people_list = []
    ticket_line(num_people_list)
    return num_people_list
if __name__ == "__main__":
    main()