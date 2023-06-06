import pandas as pd
import numpy as np
from math import nan
print(pd.NA, np.nan, nan, None)
import pandas as pd
from PrettyColorPrinter import add_printer
add_printer(1)
df=pd.read_csv("https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv")
df=df.fillna(pd.NA)
df.at[0,'Pclass'] = np.nan
df.Age = df.Age.astype('Float64').fillna(pd.NA)
df.Pclass = df.Pclass.astype('Int64').fillna(pd.NA)
df.Pclass / 2
df.Pclass.sum()
df.loc[df.Cabin.str.contains('^C',regex=True,na=False)]
