import pandas as pd

a = pd.DataFrame([[1],[2],[3],[4],[5]], columns=['Numbers'])

for i in a.itertuples():
    print(i)


for i in a.iterrows():
    print(i)