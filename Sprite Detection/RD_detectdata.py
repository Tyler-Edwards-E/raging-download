

# Tyler Edwards
# 4-11-2022
# yolov5 .txt > .csv

import os
import pandas as pd

P1_filepath = r'C:\Users\Ty\3D Objects\~RD\DETECTION\Chun93TEST\labels' # Path to yolov5 output folder
P1_keypath = r"C:\Users\Ty\3D Objects\~RD\RD-SF3S\SF3rdStrike-YARDS\chunlabels.txt"

P2_filepath = r"C:\Users\Ty\3D Objects\~RD\DETECTION\KenProtoTEST\labels" # Path to yolov5 output folder
P2_keypath = r"C:\Users\Ty\3D Objects\~RD\RD-SF3S\SF3rdStrike-YARDS\~OLD\ken-OLD.txt"


def RD_Function(filepath, keypath):

    df = pd.DataFrame(columns = ["video", "frame", "character", "action", "description", "confidence"])

    with open(keypath) as f:
        lines = f.readlines()

        i_list = list(range(0,len(lines)))
        lines2 = []
        for i in lines:
            lines2.append(i.strip())

        # if lines2[0].split("-")[0] == "KEN": # TEMPORARY FIX FOR OLD LABELS **********************************************
        #     i_list = list(range(0,len(lines)))

        keys = dict(zip(i_list, lines2))

    print()
    for file in os.listdir(filepath):
        with open(str(filepath + "/" + file)) as f:
            lines = f.readlines()

        filesplit = file.split("_")
        linesplit = lines[0].split()

        #character = lines2[0].split("-")[0]
        video = filesplit[0]
        frame = int(filesplit[1].replace(".txt", ""))

        clas = linesplit[0] # Class

        actiondesc = keys[int(clas)].split("-")
        character = actiondesc[0]
        desc = ""
        if len(actiondesc) > 2:
            desc = actiondesc[2]
        action = actiondesc[1]

        conf = linesplit[5]

        # print("VIDEO:", video)
        # print("FRAME:", frame)
        # print("CHARACTER:", character)
        # print("ACTION:", action)
        # print("DESCRIPTION:", desc)
        # print("CONFIDENCE:", conf)
        # print("--------------------------------------------------------------------")

        row = [video, frame, character, action, desc, conf]
        df.loc[len(df)] = row

    print(df)
    return df

A = RD_Function(P1_filepath, P1_keypath)
B = RD_Function(P2_filepath, P2_keypath)

C = pd.merge(A, B, on=['video',  'frame'])
C = C.sort_values(by=['frame'])

print(C)

C.to_csv('RD_proto.csv', index=False)
