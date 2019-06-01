import csv
import pandas as pd
import re

csvfilepath = input('LINEでダウンロードしたテキストファイル filepath : ')
line_name = input('解析したいユーザーの名前 : ')
data = pd.read_table(csvfilepath, names=('time', 'name', 'text'), encoding='utf-8')
print("line_name: " + line_name)
data = data[data["name"] == line_name]
data.to_csv("processed.csv")