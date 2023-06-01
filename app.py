import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# 質問のリスト
questions = [
    "性別を教えてください。",
    "年齢を教えてください。",
    "身長を教えてください。",
    "体重を教えてください。",
    "どのような症状がありますか？",
    "現在服用している薬はありますか？",
    "アレルギーの有無を教えください。"
]

# 質問に対する回答のリスト
answers = []

# 質問に回答するためのフォームを作成
for question in questions:
    if question == "どのような症状がありますか？":
        answer = st.text_input(question)
    elif question == "現在服用している薬はありますか？":
        answer = st.text_input(question)
    elif question == "アレルギーの有無を教えてください。":
        answer = st.checkbox(question)
    else:
        answer = st.number_input(question)
    answers.append(answer)

# 回答をデータフレームに変換
input_data = pd.DataFrame([answers], columns=["性別", "年齢", "身長", "体重", "症状", "薬", "アレルギー"])

# モデルの読み込み
model = RandomForestClassifier()
model.fit(data.drop("医薬品", axis=1), data["医薬品"])

# 最適な医薬品の予測
prediction = model.predict(input_data.drop("薬", axis=1))

# 医薬品に関する情報の表示
st.write("最適な医薬品は", prediction[0], "です。")

# 医薬品に関する情報の表示
drug_info = data[data["医薬品"] == prediction[0]].drop("医薬品", axis=1)
st.write(drug_info)

# 医薬品の副作用の可視化
side_effects = drug_info.T.squeeze()
side_effects.plot(kind="bar")
plt.title("副作用")
plt.xlabel("副作用")
plt.ylabel("割合")
st.pyplot()
