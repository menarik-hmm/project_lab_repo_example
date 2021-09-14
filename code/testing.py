import numpy as np
import pandas as pd

def file_importer():
    """
    some documentations
    """
    data = pd.read_csv('yaddayadda.csv', delimiter=",")
    data.dropna()
    return data

if __name__ == "__main__":
    test = file_importer()
