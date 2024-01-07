import os
import pandas as pd
import re

DIR = "Trt_TEOS — kopia/Medium TEOS"
INPUT = "FeTrz_Trt_medium_FC_FH.rso"
OUTPUT = ""
COLS = [2, 3, 4, 6] # columns indexed from 0
HEADERS = ["Field (Oe)", "Temperature (K)", "Long Moment (emu)", "Long Offset (cm)"]


def get_mass():
    filename = os.path.join(DIR, INPUT + ".dat")
    
    with open(filename, "r") as f:
        text = f.read()

    # Define a regular expression pattern to match the weight value
    pattern = re.compile(r"WEIGHT, (\d+\.\d+)", re.IGNORECASE)
    
    # Use re.search to find the match in the text
    match = pattern.search(text)

    if match:
        # Extract the weight value from the matched group
        weight = float(match.group(1))
        return weight
    else:
        raise Exception("Pattern not found in the text")




def extract_dat():
    filename = os.path.join(DIR, INPUT + ".dat")
    with open(filename, "r") as f:
        lines = f.readlines()[31:]
        data = {}

        for h in HEADERS:
            data[h] = []
        for line in lines:
            items = line.split(',')
            for c, h in zip(COLS, HEADERS):
                data[h].append(items[c])
    df = pd.DataFrame(data)
    output = OUTPUT if OUTPUT else INPUT
    df.to_csv(os.path.join(DIR, output + ".csv"), index=False)



get_mass()
extract_dat()







