import pandas as pd

def test_penguin_dataset_shape():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    df = pd.read_csv(url)
    assert df.shape == (344, 7)



