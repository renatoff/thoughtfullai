import pandas as pd

from read import read_packages
from package_sorter import sort


def main():
    data_path = "src/data/data.csv"
    packages = read_packages(data_path)
    df = pd.DataFrame(packages)
    df["stack"] = df.apply(
        lambda row: sort(row["width"], row["height"], row["length"], row["mass"]),
        axis=1,
    ) # FIXME: handle errors inside sort function

df
