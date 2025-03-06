import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')
df1 = df.loc[df['Year'] >= 2000]

print(df1)