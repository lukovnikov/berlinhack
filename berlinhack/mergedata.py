import pandas as pd
import os
import sys
import re


def run():
    frames = []
    filter = re.compile(r'.+stop-and-search\.csv')
    for root, dirs, files in os.walk("../data/"):
        path = root.split(os.sep)
        print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            filep = root + "/" + file
            if filter.match(filep):
                print(filep)
                frame = pd.DataFrame.from_csv(filep)
                frames.append(frame)
    print("loaded {} frames".format(len(frames)))



if __name__ == "__main__":
    run()