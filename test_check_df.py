import pandas as pd
from check_df import check_df

# サンプルCSVを読み込み
df = pd.read_csv("sample_data.csv")

# 関数を実行
info = check_df(df)

# 結果を表示
print(info)
