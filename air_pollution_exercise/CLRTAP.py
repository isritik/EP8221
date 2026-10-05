#%%
import pandas as pd

#%%
df_TAP = pd.read_csv("CLRTAP_small.txt", delimiter ="\t", header=0, index_col=0)
print(df_TAP.head())

#%%
df_TAP.shape

# %%
df_TAP.head()
# %%
df_TAP.info()
# %%
df_TAP.describe()
# %%
df_TAP.isna().sum()

#%%
df_TAP.nunique()
# %%
