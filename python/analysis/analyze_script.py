#csvファイルの読み込み
#ファイル形式
# "day","job","Ptime","starttime","endtime", "kokyaku", "kokyaku_total", "WD"

import pandas as pd
import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import datetime

df = pd.read_csv('./csv/sample2.csv',header=0)

# 標準化
#scaler = StandardScaler()
#scaler.fit(np.array(df))
#df_std = scaler.transform(np.array(df))
#df_std = pd.DataFrame(df_std,columns=df.columns)

# 目的変数(Y)
Y = np.array(df['Ptime'])

# 説明変数(X)
col_name = ['kokyaku', 'kokyaku_total']
X = np.array(df[col_name])

# データの分割(訓練データとテストデータ)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# モデル構築
model = LinearRegression()

# 学習
model.fit(X_train, Y_train)

# 回帰係数
coef = pd.DataFrame({"col_name":np.array(col_name),"coefficient":model.coef_}).sort_values(by='coefficient')

# 結果

#f = open('out.csv',"w")
coef.to_csv("out.csv")
#writer = csv.writer(f)
#writer.writerows(print("【回帰係数】", coef))
#f.close()
#print("【回帰係数】", coef)
#print("【切片】:", model.intercept_)
#print("【決定係数(訓練)】:", model.score(X_train, Y_train))
#print("【決定係数(テスト)】:", model.score(X_test, Y_test))