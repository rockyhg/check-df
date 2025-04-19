# 📊 check_df - DataFrame 概要チェックツール

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

`check_df` は、Pandas の DataFrame の各列について以下の情報を一覧表示するユーティリティ関数です：

- データ型（dtype）
- NaN（欠損値）数
- ユニークな値の個数
- ユニークな値の内容（指定数以下のみ表示）

大規模データや探索的データ分析（EDA）に役立つサマリーを簡単に確認できます。

## インストール方法

この関数は Python モジュールとして pip 配布されていないため、GitHub から直接使用する形式になります。

1. 必要なライブラリ (pandas) をインポートします。

```bash
pip install pandas
```

2. 本リポジトリの **`check_df.py` を、あなたの Python プロジェクトのディレクトリに配置してください。** その上で、以下のように import して使用できます：

```python
from check_df import check_df
```

## 使用例

```python
import pandas as pd
from check_df import check_df

# サンプルCSVを読み込み
df = pd.read_csv("sample_data.csv")

# 関数を実行
info = check_df(df)

# 結果を表示
print(info)
```

### 3. 出力例（sample_data.csv の結果）

| Column        | dtypes  | NaN Count | Nunique | Unique Values                              |
|---------------|---------|------------|----------|---------------------------------------------|
| Id            | int64   | 0          | 20       | > 10 unique values                          |
| MSSubClass    | int64   | 0          | 5        | [20, 60, 70, 50, 30]                        |
| MSZoning      | object  | 0          | 4        | [RL, RM, C (all), RH]                       |
| LotFrontage   | float64 | 4          | 15       | > 10 unique values                          |
| LotArea       | int64   | 0          | 20       | > 10 unique values                          |
| SaleCondition | object  | 0          | 5        | [Normal, Abnorml, Partial, AdjLand, Alloca]|

## 関数仕様

```python
check_df(df, columns=None, show_values_limit=10)
```

### 引数

| 引数                | 説明                                     |
| ----------------- | -------------------------------------- |
| df                | pandasのDataFrame                       |
| columns           | チェック対象の列名のリスト（指定しない場合は全列が対象）      |
| show_values_limit | ユニーク値の表示上限（超えると「> n unique values」と表示） |

### 戻り値

| 戻り値     | 説明                                          |
|-----------|-----------------------------------------------|
| DataFrame | 各列の情報（dtype, NaN数, ユニーク数, 値リスト）をまとめた表 |

## ライセンス

このプロジェクトは MIT License のもとで公開されています。

<!-- ## 貢献について

バグの報告、提案、ドキュメントの改善など大歓迎です！
ぜひ [Issue](https://github.com/rockyhg/check-df/issues) や Pull Request をお送りください。 -->
