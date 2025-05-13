import numpy as np
import pandas as pd
import os, glob

def main(period):
    people = []
    path = "Data/Preprocessed/"
    
    for filename in glob.glob(os.path.join(path, '*.csv')):
        df = pd.read_csv(filename, sep = ";")
        people.append(df.head(201))

    df = pd.concat(people)
    df[f"glucose_t+{period}"] = df["glucose"].shift(periods = -period)
    df = df.drop(index = 200)
    #! por el momento el datetime causa problemas con pytorch, así que lo ignoré, pero pienso reintroducirlo
    #! porque la correlación de time es de .1 > a las demás variables
    # t = df["time"].apply(lambda time: np.datetime64(time))
    # df["hour"] = t.apply(lambda t: t.hour)
    df = df.drop(columns = ["time"])
    # df = df.reset_index()
    df.to_csv(f"Data/Processed/data_t{period}.csv")


    return 0


if __name__ == "__main__":
    period = 3
    main(period)