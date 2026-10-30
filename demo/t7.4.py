import pandas as pd
 
df = pd.DataFrame({
    "Անուն": ["Անի", "Արամ", "Մարի", "Գագիկ", "Լիլիթ", "Նարե"],
    "Տարիք": [20, 32, 27, 24, 19, 35],
})
 
print(df.columns.tolist())
