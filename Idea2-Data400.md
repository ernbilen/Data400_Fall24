# Idea 2
###### Derek Chibbaro
#
#

## Idea:
My second idea for a potential project would be to expand my research that I conducted while taking Advanced Econometrics (ECON 398) this past spring. My intention is to expand on my analysis of winning percentages when the Knicks play an away game. I would like to numerically evaluate a team's effort in winning certain games based on who they play and if there are playoff implications. I can use the ranking statistics to determine which team in which season can be categorized as "playoff-bound".
### Research Question:
How does the knowledge of opponent strength and playoff implications affect a team’s performance in regular season games? Do the point differentials or other game level statistics vary across teams and years?

### Data
I created a merged data set of game level data for the New York Knicks in the last 10 seasons and added numerous ranking statistics for the opponents of each game. This data is from Basketball Reference and was downloaded via Excel spreadsheets. My cleaned data set is in Stata format, but can be uploaded into Python.

### Useful variables from the dataset
|variable | description
| :---        |    :---   |
rank | provides a numerical value of rank for each team based on one season
pointdiff | point differential of each game
LateGame | =1 if game was played after 5:00pm; =0 otherwise
Away | =1 if game was played away; =0 if home game


## Model
I can create a cutoff point for all seasons, maybe the 60th game of the season (out of 82) and compare the winning percentages and other statisitcs before and after the cutoff. I learned the Regression Discontinuity model in ECON 398, which looks at how significant a specified cutoff point is. Is there a significant "jump" at the cutoff, indicating that latter portion of the season is played differently than the earlier parts of the season?

### Implications for stakeholders
The results from my project can be used by casual basketball fans to identify any trends related to teams that are contending for playoffs or not. NBA executives could also look at the performance of teams that are out of playoff contention and determine if there should be any penalty for "purposefully" losing. This would be difficult to determine since you can't be 100% sure that a team is doing something on purpose.

### Ethical/Legal/Societal Implications
This data is available for free to anyone who wants to use it for their own research and there are no intentions of selling these results. Teams who don't perform to their best ability could drop in the standings, which would impact their chances of receiving higher draft picks in the future season. This can create an unfair advantage and a worse viewer experience if the team is only focusing on future seasons. Owners and managers wouldn't want teams to underperform because this could impact attendance ratings and hurt their financial sucess.
