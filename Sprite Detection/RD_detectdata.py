

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

    return df

A = RD_Function(P1_filepath, P1_keypath)
B = RD_Function(P2_filepath, P2_keypath)
A = A.sort_values(by=['frame'])
B = B.sort_values(by=['frame'])

C = pd.merge(A, B, on=['video',  'frame'])
C = C.sort_values(by=['frame'])
C.to_csv('RD_proto.csv', index=False)

# ------------------------------------------ ACTION MERGING ---------------------------------------------------------------

def action_merge(df):
    new_df = pd.DataFrame(columns = ["startup_frame", "ending_frame", "total_frames", "character", "action"])
    prev_act = df["action"].iloc[0]
    firstframe = 1
    lastframe = ""
    duration = 0
    count = 0

    for index, row in df.iterrows():
        if(prev_act != row["action"] or count == len(df) - 1): # If previous action is different from current, stop tracking current move
            totalframe = lastframe - firstframe
            if duration == 0: # Only appears for one frame
                firstframe = lastframe
                totalframe = 1
            new_row = {"startup_frame": firstframe, "ending_frame": lastframe, "total_frames": totalframe,  "character": row["character"],  "action": prev_act}
            new_df.loc[len(new_df)] = new_row

            # print(firstframe, [firstframe, lastframe], prev_act, duration)
            # print("----------------------------------")

            # Reset for next move
            prev_act = row["action"]
            firstframe = row["frame"]
            duration = 0
        elif prev_act == row["action"]: # If previous action is the same
            lastframe = row["frame"]
            duration = duration + 1
        count = count + 1
    return new_df

A2 = action_merge(A)
B2 = action_merge(B)
C2 = pd.merge(A2, B2, on = "startup_frame", how = "outer")
C2 = C2.sort_values(by = ["startup_frame"])
C2.to_csv('RD_prod2.csv', index=False)
