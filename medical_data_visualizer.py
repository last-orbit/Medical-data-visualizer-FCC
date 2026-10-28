import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)
# df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
# df.plot(x="x", y="y", kind="line")
# plt.show()
# 3
df.loc[df['cholesterol'] ==1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 0

df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 0



# 4
def draw_cat_plot():
    df_cat = df.copy()
    # 5
    df_cat = pd.melt(df_cat, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count').sort_values(by=['cardio', 'variable', 'value'])
    

    # 7
    g = sns.catplot(data=df_cat, x='value', y='count', hue='cardio', col='variable', kind='bar')


    # 8
    fig = g.figure


    # 9
    fig.savefig('catplot.png')

    return fig


# 10
def draw_heat_map():
    df_heat = df.copy()
    # 11
    
    df_heat = df_heat[
    (df_heat['ap_lo'] <= df_heat['ap_hi']) &
    (df_heat['height'] >= df_heat['height'].quantile(0.025)) &
    (df_heat['height'] <= df_heat['height'].quantile(0.975)) &
    (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) &
    (df_heat['weight'] <= df_heat['weight'].quantile(0.975))
]


    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15
    sns.heatmap(corr, mask=mask, ax=ax)


    # 16
    fig.savefig('heatmap.png')
    return fig
