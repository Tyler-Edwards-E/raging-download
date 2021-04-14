# RAGING DOWNLOAD
## Applying data science to fighting games.
**Each action a player performs in a match is recorded into a dataset which can be analyzed to find trends in their play.**

_**Objectives**_
1. **Use data analysis to achieve deeper gameplay analysis.**
2. **Provide conveinent gameplay analysis for new and casual players**

[_**Read the article for more information**_](https://medium.com/@TyEdwardsE)
[![Ken Sprite Detection Prototype](https://user-images.githubusercontent.com/69095276/114774111-d5c5ad80-9d3d-11eb-97ee-01d5c9442c17.png)](https://medium.com/@TyEdwardsE "CLICK FOR FULL ARTICLE")


## Daigo vs. Tokido Example
Example that uses manually collected data from a video to analyze a match and prove how useful data can be in fighting games.

![Normals Comparison](https://user-images.githubusercontent.com/69095276/114776325-58e80300-9d40-11eb-9f6c-7d477ebcc63b.png)

## Sprite Detection
Using object detection to collect data from videos of fighting game matches

[![Ken Sprite Detection Prototype](https://user-images.githubusercontent.com/69095276/113636913-6bc44e80-9641-11eb-9587-1fbfd2701428.gif)](https://www.youtube.com/watch?v=3gc-V6mTFsc "CLICK FOR FULL VIDEO")

_**HOW TO USE**_

Currently the sprite detection is not extremely user friendly, but if you want to try the sprite detection on your own videos try following these steps.

1. Download the Sprite Detection folder
2. Download the yolov5 repository and place it in the Sprite Detection folder
3. Run detect.bat (Edit the filepath for the source to use your own video and not the sample)
4. Object detected images or videos will be saved to yolov5/runs/detect/exp

-----------------------------------------------------------------------

###### WORK IN PROGRESS
- [ ] Write script that translates detection output into useful data
- [ ] Recreate Ken model with more classes and better training
- [ ] Attempt model with two or more characters
- [ ] User friendly GUI for detection

