# RAGING DOWNLOAD (WIP)
## Implementing detailed data analysis to fighting games matches.
**Each action a player performs in a match is recorded into a dataset which can be analyzed to find trends in their play.**

_**Objectives**_
1. **Use data analysis to analyze gameplay in ways other methods, such as video analysis, cannot.**
2. **Provide conveinent gameplay analysis for new and casual players**

## Data Analysis

**SURFACE ANALYSIS** - *Data analysis that can be done with the original dataset*
- Move hit/block/whiff rates
- Throw success rate
- Jump success rate

**DEEP ANALYSIS** - *Data analysis that requires a transformation of the original dataset*
- Combos
- Meaties / Stolen Turns
- Hit Confirms

**DEEPER ANALYSIS** - *Data analysis that either requires outside data or more technology to properly implement*
- Health lost to move (e.g., total damage from fireballs) 
- Projectile throw rhythm
- Distance walked

## Data Collection
The "DvT.xlsx" dataset was collected by watching a [video of the matches](https://youtu.be/LLPUW1IAGwY) and manually recording each action. Below are the potential methods for automating the process.

**1.] OFFICIAL IMPLEMENTATION FROM DEVELOPER**
###### Action + result counter is implemented into the source code and datasets can be exported or analysis is available in-game. (For Street Fighter V, the datasets could be accessed and exported from the [CFN website](https://game.capcom.com/cfn/sfv/).
_PROS_
- Data should be guaranteed to be 100% accurate
- Should be easy to implement in source code

_CONS_
- Need to be in-game to collect data
- Requires developer support
- Won't be implemented for every fighting game (especially games that are no longer updated)

**2.] 3RD PARTY MOD OR SOFTWARE**
###### Somehow implement the same method as above by modifying game files.
_PROS_
- Data should be accurate
- Doesn't require developer support

_CONS_
- Need to be in-game to collect data
- Ease of implementation varies

**3.] VIDEO / IMAGE ANALYSIS DEEP LEARNING**
###### Same method used to manually collect the DvT dataset except done by an AI. The AI watches a video of a match and can identify the moves being used and their results.
_PROS_
- Don't need to be in-game to collect data
- Could be used to quickly provide analysis during tournament streams

_CONS_
- Can't identify moves than were counterhit on frame 1
- 100% accurate data not guranteed
- Difficult to implement


-----------------------------------------------------------------------

###### WORK IN PROGRESS
- [ ] Turn Tableau analysis
- [ ] "Deeper" Analysis on health loss from moves
- [ ] DvT dataset analysis article / report
- [ ] Deep learning prototype


