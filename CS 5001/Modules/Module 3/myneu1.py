''' Align Online
    CS5001
    Sample code -- using functions to write cleaner, elegant code,
    in this case replicating the myneu.edu website, roughly.
'''

def view_calendar():
    ''' Function view_calendar
        Parameters: none
        Returns: nothing
    '''
    print("Calendar:\n"
          "Start date: Jan 7th\n"
          "End date: April 27th\n")

def view_class_schedule(my_class):
    ''' Function view_class_schedule
        Parameter: string
        Returns: nothing
    '''
    if my_class == "CS5001":
        print("MR 6-9:00pm")
    else:
        print("T 6-9:00pm")

def calculate_tuition(total_tuition, scholarship_pct):
    ''' Function calculate_tuition
        Parameters: two floats
        Returns: float
    '''
    to_pay = total_tuition - total_tuition * scholarship_pct
    return to_pay

def main():
    view_calendar()
    view_calendar()
    view_calendar()

    view_class_schedule("CS5001")
    print("...")
    view_class_schedule("CS5002")
    print("...")

    my_class = input("What class are you taking?\n")
    print("here's your schedule...\n")
    view_class_schedule(my_class)

    tuition = float(input("How much is total tuition?\n"))
    discount = float(input("How much scholarship pct did you get?\n"))
    left_to_pay = calculate_tuition(tuition, discount)
    
    print("You need to pay $", left_to_pay, sep = "")

    
main()

