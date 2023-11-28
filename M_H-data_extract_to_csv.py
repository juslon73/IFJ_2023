import os
import pandas as pd
DIR = "STO"
INPUT = "STO-N10-2g-15a-500C-vac_MvT_H-300_Oe-K-full_220119.rso"
OUTPUT = ""
COLS = [2, 3, 4, 6] # columns indexed from 0
HEADERS = ["Field (Oe)", "Temperature (K)", "Long Moment (emu)", "Long Offset (cm)"]



def extract_dat():
    filename = os.path.join(DIR, INPUT + ".dat")
    with open(filename, "r") as f:
        lines = f.readlines()[1:]
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


extract_dat()






