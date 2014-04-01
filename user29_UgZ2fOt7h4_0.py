# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    list={"ock":0,
        "pock":1, 
        "aper":2,
        "izard":3,
        "cissors":4}
  
    if name[1:] in list:
        return list[name[1:]]


def number_to_name(number):
    list=	{0:"rock",
            1:"Spock" ,
            2:"paper",
            3:"lizard",
            4:"scissors"}
    if number in list:
        return list[number]


def rpsls(player_choice): 
    
    print "Player chooses "+player_choice
    comprand=random.randrange(0,5)
    print "Computer chooses "+number_to_name(comprand)
    
    if name_to_number(player_choice)>comprand:
        print "Player wins!"
    if name_to_number(player_choice)<comprand:
        print "Computer wins!"
    if name_to_number(player_choice)==comprand:
        print "Player and computer tie!"
    
    print ""
    
    # delete the follwing pass statement and fill in your code below
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

"""Player chooses rock
Computer chooses scissors
Player wins!"""

