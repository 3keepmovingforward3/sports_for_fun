
    # make dates match format
```
    df['DATE'] = df['DATE'].replace('/', '-')
    df.to_excel("data/NBA_Formula.xlsx", index=False)
```
