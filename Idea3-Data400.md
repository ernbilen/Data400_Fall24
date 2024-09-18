# Idea 3
###### Derek Chibbaro
#
#

## Idea:
My third idea for a potential project would be to analyze Pokemon Go statistics for individual pokemon. I can look at the attack, defense, and stamina metrics as well as the type of pokemon to see if there are correlations between these statistics.
### Research Question:
Is there a correlation between the attack, defense, or stamina and the combat power associated with each Pokemon? How does the type of pokemon (ex: normal, grass, electric, dark and ghost, etc.) impact the accuracy of the CP prediction? Do certain types provide more of an advantage than others?

### Data
I found a Pokemon Go stats data set in the form of CSV which includes 721 Pokemon, including their name, first and secondary type, and basic stats: hitpoints (HP), Attack, Defense, Stamina and Total Stats. The data was scraped from a Pokemon Go game info website and was minimally edited.

### Useful variables from the dataset
|variable | description
| :---        |    :---   |
Max CP | Max Combat Points of Pokemon
Type 1 | primary type of Pokemon
Type 2 | secondary type of Pokemon (if applicable)
Is Legendary | True or False
Stamina | stamina stat of Pokemon
Attack | attack stat of Pokemon
Defense | defense stat of Pokemon


## Model
I can use a regression analysis to predict a Pokemon's combat power by using other statistics like stamina, attack, and defense. It would be interesting to see how the model changes if the type of pokemon is known and if one type is generally predicted to have a lower combat power than another.

### Implications for stakeholders
The results from my project can be used by the developers of Pokemon Go to see how balanced certain aspects of the game are in comparison to the overall strenght of pokemon. This can allow them to adjust max combat powers if there is one type that is too strong over another. A Pokemon Go player can use these results to identify strategies in their gameplay.

### Ethical/Legal/Societal Implications
This data is available for free to anyone who wants to use it for their own research and there are no intentions of selling these results. Pokemon Go players can use this information to predict their own pokemon's effectiveness against others. They can also use this knowledge when trading with others in the game. Developers of the game can create new items for purchase that could impact the Pokemon's stats and balance the game more effectively.
