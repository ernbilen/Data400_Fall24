# Text-based game of managing a data science team, inspired by the PbD board game
# Author: Eren Bilen v02, Aug 23, 2022

import random
import time
import sys
import os

# welcome text
welcome_text = """
Welcome to Data Science: The Game!""",""" Inspired by the PbD board game, v02 by Eren Bilen - comments/feedback welcome at bilene@dickinson.edu

"""

# quick start text, if tutorial is skipped
quick_start_text = """
Jumping right into the game? Great! As a reminder, here are the keyboard commands and shortcuts:
"""
quick_start_commands = """
  yes - submits a "yes" response
  no  - submits a "no" response

When prompted for an action, you can also enter one of these
commands without using up your turn:

  status - lists the current round #, DA points, trust points
  help   - lists all the commands.
  quit   - will end the game.

You can also use these shortcuts for commands:

  'y', 'n', 's', '?', 'q'
"""

# takes the form of a list of strings in order to insert pauses in between text
game_description = """
You are in charge of the data science team at the BigApple Software Company.""",""" You are working on a new mobile app called MyFitnessApp.""","""Your app enables daily weight monitoring by tracking its users' physical activities. It also allows users to enter their meals each day which then the app uses to provide meal suggestions based on calorie and vitamin intake with the help of a machine learning algorithm.""","""
\nObjective of the Game:🤨""" , """ Decide and maintain a privacy policy for your company, while providing a cutting edge experience for its users.""",""" What data will you collect, and who will you share it with?""","""
Your decisions will cost you or gain you resources, resulting in a winning or losing app development strategy."""

help_text = """
You have two resources that you need to keep track of: Data Analytics (DA) points, and user trust. You begin with 25 DA points and 25 user trust points.
DA points are like money💵 DA points are precious because it helps you build🔨 more, bigger, and better data analysis products. \nUser trust represents your customer base😇 User trust is precious because
it helps ensure customers want to use your application. You will spend these
resources, or earn more of them, depending on the choices you make in your policy. Try not to let your DA points and user trust fall below 15. If you complete the game with less than 15 points each, you lose the game. If any of these reach to 0, you automatically lose the game!😬

In each turn, you will be given choices that will affect your balance of DA points and user trust. When you’ve completed your decisions, the game will draw an event card at random. Event cards represent the many things in design you can't see coming. You'll be presented with new opportunities and challenges that you'll have to make decisions about, and you may gain or lose resources depending on the decisions you've already made. After the card is drawn and its effect is applied, your turn is completed. Keyboard commands for the game are:

  yes - submits a "yes" response
  no  - submits a "no" response

When prompted for an action, you can also enter one of these
commands without using up your turn:

  status - lists the current round #, DA points, trust points
  help   - lists all the commands.
  quit   - will end the game.

You can also use these shortcuts for commands:

  'y', 'n', 's', '?', 'q'

"""

good_luck_text = "Good luck, and see you with a sucessful product!"

# Model -- value data from the game board

da_benefit = [[-2,2,2],[4,2,-3],[2,2,2],[-3,3,3],[2,4,2],[5,2,-3],[2,4,1],[-3,2,3],[2,2,2],[5,2,-3],[2,4,2],[-3,3,4]]
da_cost = [[0,-2,-2],[-3,-2,-3],[-2,-2,0],[-3,-3,-5],[-1,-3,-2],[-4,-2,-3],[-2,-3,0],[-3,-2,-3],[-2,-2,-2],[-4,-2,-3],[-2,-4,-2],[-3,-2,-4]]
trust_cost = [[0,-2,-1],[-4,0,0],[-1,-4,0],[-5,-3,-4],[-1,-3,-2],[-6,-3,-3],[-2,-3,-2],[-3,-3,-4],[-2,-2,-1],[-5,-2,-3],[-1,-4,-2],[-2,-3,-4]]
trust_benefit = [[2,2,1],[3,1,2],[1,2,2],[2,3,3],[1,2,1],[4,2,2],[1,2,2],[2,2,3],[2,2,1],[3,2,3],[1,4,1],[3,3,4]]


