import numpy as np
import pandas as pd
import os, glob

def main():
    people = []
    path = "Data/Preprocessed/"
    
    for filename in glob.glob(os.path.join(path, '*.csv')):
        df = pd.read_csv(filename, sep = ";")
        people.append(df.head(201))

    df = pd.concat(people)
    df["glucose_t+1"] = df["glucose"].shift(periods = -1)
    df = df.drop(index = 200)
    df["time"] = df["time"].apply(lambda time: np.datetime64(time))
    df.to_csv("Data/Processed/data.csv")
    
    return 0


if __name__ == "__main__":
    main()