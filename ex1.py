import os
import pandas as pd

s = 'C:\Users\16142\OneDrive\Documents\aProject\1mlpytorchbook\iris.data'

print('From URL:',s)

From URL: C:\Users\16142\OneDrive\Documents\aProject\1mlpytorchbook\iris.data

df = pd.read_csv(s,
                 header=None,
                 encoding='utf-8')
df.tail()