collect_text = [
# first index is for round #
# round 1
["""
Here is the first round!🚀
Collecting demographic data. Maintain your service by asking users demographics questions?
\nIf you decide yes: you will get {} DA points (because keeping service updated requires development time) and {} trust points.\n If you decide no: you will get {} DA points and {} trust points (because not to collect demographic data to provide service gains your team two user trust- users appreciate that you’re not asking probing questions about their social categories or status).
""".format(da_benefit[0][0],trust_cost[0][0],da_cost[0][0],trust_benefit[0][0]), """
Ask demographics questions to be used for marketing? \nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[0][1],trust_cost[0][1],da_cost[0][1],trust_benefit[0][1]), """
Ask demographics questions to be included on users' profiles?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[0][2],trust_cost[0][2],da_cost[0][2],trust_benefit[0][2])],

# round 2
["""
Ok. Here is turn 2!🗿
Sharing demographic data. With other corps? \nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[1][0],trust_cost[1][0],da_cost[1][0],trust_benefit[1][0]), """
With academic researchers?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[1][1],trust_cost[1][1],da_cost[1][1],trust_benefit[1][1]), """
With government on request?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[1][2],trust_cost[1][2],da_cost[1][2],trust_benefit[1][2])],

# round 3
["""
Here is turn 3!🧗‍♀️
Collecting health information. For user profiles? \nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[2][0],trust_cost[2][0],da_cost[2][0],trust_benefit[2][0]), """
For marketing?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[2][1],trust_cost[2][1],da_cost[2][1],trust_benefit[2][1]), """
To maintain service?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[2][2],trust_cost[2][2],da_cost[2][2],trust_benefit[2][2])],

# round 4
["""
Get ready for turn 4!🎯
Sharing health information. With government on request? \nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[3][0],trust_cost[3][0],da_cost[3][0],trust_benefit[3][0]), """
With academic researchers?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[3][1],trust_cost[3][1],da_cost[3][1],trust_benefit[3][1]), """
With other corps?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[3][2],trust_cost[3][2],da_cost[3][2],trust_benefit[3][2])],

# round 5
["""
Ready for turn 5?🎥
Collecting purchasing information. To maintain service? \nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[4][0],trust_cost[4][0],da_cost[4][0],trust_benefit[4][0]), """
For marketing?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[4][1],trust_cost[4][1],da_cost[4][1],trust_benefit[4][1]), """
For user profiles?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[4][2],trust_cost[4][2],da_cost[4][2],trust_benefit[4][2])],

# round 6
["""
Now, turn 6:🗄
Sharing purchasing information. With other corps? \nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[5][0],trust_cost[5][0],da_cost[5][0],trust_benefit[5][0]), """
With academic researchers?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[5][1],trust_cost[5][1],da_cost[5][1],trust_benefit[5][1]), """
With government on request?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[5][2],trust_cost[5][2],da_cost[5][2],trust_benefit[5][2])],

# round 7
["""
Here is turn 7🛎
Collecting contact lists. For user profiles?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[6][0],trust_cost[6][0],da_cost[6][0],trust_benefit[6][0]), """
For marketing?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[6][1],trust_cost[6][1],da_cost[6][1],trust_benefit[6][1]), """
To maintain service?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[6][2],trust_cost[6][2],da_cost[6][2],trust_benefit[6][2])],

# round 8
["""
Let's get ready for round 8!🎱
Sharing contact lists. With government on request?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[7][0],trust_cost[7][0],da_cost[7][0],trust_benefit[7][0]), """
With academic researchers?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[7][1],trust_cost[7][1],da_cost[7][1],trust_benefit[7][1]), """
With other corps?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[7][2],trust_cost[7][2],da_cost[7][2],trust_benefit[7][2])],

# round 9
["""
Here is turn 9:🚦
Collecting site activity. To maintain service?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[8][0],trust_cost[8][0],da_cost[8][0],trust_benefit[8][0]), """
For marketing?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[8][1],trust_cost[8][1],da_cost[8][1],trust_benefit[8][1]), """
For user profiles?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[8][2],trust_cost[8][2],da_cost[8][2],trust_benefit[8][2])],

