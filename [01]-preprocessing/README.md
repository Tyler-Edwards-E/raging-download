# 01 - Preprocessing
## Preparing image datasets for object detection training with [YARDS](https://github.com/faimSD/yards)

_To train models on character movesets, you need to first create a large image dataset with each move in each image labeled. This is done automatically by creating folders for each moves' animations and running [YARDS (YOLO Artificial Retro-game Data Synthesizer
](https://github.com/faimSD/yards). YARDS will randomly take images for the moveset folders and paste them onto the stage backgrounds and automatically label them, creating a "synthetic" image dataset that resembles gameplay and can be used for training._ 


![SF3rdStrike-20](https://github.com/user-attachments/assets/e061cd74-411a-4caa-a9aa-6f2bdf71a2b7)
![SF3rdStrike-23](https://github.com/user-attachments/assets/f6f8b4e5-3fcc-46c6-970b-97a9ae034293)

### Process
1. Obtain the necessary character sprites & backgrounds (`ken-sprites` & `stages` folders)
2. Manually split the frames of the animations into folders for each move (`ken-sprites`)
3. Create a labelmap text file by going to command prompt, navigating to the sprites folder (`ken-sprites`), and enter `dir /b > labels.txt`. Open the text file, remove the filename from the list, save the file, and remove it from the sprites folder.
4. Paste the list from the labelmap into the `RD Class Template.xlsx` to simplify the formatting for the .YAML files
5. Run `sprite_transform.py` (Will create `ken-sprites-shift` folder)
6. Create config.yaml file (`ken-config.yaml`) and edit the parameters as needed (See [YARDS documentation](https://github.com/faimSD/yards))
7. Run YARDS command on that config file (`yards command.bat`, creates `ken-example` folder)
8. Run `pngtojpg.py` (Creates `train-jpg` and `val-jpg` folders inside `ken-example`)
9. Delete the current `train` and `val` folders
10. Rename `train-jpg` and `val-jpg` to "train" and "val" respectively
11. Create a data.yaml file (`ken-data.yaml`) if you haven't already and change `nc` to be the number of classes/moves you're training
12. Zip the folder (`ken-example`)
13. Move onto training =]

___

**Script** | **Description** |
--- | --- | 
`sprite_transform.py` | Takes the raw sprites from a game, trims the white space, and creates color shifted copies. Can also resize sprites if necessary| 
`RD Class Template.xlsx` | Workbook used to keep track of class lists and make formatting for .YAML files easier | 
`yards.bat` | Simple batch script used to run YARDS and generate synthetic data | 
`pngtojpg.py` | Converts the .png images generated by YARDS into smaller .jpg files | 
`hueshift.py` | Contains color shift functions imported into `sprite_transform.py`. Just keep in same folder as `sprite_transform.py`  | 
