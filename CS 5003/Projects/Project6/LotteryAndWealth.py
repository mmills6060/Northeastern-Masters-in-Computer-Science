import random
import numpy as np
import numpy as numpy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib


# ----------------- THE SIMULATION ----------------- #

def generateLotteryNumbers():
    """
    Returns a list of 5 random ints between 1 and 42, inclusive, with no
    duplicates.
    """


    # Generate 5 random numbers between 1 and 43
    nums = []
    while len(nums) < 5:
        num = random.randint(1, 43)
        if num not in nums:
            nums.append(num)

    # Assign the random numbers to 5 different variables, checking for duplicates
    num1 = nums[0]

    found_num2 = False
    while not found_num2:
        num2 = random.randint(1, 43)
        if num2 != num1:
            found_num2 = True

    found_num3 = False
    while not found_num3:
        num3 = random.randint(1, 43)
        if num3 not in [num1, num2]:
            found_num3 = True

    found_num4 = False
    while not found_num4:
        num4 = random.randint(1, 43)
        if num4 not in [num1, num2, num3]:
            found_num4 = True

    found_num5 = False
    while not found_num5:
        num5 = random.randint(1, 43)
        if num5 not in [num1, num2, num3, num4]:
            found_num5 = True
    return [num1, num2, num3, num4, num5]

def countMatches(my_list, lottery_list):
    
    
    """
    Returns the number of matches between my_list and lottery_list.
    Inputs: * my_list: A list of your lottery numbers.
            * lottery_list: A list of the winning numbers.
    """
    matches = 0
    for num in my_list:
        if num in lottery_list:
            matches += 1
    return matches
def playLottery():
    """
    Returns the reward after one lottery play.
    """
    matches = countMatches(generateLotteryNumbers(), generateLotteryNumbers())
    if matches <= 1:
        reward = -1
    elif matches == 2:
        reward = 0
    elif matches == 3:
        reward = 10
    elif matches == 4:
        reward = 197
    elif matches == 5:
        reward = 212,534
    else:
        reward = "Error: Invalid number of matches"
        
    return (reward)
    
def getDisparityMessage(highIncomeList, lowIncomeList, decade):
    """
    Returns a string that describes the percentages of wealth possessed by the
    higher income half and lower income half for any given year.
    Inputs: *highIncomeList: The list containing wealth values for the high
             income group.
            *lowIncomeList: The list containing wealth values for low income
             group.
            *decade: The current decade as an integer.
    """
    # YOUR CODE HERE

    total_wealth = sum(highIncomeList) + sum(lowIncomeList)
    low_income_wealth = sum(lowIncomeList)
    high_income_wealth = sum(highIncomeList)
    lowIncomePercent = (low_income_wealth / total_wealth) * 100
    highIncomePercent = (high_income_wealth / total_wealth) * 100
    

    message = "Decade " + str(decade/10) + ": The high income group possesses " +\
        str(highIncomePercent) + "% of the community's wealth, while the low"\
        "income group possesses " + str(lowIncomePercent) +\
        "% of the community's wealth."

    return message
def simLottery(incomeList, numPlayers):
    """
    Simulates lottery play for a number of players from a given income group.
    Inputs: *incomeList: The list containing wealth values for the given
             income group.
            * numPlayers: The number of players who will play the lottery.
    """


    for i in range(numPlayers):
        try:
            reward = playLottery()
            incomeList[i] += reward
        except IndexError:
            break
#        print("Player #" + str(i+1) + " won $" + str(reward))
            
#       print("Player #" + str(i+1) + " won $" + str(reward))
    return incomeList
        #incomeList.append(incomeList[i] + reward)
#    player3_wealth = incomeList[2]
#    newplayer3_wealth = player3_wealth + reward
#    print("Player #3 won $" + str(reward) + ", adding to the wealth of player #3" + ". New wealth: $" + str(newplayer3_wealth))

def awardScholarship(incomeList, awardTotal):
    """
    Redistributes funds from the lottery in the form of a $1 scholarship.
    Inputs: *incomeList: The list containing wealth values for the given
             income group.
            *awardTotal: The total amount of lottery funds to be rewarded
             to members of this income group.
    """
    for i in range(awardTotal):
        pick_random_recipient = random.randint(0, len(incomeList)-1)
        recipientindexed = pick_random_recipient + 1
        incomeList[pick_random_recipient] += 1
        recipient_wealth = incomeList[pick_random_recipient]        
    #    print("Player #" + str(recipientindexed) + " won the scholarship, adding to the wealth of player #" + str(recipientindexed) + ". New wealth: $" + str(recipient_wealth))
    return incomeList
