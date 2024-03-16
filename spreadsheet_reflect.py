##修正version
import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import toml
from calculate_scores import calculate_soten_score
from high_stress_check import stress_check_spreadsheetreflect

# StreamlitのSecretsから認証情報を取得してGoogle APIにログイン
service_account_info = st.secrets["gcp_service_account"]
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_info(service_account_info, scopes=scope)
gc = gspread.authorize(credentials)


def spreadsheet_reflect(user_data, calculate,results,test_list):

    # スプレッドシートIDを変数に格納する
    SPREADSHEET_KEY = st.secrets["spreadsheet"]["id"]
    
    # スプレッドシート（ブック）を開く
    workbook = gc.open_by_key(SPREADSHEET_KEY)
    # 最初のワークシートを開く
    worksheet = workbook.sheet1
    
    # calculateから値のリストを作成し、user_dataにcalculate_valuesを追加
    calculate_values = list(calculate.values())
    results_values=list(results.values())
    high_stress_values = list(test_list.values())
    values_list = list(results.values())

# これでscoresには、すべての値が列挙された形になります。

    row_data = user_data + calculate_values + results_values + high_stress_values

    # スプレッドシートにデータを追加
    worksheet.append_row(row_data)

# この関数を実際に使用する際には、"JSONファイルのパス"と"シートID"を適切な値に置き換えてください。