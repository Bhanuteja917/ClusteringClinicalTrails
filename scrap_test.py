from utils.DataLoader import DataLoader
import pandas as pd

d = DataLoader(r'.\ctg-studies.json')
L = d.load_data()

L.to_csv(r'.\ctg-studies.csv', index=False)

