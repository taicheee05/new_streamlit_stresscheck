import streamlit as st
from load_data import load_questions,load_output
from calculate_scores import calculate_score,calculate_soten_score
import re
import numpy as np
import pandas as pd
from google.oauth2.service_account import Credentials
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from high_stress_check import a_stress_score,b_stress_score,c_stress_score
#questions
# [
#     {
#         'No': '質問番号',
#         '質問文': '具体的な質問内容',
#         '選択肢': {
#             '選択肢1のテキスト': 選択肢1のスコア,
#             '選択肢2のテキスト': 選択肢2のスコア,
#             '選択肢3のテキスト': 選択肢3のスコア,
#             '選択肢4のテキスト': 選択肢4のスコア
#         }
#     },
# ]
#questionはload_questions関数の中で登場する変数みたいなもので、questionsリストの中に入っている1つ1つのインデックス内にある辞書がquestion

#answers辞書のキーは質問番号 (q_id) となり、要素（値）はユーザーが選択した選択肢のスコアになります。具体的には、ユーザーが質問に対して選んだ選択肢のテキストではなく、その選択肢に関連付けられたスコア（数値）がanswers辞書に格納されます。

# Email Address (半角英数チェック)
email = st.text_input("Email Address")
if email and not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    st.error("メールアドレスは半角英数で入力してください。")

# 職場コード
workplace_code = st.selectbox("職場コードを選択してください", ["コード1", "コード2", "コード3", "その他"])

# 職場名
workplace_name = st.selectbox("職場名を選択してください", ["職場A", "職場B", "職場C", "その他"])

# 氏名（スペースなしチェック）p
name = st.text_input("氏名")
if ' ' in name:
    st.error("氏名にスペースを入れないでください。")

# ふりがな（スペースなしチェック）
furigana = st.text_input("ふりがな")
if ' ' in furigana:
    st.error("ふりがなにスペースを入れないでください。")

# 社員番号 (半角英数チェック)
employee_number = st.text_input("社員番号")
if employee_number and not re.match(r'^[A-Za-z0-9]+$', employee_number):
    st.error("社員番号は半角英数で入力してください。")

# 生年月日
birthdate = st.date_input("生年月日を記入してください")

# 性別
gender = st.radio("性別", ["男性", "女性"])


def main():
    st.title("ストレスチェック")

    # 質問をロード
    questions = load_questions("survey_questions.csv")
    # 素点計算ロジックをロード
    if gender== "男性":
        outputs=load_output("output_man.csv")
    else:
        outputs=load_output("output_woman.csv")
    
    # ユーザーの回答を保持する辞書
    answers = {}
    # 計算用にユーザー回答を保存する辞書
    calculate={}

    # 質問ごとにUIを作成
    for question in questions:
        q_id, q_text, choices = question['No'], question['質問文'], question['選択肢']
        answers[q_id] = st.radio(q_text, list(choices.keys()))
        # calculate[q_id]=st.radio(q_text,list(choices.values()))
        calculate[q_id]=choices[answers[q_id]]

    results =calculate_soten_score(calculate, outputs)
    #尺度ごとに計算結果を算出
    a_stress_scores=a_stress_score(calculate)
    b_stress_scores=b_stress_score(calculate)
    c_stress_scores=c_stress_score(calculate)

    if st.button("回答を提出する"):
        # for output in outputs:
            score = 0

            columns = ['Category', '低い／少ない', 'やや低い／少ない', '普通', 'やや高い／多い', '高い／多い']
        
            rows_a = []  # 空のリストを初期化

            for category, rating in results.items():
                new_row = {column: '' for column in columns}  # 新しい行を辞書として作成
                new_row['Category'] = category
                new_row[rating] = '〇'
                rows_a.append(new_row)  # リストに辞書を追加
            df_a = pd.DataFrame(rows_a, columns=columns)  # リストからDataFrameを作成
            st.table(df_a)
            # スコアに基づいてメッセージを表示
            if (b_stress_scores >= 77) or ((a_stress_scores + c_stress_scores >= 76) and (b_stress_scores >= 63)):
            # 条件を満たす場合、メッセージを表示
                st.write("あなたは高ストレス者に該当します。医師の面接指導を受けていただくことをおすすめします。")
            else:
                # 条件を満たさない場合、別のメッセージを表示（必要に応じて）
                st.write("高ストレスのリスクは低いようです")

if __name__ == "__main__":
    main()
