# 00 - Proof of Concept
## Using manually collected data to explore its potential applications.

### [_**More details in the article.**_](https://medium.com/@TyEdwardz/raging-download-a3ff6fcc42cb)

### Data
_Data was collected from a video of an online Street Fighter 5 matches between top Japanese players Daigo Umehara and Tokido. The video has since been deleted, 
but the data was collected by pausing the video anytime a player performed an action and manually recording it into the spreadsheet. (Basic movements like walking and crouching were excluded.)_

**Dataset** | **Description** |
--- | --- | 
DvT.xlsx | Master dataset that cleans up DvT(Raw).xlsx and adds sheets showing who won each game/round| 
DvT(Raw).xlsx | Raw copy of the manually recorded data from the video | 
DvT-Combos.xlsx | Output from DvT-ComboTransform.R that shows the frequency of combos used in the match.  | 
DvT-Turns.xlsx |  Output from DvT-TurnTransform.R that shows the frequency of "turns" lost/won after actions and also block strings. | 
BoomDamage.xlsx | Output from RoundAnalysis.R thats shows the amount of damage taken from Guile's (Daigo) *Sonic Boom* in each round. | 

### Scripts
_R scripts used to clean and aggregate data for visualizations_
**Script** | **Description** |
--- | --- | 
DvT-ComboTransoform.R | ...|
DvT-RoundAnalysis.R | ...|
DvT-TurnTransoform.R | ...|


### Visuals
_Visualizations ..._
**Visual** | **Description** |
--- | --- | 
DvT - Action + Result Visuals.pdf | ...|
DvT - Combo Visuals.pdf | ...|
DvT - Round Visuals.pdf | ...|
DvT – Turn Visualizations.pdf | ...|
