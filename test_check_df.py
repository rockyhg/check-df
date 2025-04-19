import pandas as pd
from check_df import check_df

# サンプル用のCSVファイルを読み込む
# 適宜、自分のファイルパスに置き換えてください
df = pd.read_csv("sample_data.csv")

# check_df 関数で情報を取得
info = check_df(df)

# 結果を表示
print(info)
