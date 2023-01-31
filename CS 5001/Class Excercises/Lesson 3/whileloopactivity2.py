def findLargest():
    largest = 0 
    num =int(input("Enter a positive integer"))
    
    while(num>0):
        if num >largest:
            largest = num
        num = int(input("Enter a positive integer: "))
        
    print("The biggest number was: " + str(largest))
    
findLargest()