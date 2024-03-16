import streamlit as st
from load_data import load_questions,load_output
from calculate_scores import calculate_score,calculate_soten_score
import re
import numpy as np
import pandas as pd
import toml
from google.oauth2.service_account import Credentials
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from high_stress_check import a_stress_score,b_stress_score,c_stress_score,stress_check_spreadsheetreflect
from spreadsheet_reflect import spreadsheet_reflect #add 2024/03/08
from calculate_scores import calculate_score
from datetime import date
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
#初期化
form_valid = True
st.write("正しい記載があった後にストレスチェックの質問が表示されます")
# メールアドレスの入力
email = st.text_input("Email Address")
if email:
    # RFC 5322 に基づいたメールアドレスの検証パターン
    pattern = (r'(?i)^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$')
    if not re.match(pattern, email):
        form_valid = False
        st.error("正しいメールアドレスの形式で入力してください。")
else:
    st.error("メールアドレスは必須項目です。")
    form_valid = False

# 職場コード
workplace_code = st.selectbox("職場コードを選択してください", ["コード1", "コード2", "コード3", "その他"], index=0)
if not workplace_code:
    st.error("職場コードは必須項目です。")
    form_valid=False

# 職場名
workplace_name = st.selectbox("職場名を選択してください", ["職場A", "職場B", "職場C", "その他"], index=0)
if not workplace_name:
    st.error("職場名は必須項目です。")
    form_valid=False

# 氏名
name = st.text_input("氏名")
if not name:
    st.error("氏名は必須項目です。")
    form_valid=False
elif ' ' in name:
    st.error("氏名にスペースを入れないでください。")
    form_valid=False

# ふりがな
furigana = st.text_input("ふりがな")
if not furigana:
    st.error("ふりがなは必須項目です。")
    form_valid=False
elif ' ' in furigana:
    st.error("ふりがなにスペースを入れないでください。")
    form_valid=False

# 社員番号
employee_number = st.text_input("社員番号")
if employee_number:
    if not re.match(r'^[A-Za-z0-9]+$', employee_number):
        st.error("社員番号は半角英数で入力してください。")
        form_valid=False
else:
    st.error("社員番号は必須項目です。")
    form_valid=False

# 生年月日
birthdate = st.date_input(
    "生年月日を記入してください",
    min_value=date(1930, 1, 1),
    max_value=date.today()
)

# 性別
gender = st.radio("性別", ["男性", "女性"], index=0)


def main():
    st.title("ストレスチェック")
    if form_valid:

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

        results, syakudo_values =calculate_soten_score(calculate, outputs)
        #尺度ごとに計算結果を算出
        a_stress_scores=a_stress_score(calculate)
        b_stress_scores=b_stress_score(calculate)
        c_stress_scores=c_stress_score(calculate)

        if st.button("回答を提出する"):
            # for output in outputs
                st.write('以下があたなのストレスプロフィールです。スクリーンショット等でご自分で記録を大切に保管してください')
                
                columns = ['Category', '低い／少ない', 'やや低い／少ない', '普通', 'やや高い／多い', '高い／多い']
            
                rows_a = []  # 空のリストを初期化

                for category, rating in results.items():
                    new_row = {column: '' for column in columns}  # 新しい行を辞書として作成
                    new_row['Category'] = category
                    new_row[rating] = "〇"
                    rows_a.append(new_row)  # リストに辞書を追加
                df_a = pd.DataFrame(rows_a, columns=columns)  # リストからDataFrameを作成
                st.table(df_a)
                # スコアに基づいてメッセージを表示
                if (b_stress_scores >= 77) or ((a_stress_scores + c_stress_scores >= 76) and (b_stress_scores >= 63)):
                # 条件を満たす場合、メッセージを表示
                    st.write("あなたは高ストレス者に該当します。医師の面接指導を受けていただくことをおすすめします。")
                else:
                # 条件を満たさない場合、別のメッセージを表示（必要に応じて）
                    st.write("高ストレスのリスクは低いようです。一方で体調が優れない、気分の変調があるなどの異変がある場合には周囲に相談し、医師の面談を受けてください")

                data = [
                    [a_stress_scores, "高得点ほど高ストレス(17~68点)"],
                    [b_stress_scores, "高得点ほど高ストレス(29~116点)"],
                    [c_stress_scores, "高得点ほど高ストレス(9~36点)"]
                ]
                    #表示と点数があってる？
                # インデックスとカラム
                index1 = ["ストレスの要因に関する項目", "心身のストレス反応に関する項目", "周囲のサポートに関する項目"]
                columns1 = ["評価点（合計）", "解説"]
                df=pd.DataFrame(data=data, index=index1, columns=columns1)
                st.table(df)

                # ユーザーの個人情報と回答を結合
                user_data = [
                    email,
                    workplace_code,
                    workplace_name,
                    name,
                    furigana,
                    employee_number,
                    str(birthdate),  # datetimeオブジェクトを文字列に変換
                    gender
                ] 
                
                # スプレッドシートにデータを追加する関数を呼び出し
                test_list=stress_check_spreadsheetreflect(calculate)

                spreadsheet_reflect(user_data,calculate,results,test_list,syakudo_values)      
    else:
        st.error("エラーを修正してください")
if __name__ == "__main__":
        main()

