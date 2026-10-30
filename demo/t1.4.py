import pandas as pd
df=pd.DataFrame({
    "anun":["Armine","Nane","Aram","Karo"],
    "tariq":[12,23,4,77]
    })

filtered=df[df["tariq"]>25]
print(filtered)
