# Michael Arthur Mills
# Fall 2023, CS 5001
# Lab 2 code file
# Practicing good code style and more complex functions


# Ask the user to provide the date in number form
def main():
    date = str(input("Please provide the date in the following format, MM/DD/YYYY --> "))
    
# Use split function to single out the month
    datesplit = date.split("/")
    month = datesplit[0]
    
# Single out what month is what season, print season

# I am keeping as a string because there are additional complexities 
# changing to an integer, specifically when there is a zero digit in front
    if  month in ["12" , "01" , "02"]:
        print("The season is Winter")
    else:
        if  month in ["03" , "04" , "05"]:
            print("The season is Spring")
        else:
            if  month in ["06" , "07" , "08"]:
                print("The season is Summer")
            else:
                print("The season is Fall")        
main()