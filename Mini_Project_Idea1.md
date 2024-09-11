# Mini Project - Idea 1
###### Derek Chibbaro
#
#

## Idea:
For my mini project, I'm interested in analyzing the effects of the infield shift rule that was implemented at the start of the 2023-2024 season. I'd like to see where balls were put into play and identify any trends with where the ball was hit in the field and how locations of ballparks could influence the outcomes as well. I'm thinking of creating an interactive heat map that represents where a ball was put into play. The viewer can use a drop down menu to change the field location and they can use a slider to change the year.
### Background on the rule change:
According to the MLB, "defensive teams will be required to have a minimum of four players on the infield, with at least two infielders completely on either side of second base. These restrictions are intended to increase the batting average on balls in play, to allow infielders to better showcase their athleticism and to restore more traditional outcomes on batted balls."
My intention is to analyze the difference between batted ball outcomes before and after the new shift rule was added as well as identify any correlations between the outcomes and what stadium a team was playing in.
### Research Question:
Is there a correlation between where a ball is put into play and the change of the MLB shift rule? Does the location of an MLB stadium impact a hitter's decision on where they try to hit the baseball?

### Data
The data I plan on using is from pybaseball, which pulls from Baseball Savant's website. It contains numerous game level statistics (94), and is a package that can be imported into Python.

### Useful variables from the dataset
|variable | description
| :---        |    :---   |
hit_location | Indicated by which number position
home_team | home team for a given game
events | explains what happened after each pitch
launch_speed | speed of batted ball
des | description of outcome

Note that for the years, I can select the time frame when importing the data. Other variables could be considered as well.

### Implications for stakeholders
The results from my project can be used by casual baseball fans to identify any trends related to the new shift rule. This rule can still impact the game in the future in ways we haven't experienced yet, which can make this project even more interesting in years to come.

### Ethical/Legal/Societal Implications
This data is available for free to anyone who wants to use it for their own research and there are no intentions of selling these results. Baseball fans can better understand aspects of the game that are less obvious to a casual viewer, which can help the game's fanbase as well.
