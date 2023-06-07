# Michael Arthur Mills
# Fall 2023, CS 5001
# Class code Problem
# Practicing good code style and more complex functions
#Write code to write the first 5 powers of 2 


def main():
    number = int(input("What's your number? -->" ))
    

    print(number ** 0)
    print(number ** 1)
    print(number ** 2)
    print(number ** 3)
    print(number ** 4)
                    
   
    print("Done")
     
#Write code to compute how much money will be needed to buy fencing matterail at $5 per foot** to enclose a 10’ x 12’ area for chickens 
    length = 10
    width = 12
    fence = 5
    net = 10
    fence_cost = (length * 2 + width * 2) * fence
    net_cost = length*width*net
    print("The fence cost is $" + str(fence_cost))
    
#Now, change that to include the right amount of $10 per square foot nettling** to cover the 10’ x 12’ area so the haws don’t get the chickens 
    print("The net cost is $" + str(net_cost))
    print("Done")

main()