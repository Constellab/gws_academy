import pandas as pd


df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                           'B': {0: 1, 1: 3, 2: 5},
                           'C': {0: 2, 1: 4, 2: 6}})

essai ={
    "zero" : df,
    "un" : pd.melt(df, id_vars=['A'], value_vars=['B']),

    "deux" : pd.melt(df, id_vars=['A'], value_vars=['B', 'C']),

    "trois" : pd.melt(df, id_vars=['A'], value_vars=['B'],
        var_name='myVarname', value_name='myValname'),

    "quatre" : pd.melt(df, id_vars=['A'], value_vars=['B', 'C'], ignore_index=False)}

for i in essai :
    print(i,"\n", essai[i] )