def simCommunity(years, communitySize):
    """
    Simulates the movement of money between high income and low income
    communities via the Georgia lottery and scholarship system over several
    years. Half of the community is from low income backgrounds, and half from
    high income backgrounds. The resulting wealth disparity is printed as a
    message and displayed as a scatter plot indicating overall wealth per
    person per year.
    Inputs: *years: The number of years the simulation should be run.
            *communitySize: The number of people in the community.
    """

    # ---- PART 1: Populate Wealth Lists
    # Fill highIncomeList and lowIncomeList with starting wealth values.

    highIncomeList = [] 
    lowIncomeList = [] 

    for i in range(communitySize):
        highIncomeList.append(100)
        lowIncomeList.append(99)

        
    # ---- PART 2: Populate Record Lists
    # Fill highIncomeRecord and lowIncomeRecord with the starting ("year 0")
    # values from highIncomeList and lowIncomeList.


    
    highIncomeRecord = []
    lowIncomeRecord = []


    # simulation loop
    for i in range(years):

        # ---- PART 3: Play the Lottery
        # Use the simLottery() function to simulate community
        # wealth interactions.
        simLottery(highIncomeList, 40)
        simLottery(lowIncomeList, 60)
        
        
        # ---- PART 4: Award Scholarships
        # Use the awardScholarship() function to redistribute lottery funds
        # as scholarships.
        awardScholarship(highIncomeList, 70)
        awardScholarship(lowIncomeList, 30)
        # ---- PART 5: Update Record Lists
        # Update the income records every year.
        highIncomeRecord.append(highIncomeList)
        lowIncomeRecord.append(lowIncomeList)

        highIncomeList = highIncomeList.copy()
        lowIncomeList = lowIncomeList.copy()
        
#        print("Year #" + str(i) + " " + str(highIncomeRecord[i]))
#        print("Year #" + str(i) + " " + str(lowIncomeRecord[i]))         
        # ---- PART 6: Display Wealth Distribution
        # Use getDisparityMessage() to display the wealth distribution
        # every decade.

        if i % 10 == 0:
            print(getDisparityMessage(highIncomeList, lowIncomeList, i))

    # ---- PART 7: Visualize the Simulation
    # Uncomment the next line to plot the simulation.
    plotSim(highIncomeRecord, lowIncomeRecord)
# ----------------- HELPER FUNCTIONS ----------------- #
# These functions are provided for you to use.
# You do not need to change them, but feel free to explore what they do.

def plotSim(highIncomeRecord, lowIncomeRecord):
    """
    Helper function for simCommunity() to generate a scatterplot displaying
    the wealth of each person in the simulation over 8 decades. High income
    values are plotted in red. Low income values are plotted in blue.
    Inputs: *highIncomeRecord: A list of all high income wealth lists
            from each year.
            *lowIncomeRecord: A list of all low income wealth lists
             from each year.
    """
    x = np.arange(len(highIncomeRecord))

    # plot wealth records
    plotWealthRecord(x, highIncomeRecord, '#882255', '.')
    plotWealthRecord(x, lowIncomeRecord, '#44AA99', '*')

    # plot labels/legend
    plt.xlabel("Year")
    plt.ylabel("Wealth Value")
    magenta_patch = mpatches.Patch(color='#882255', label='High Income')
    teal_patch = mpatches.Patch(color='#44AA99', label='Low Income')
    plt.legend(handles=[magenta_patch, teal_patch])

    # display the plot
    plt.show()
def plotWealthRecord(x, record, markerColor, markerShape):
    """
    Helper function for plotSim(). Plots each individual wealth group.
    Inputs: *x: List of x-axis values.
            *record: The income record to be plotted.
            *markerColor: String defining the color of markers.
            *markerShape: String defining marker shape.
    """
    for i in range(len(record[0])):
        plotData = []
        for j in range(len(record)):
            plotData += [record[j][i]]
        plt.scatter(x, plotData, color=markerColor, marker=markerShape)
def simManyPlays(n):
    """
    Function to graph the total winnings of a player who plays the lottery
    n times.
    Inputs: *n: The number of times the player enters the lottery.
    """
    winnings = []
    reward = 0
    for i in range(n):
        reward += playLottery()
        winnings.append(reward)
    plt.xlabel("Number of Lottery Plays")
    plt.ylabel("Winnings")
    plt.plot(winnings)
    plt.legend()
    plt.show()

# ----------------- MAIN FUNCTION ----------------- #


def main():
    highIncomeList = [2,3,4,5,6]
    lowIncomeList = [6,5,4,3,2]
    incomeList = [2,3,4,5,6]
    awardTotal = 1
    my_list = generateLotteryNumbers()
    print ("My lottery numbers are" + str(my_list))
    lottery_list = generateLotteryNumbers()
    print ("The winning lottery numbers are " + str(lottery_list))
    matches = countMatches(my_list, lottery_list)
    print("The number of matches between my_list and lottery_list are " + str(matches))
    reward = playLottery()
    print("The reward is $" + str(reward))
    print(getDisparityMessage(highIncomeList, lowIncomeList, 1))
    simLottery(incomeList, 5)
    awardScholarship(incomeList, awardTotal)
    # Simulate 1000 plays by one preward and plot the winnings.
    simManyPlays(1000)
    # Simulate a community playing Lottery 5 with 30 people for 80 years.
    simCommunity(80, 30)
if __name__ == "__main__":
    main()


# when I run simmanyplays I typically see that the more number of times, the more earnings 
# the player gets. Until I win the lottery, then the graph looks much different. 