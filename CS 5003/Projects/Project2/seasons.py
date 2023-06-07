# Michael Arthur Mills
# Fall 2023, CS 5001
# Lab 2 code file
# Ask the user for a date, in number form. 
#  Then use this information to print out the season that date 
# happens in (ie 1/18/2022 is in Winter).


# Ask the user to provide the date in number form
def main():
    date = str(input("Please provide the date in the following format, MM/DD/YYYY --> "))
    
# Use split function to separate into three different values
#based on where the "/" is inputted.
    datesplit = date.split("/")

#Defining the first value in the set as month
    month = datesplit[0]
#Defining the second value in the set as day
    day = int(datesplit[1])
    
# Single out what month and day is what season, print season
    if  month == '12' or month == '01' or month == '02':
        if month == '12' and day < 20:
            print("The season is Fall")
        else:
            print("The season is Winter")
    else:
        if  month == '03' or month == '04' or month == '05':
            if month == '03' and day < 19:
                print("The season is Winter")
            else:
                print("The season is Spring") 
        else:
            if  month == '06' or month == '07' or month == '08':
                if month == '06' and day < 20:
                    print("The season is Spring")
                else:
                    print("The season is Summer")                    
            else:
                if  month == '09' or month == '10' or month == '11':
                    if month == '09' and day < 21:
                        print("The season is Summer") 
                    else:                     
                        print("The season is Fall")
                        
                                
main()