# round 10
["""
Now, turn 10:✈️
Sharing site activity. With other corps?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[9][0],trust_cost[9][0],da_cost[9][0],trust_benefit[9][0]), """
With academic researchers?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[9][1],trust_cost[9][1],da_cost[9][1],trust_benefit[9][1]), """
With government on request?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[9][2],trust_cost[9][2],da_cost[9][2],trust_benefit[9][2])],

# round 11
["""
Here is turn 11:🚘
Collecting location data. For user profiles?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[10][0],trust_cost[10][0],da_cost[10][0],trust_benefit[10][0]), """
For marketing?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[10][1],trust_cost[10][1],da_cost[10][1],trust_benefit[10][1]), """
To maintain service?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[10][2],trust_cost[10][2],da_cost[10][2],trust_benefit[10][2])],

# round 12
["""
Here is the last turn, turn 12!🗺
Sharing location data. With government on request?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[11][0],trust_cost[11][0],da_cost[11][0],trust_benefit[11][0]), """
With academic researchers?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[11][1],trust_cost[11][1],da_cost[11][1],trust_benefit[11][1]), """
With other corps?\nIf you decide yes: you will get {} DA points and {} trust points.
If you decide no: you will get {} DA points and {} trust points.
""".format(da_benefit[11][2],trust_cost[11][2],da_cost[11][2],trust_benefit[11][2])]
]

#creating functions that prints out a string one character at a time with X seconds between each character. to be used for printing the title and the end messages.
def titleprint(string):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.06)

def slowprint(string):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.03)

def slowerprint(string):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)
def fastprint(string):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.02)

# parameter initialization

da=25
trust=25
round=0
collected_site=0
collected_health=0
collected_location=0
collected_contact=0
collected_demographics=0
collected_purchasing=0
shared_site=0
shared_health=0
shared_location=0
shared_contact=0
shared_demographics=0
shared_purchasing=0


# game cards below

