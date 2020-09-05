import pandas as pd
df = pd.read_excel("test_data.xlsx")

data = {}
for i in df.columns[1:]:
    for j in zip(df['Bengala'],df[i]):
        a,b = j[::-1]
        data[a]=b

d1 = pd.Dataframe(data.items(),columns=['English','Bengala'])
d1.to_csv("mapping.csv")