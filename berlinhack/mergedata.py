import pandas as pd
import os
import sys
import re


def run():
    ret = None
    frames = []
    filter = re.compile(r'.+street\.csv')
    for root, dirs, files in os.walk("../data/alllondon"):
        path = root.split(os.sep)
        print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            filep = root + "/" + file
            if filter.match(filep):
                print(filep)
                frame = pd.DataFrame.from_csv(filep)
                frames.append(frame)
    print("loaded {} frames".format(len(frames)))
    ret = pd.concat(frames)
    print("merged files contain {} rows".format(len(ret)))
    print(ret)
    ret.to_csv("../data/all-street-2015.csv")
    print("saved")
    lastoutcomes = ret["Last outcome category"]
    ulastoutcomes = lastoutcomes.unique()
    print(len(ulastoutcomes))
    print(ulastoutcomes)
    return ret



if __name__ == "__main__":
    run()