def card0():
    global da, trust, shared_health, shared_contact,shared_site
    print("""
       _______________________________________
      |                                       |
      |  Regulatory Changes!                  |
      |                                       |
      |    The European Union passes          |
      |    sweeping new privacy regulations.  |
      |                                       |
      |                                       |
      |   Past decision: You lose 3 DA        |
      |   points if you've shared any of the  |
      |   following with anyone:              |
      |   health information, contact lists,  |
      |   site activity                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if (shared_health >0) | (shared_contact >0)| (shared_site >0):
        da = da-3
        print('Past decision was applied to you.')
    print('Past decision does not apply to you.')
    handle_status()

def card1():
    global da, trust, da_benefit, shared_contact
    print("""
       _______________________________________
      |                                       |
      |  Guidelines Change!                   |
      |                                       |
      |    The App Store released new, more   |
      |    restrictive app review guidelines  |
      |                                       |
      |                                       |
      |   Past decision: You lose 3 DA        |
      |   points if you've shared contact     |
      |   lists with anyone                   |
      |             -- OR --                  |
      |   Future condition: Sharing contact   |
      |   with anyone will cost -5 DA points  |
      |   from now on.                        |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if shared_contact>0:
        da = da-3
        print('Past decision was applied to you.')
    else:
        da_benefit[7]=[-5,-5,-5]
        print('Past decision does not apply to you, so future condition is applied.')
    handle_status()

def card2():
    global da
    print("""
       _______________________________________
      |                                       |
      |  Crunch Time!                         |
      |                                       |
      |    Data analysts are working overtime |
      |    to meet deadlines. Sad data        |
      |    analysts, happy bottom line.       |
      |                                       |
      |   You have gained 1 DA point.         |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    da = da +1
    handle_status()
    print('Points updated!')

def card3():
    global da
    print("""
           _______________________________________
          |                                       |
          |  New investment!                      |
          |                                       |
          |    Your idea has sparkled a lot of    |
          |    interest on Wall Street.           |
          |                                       |
          |   You have gained 2 DA points.        |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |_______________________________________|

          """)
    da = da+2
    handle_status()
    print('Points updated!')

def card4():
    global da
    print("""
           _______________________________________
          |                                       |
          |  Venture capital!                     |
          |                                       |
          |    Your idea has sparkled a lot of    |
          |    interest in Silicon Valley         |
          |                                       |
          |   You have gained 2 DA points.        |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |_______________________________________|

          """)
    da = da+2
    handle_status()
    print('Points updated!')

def card5():
    global da, trust, da_benefit, shared_health
    print("""
       _______________________________________
      |                                       |
      |  IHI Partnership                      |
      |                                       |
      |    International Health Insurance     |
      |    wants to buy health information    |
      |    about its customers. In exchange,  |
      |    they will promote your application.|
      |                                       |
      |   Past decision: You gain 2 DA        |
      |   points if you've shared health      |
      |   information with others             |
      |             -- OR --                  |
      |   Future condition: Sharing health    |
      |   information with other companies    |
      |   now earns you 5 DA points.          |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if shared_health>0:
        da = da+2
        print('Past decision was applied to you.')
    else:
        da_benefit[3][2]=5
        print('Past decision does not apply to you, so future condition is applied.')
    handle_status()

def card6():
    global da, trust, da_benefit, shared_purchasing
    print("""
       _______________________________________
      |                                       |
      |  Amazon Partnership                   |
      |                                       |
      |    Amazon wants to learn more about   |
      |    your users by accessing their      |
      |    purchasing information.            |
      |                                       |
      |   Past decision: You gain 2 DA        |
      |   points if you've shared purchasing  |
      |   information with others             |
      |             -- OR --                  |
      |   Future condition: Sharing purchasing|
      |   information with other companies    |
      |   now earns you 7 DA points.          |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if shared_purchasing>0:
        da = da+2
        print('Past decision was applied to you.')
    else:
        da_benefit[5][0]=7
        print('Past decision does not apply to you, so future condition is applied.')
    handle_status()


def card7():
    global da, trust, da_benefit, shared_contact
    print("""
       _______________________________________
      |                                       |
      |  ISA Wants to Partner                 |
      |                                       |
      |    Intelligent Sheep Analytics will   |
      |    pay you for access to your users'  |
      |    contacts lists.                    |
      |                                       |
      |   Past decision: You gain 2 DA        |
      |   points if you've shared contact list|
      |   information with others             |
      |             -- OR --                  |
      |   Future condition: Sharing contact   |
      |   information with other companies    |
      |   now earns you 5 DA points.          |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if shared_contact>0:
        da = da+2
        print('Past decision was applied to you.')
    else:
        da_benefit[7][2]=5
        print('Past decision does not apply to you, so future condition is applied.')
    handle_status()

def card8():
    global da, trust, da_benefit
    print("""
       _______________________________________
      |                                       |
      |  Targeted Advertising                 |
      |                                       |
      |    OmniCom wants to target their ads  |
      |    based on your users' location.     |
      |                                       |
      |                                       |
      |   Future condition: Sharing location  |
      |   information with other companies    |
      |   now earns you 6 DA points.          |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    da_benefit[11][2]=6
    handle_status()

def card9():
    global da, trust, da_benefit, collected_location
    print("""
       _______________________________________
      |                                       |
      |  Location Tracking for Health         |
      |                                       |
      |    Management wants location data to  |
      |    calculate users' physical activity.|
      |                                       |
      |                                       |
      |   Past decision: You gain 1 DA        |
      |   point if you've shared collected    |
      |   location data for any reason.       |
      |             -- OR --                  |
      |   Future condition: Collecting        |
      |   location data to maintain service   |
      |   now earns you 3 DA points.          |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if collected_location>0:
        da = da+1
        print('Past decision was applied to you.')
    else:
        da_benefit[10][2]=3
        print('Past decision does not apply to you, so future condition is applied.')
    handle_status()

def card10():
    global da, trust, da_benefit, collected_site
    print("""
       _______________________________________
      |                                       |
      |  Site Activity                        |
      |                                       |
      |    Management wants build new features|
      |    for the most active users based    |
      |    on their site activity.            |
      |                                       |
      |   Past decision: You gain 1 DA        |
      |   point if you've collected           |
      |   site activity for any reason.       |
      |             -- OR --                  |
      |   Future condition: Collecting        |
      |   site activity for user profiles     |
      |   now earns you 3 DA points.          |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if collected_site>0:
        da = da+1
        print('Past decision was applied to you.')
    else:
        da_benefit[8][2]=3
        print('Past decision does not apply to you, so future condition is applied.')
    handle_status()

def card11():
    global da, trust, da_benefit, collected_contact
    print("""
       _______________________________________
      |                                       |
      |  Contact info                         |
      |                                       |
      |    Management thinks collecting user  |
      |    contact lists can encourage        |
      |    users to share the app with their  |
      |    friends.                           |
      |                                       |
      |   Past decision: You gain 1 DA        |
      |   point if you've collected           |
      |   contact lists for any reason.       |
      |             -- OR --                  |
      |   Future condition: Collecting        |
      |   contact lists to maintain service   |
      |   now earns you 3 DA points.          |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if collected_site>0:
        da = da+1
        print('Past decision was applied to you.')
    else:
        da_benefit[6][2]=3
        print('Past decision does not apply to you, so future condition is applied.')
    handle_status()

def card12():
    global da, trust, collected_demographics
    print("""
       _______________________________________
      |                                       |
      |  Demo info                            |
      |                                       |
      |    The data team wants to collect     |
      |    demographic info to better         |
      |    understand the users.              |
      |                                       |
      |   Past decision: You gain 1 DA        |
      |   point if you've collected           |
      |   demographic info for any reason.    |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if collected_demographics>0:
        da = da+1
        print('Past decision was applied to you.')
    elif collected_demographics==0:
        print('Past decision does not apply to you, so no points have been added.')
    handle_status()

def card13():
    global da, trust, da_benefit, collected_contact, round
    print("""
       _______________________________________
      |                                       |
      |  Dogfood                              |
      |                                       |
      |    The internal testing team uses     |
      |    the app for a week and gets        |
      |    irritated that they have to give   |
      |    permission for their contact list  |
      |    to be collected.                   |
      |                                       |
      |   Past decision: You gain 3 user      |
      |   trust if you've decided NOT to      |
      |   collect contact lists for any       |
      |   reason.                             |
      |             -- OR --                  |
      |   Future condition: Deciding not to   |
      |   collect contact lists for providing |
      |   service and maintaining app now     |
      |   earns you 3 extra DA points.        |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if (round>=6) & (collected_contact==0):
        trust = trust+3
        print('Past decision was applied to you.')
    else:
        da_benefit[6][0]=5
        da_benefit[6][2]=4
        print('Past decision does not apply to you, so future condition is applied.')
    handle_status()

def card14():
    global da, trust, da_benefit, collected_site, round
    print("""
       _______________________________________
      |                                       |
      |  Reviews Are In                       |
      |                                       |
      |    Reviewers want to know: do you     |
      |    really need to track site activity?|
      |                                       |
      |   Past decision: You gain 3 user      |
      |   trust if you've decided NOT to      |
      |   collect site activity for           |
      |   any reason.                         |
      |             -- OR --                  |
      |   Future condition: Deciding not to   |
      |   collect site activity for marketing |
      |   now earns you 3 extra user trust.   |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if (round>=8) & (collected_site==0):
        trust = trust+3
        print('Past decision was applied to you.')
    else:
        da_benefit[8][1]=5
        print('Past decision does not apply to you, so future condition is applied.')
    handle_status()

def card15():
    global da, trust, da_benefit, collected_demographics, round
    print("""
       _______________________________________
      |                                       |
      |  Polling Numbers                      |
      |                                       |
      |    3 out of 5 users agree that you    |
      |    shouldn't have to provide          |
      |    demographic info to use the app.   |
      |                                       |
      |   Past decision: You gain 3 user      |
      |   trust if you've decided NOT to      |
      |   collect demographic info for any    |
      |   reason.                             |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if (round>=0) & (collected_demographics==0):
        trust = trust+3
        print('Past decision was applied to you.')
    handle_status()

def card16():
    global da, trust, shared_site, shared_health, shared_contact, shared_location, shared_demographics, shared_purchasing
    print("""
       _______________________________________
      |                                       |
      |  Angry emails                         |
      |                                       |
      |    Many users wrote to say they       |
      |    CANNOT EVEN with your sharing      |
      |    of their data.                     |
      |                                       |
      |   Past decision: You lose 2 user      |
      |   trust if you've decided to share    |
      |   more than 2 types of data with      |
      |   other parties.                      |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if shared_site + shared_health + shared_contact + shared_location + shared_demographics + shared_purchasing >2:
        trust = trust-2
        print('Past decision was applied to you.')
    handle_status()

def card17():
    global da, trust, shared_site, shared_health, shared_contact, shared_location, shared_demographics, shared_purchasing
    print("""
       _______________________________________
      |                                       |
      |  Best App Policies Ever               |
      |                                       |
      |    Your restraint of sharing data has |
      |    paid off.                          |
      |                                       |
      |   Past decision: You gain 2 user      |
      |   trust and 2 DA points if you        |
      |   have NOT shared any data with other |
      |   parties.                            |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |_______________________________________|

      """)
    if shared_site + shared_health + shared_contact + shared_location + shared_demographics + shared_purchasing ==0:
        trust = trust+2
        print('Past decision was applied to you.')
    handle_status()




# create a list of functions, to be randomized
cards = [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15,card16,card17]


# next round update
def next_round():
  global round
  round=round+1

# collect choices from the player
def collect_prompt(i):
    global da, trust, round
    print(collect_text[round][i])

# update with yes answer
def handle_yes(i):
    global da, trust, round, collected_demographics,shared_demographics,collected_health,shared_health,collected_purchasing,shared_purchasing,collected_contact,shared_contact,collected_site,shared_site,collected_location,shared_location
    da = da + da_benefit[round][i]
    trust = trust + trust_cost[round][i]
    if i==2: # remember each turn has 0,1,2 decisions
        next_round()
    if round ==0:
        collected_demographics += 1
    elif round==1:
        shared_demographics+=1
    elif round==2:
        collected_health+=1
    elif round==3:
        shared_health+=1
    elif round==4:
        collected_purchasing+=1
    elif round==5:
        shared_purchasing+=1
    elif round==6:
        collected_contact+=1
    elif round==7:
        shared_contact+=1
    elif round==8:
        collected_site+=1
    elif round==9:
        shared_site+=1
    elif round==10:
        collected_location+=1
    elif round==11:
        shared_location+=1

# update with no answer
def handle_no(i):
    global da, trust, round
    da = da + da_cost[round][i]
    trust = trust + trust_benefit[round][i]
    if i==2:
        next_round()





#name:handle_status()
#description:prints the status of the player
#input: round, da, trust
#returns: none
def handle_status():
	print(
  ''' \n      Status
  ---------------
  # of rounds: {}
  DA points: {}
  Trust points: {}
  ---------------
  '''.format(round,da,trust))


#name: handle_help()
#description: prints the help text
#input: none
#returns: none
def handle_help():
	print(help_text)


#name:handle_quit()
#description: ends the game
#input: playing
#returns: updated playing
def handle_quit():
  global playing
  print("Goodbye. Thank you for playing!")
  playing=False


#name:handle_invalid_input()
#description: prints invalid input if no valid command is put in.
#input: response
#returns: none
def handle_invalid_input(response):
    print("Invalid response. Please try again.")

#name:game_is_over()
# description: Inspects the flow and determines if the game has ended for any reason (e.g.
# player is out of da or trust points, or the game has reached to max rounds.
#input: round, trust, da, user input
# Returns: True if game is over.
def game_is_over():
  if (round==12) or (trust<=0) or (da<=0) or (action == 'quit' or action == 'q'):
    return True


# game outcome conditions
def belowed_but_outdated():
	if (da<15) & (trust>=25) & (da>0) & (trust>0) & (round==12):
	  return True
def bleeding_edge_bleeding_users():
	if (da>=25) & (trust <15) & (da>0) & (trust>0) & (round==12):
	  return True
def middle_of_the_road():
	if ((da<25) & (da>=15)) & (da>0) & (trust>0) | ((trust<25) & (trust >=15) & (da>0) & (trust>0)) & (round==12):
	  return True
def total_victory():
	if (da>=25) & (trust>=25) & (round==12):
	  return True

#name: loss_report()
#description: Prints reason the player has lost.
#input: da, trust, action
# Returns:none
def loss_report():
	if da <= 0:
		print("You lost because you have \033[4mno DA points!\033[0m\nTry again?")
	elif trust <= 0:
		print("You lost because you have \033[4mno trust points!\033[0m\nTry again?")
	elif action == "quit" or action == "q":
		print("You lost because you quit.")
	else:
		print()

# print welcome text
for i in range(len(welcome_text)):
    slowprint(welcome_text[i])
    time.sleep(1.7)
# skip tutorial?
while True:
    skip_tutorial = input("\nWould you like to skip tutorial? (y/n)")
    if skip_tutorial == "yes" or skip_tutorial == "y":
        slowprint(quick_start_text)
        print(quick_start_commands)
        break
    elif skip_tutorial == "no" or skip_tutorial == "n":
        ## prints the game description text with pauses in between
        for i in range(len(game_description)):
            slowprint(game_description[i])
            if (i==0)|(i==2)| (i==4) | (i ==5) | (i==6) | (i==7):
                time.sleep(1.7)
            else:
                input(f" (Press enter to continue.)").lower()
        slowerprint(help_text)
        break
    else:
        handle_invalid_input(skip_tutorial)
# next set of texts
slowerprint(good_luck_text)

# collect player name
player_name = input("\nWhat is your name, player?")
slowprint('Nice name!')
time.sleep(1)
input(f" (Press enter to start the game.)").lower()
#############
# loading bar to make it more fun!
import sys
def progressbar(it, prefix="", size=60, out=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count),
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

import time
for i in progressbar(range(100), "Loading: ", 40):
    time.sleep(0.015)
################

# This is the main execution of the game
playing = True
while playing:
  print()
  i = 0
  while i<3: # for 3 sub rounds, while required for invalid player input
      collect_prompt(i)
      action = input("Choose an action, {0} -->".format(player_name)).lower()
      if action == "yes" or action == "y":
        handle_yes(i)
      elif action == "no" or action == "n":
        handle_no(i)
      elif action == "help" or action == "?":
        handle_help()
        i -= 1
      elif action == "status" or action == "s":
        handle_status()
        i -= 1
      elif action == "quit" or action == "q":
        handle_quit()
        break
      else:
        handle_invalid_input(action)
        i -= 1
      if game_is_over():
        playing = False
      i +=1
  if i ==3:
      # proceed to drawing an event card at the end of 3rd sub round
      print('Your choices are recorded. Now you will receive an event card.')
      input(f" (Press enter to receive an event card.)  ").lower()
      # loading bar for event card
      for i in progressbar(range(100), "Drawing an event card: ", 40):
          time.sleep(0.015)
      # draw a random card function
      random.choice(cards)()
      input(f" (Your turn is completed. Press enter to begin next turn.)").lower()

# game outcome prompts
if belowed_but_outdated():
	slowprint('\n\nCongratulations you made it to the end!🎉 Your product is "belowed, but outdated"💾 Thanks for playing. Good bye!')
	handle_status()
elif bleeding_edge_bleeding_users():
	slowprint('\n\nCongratulations you made it to the end!🎉 Your product suffers from "bleeding edge with bleeding users"💎💰 Thanks for playing. Good bye!')
	handle_status()
elif middle_of_the_road():
	slowprint('\n\nCongratulations you made it to the end!🎉 Your product is "middle of the road"🔧 Thanks for playing. Good bye!')
	handle_status()
elif total_victory():
	slowprint('\n\nCongratulations you made it to the end!🎉 Your product achieved "total victory" and became the most downloaded fitness app of all time. Well played! Thanks for playing. Good bye!')
	handle_status()
else:
	print("\n\nAlas! You lose. Try again?")
	handle_status()
	loss_report()
