# File which will hold a stack data strcture
# Created by Lindsay Jamieson
# 4/4/2023
# Implemented by Michael Mills

import random

def ticket_line():
    queue = []
    num_entered = 0
    for i in range(100):
        num_people = random.randint(0, 2)
        for j in range(num_people):
            queue.append(num_entered)
            num_entered += 1
        if len(queue) > 0:
            served_customer = queue.pop(0)
            print(f"Served customer {served_customer}.")
    num_remaining = len(queue)
    print(f"{num_remaining} people are still in the queue.")

def main():
    
    ticket_line()

if __name__ == "__main__":
    main()