import gspread
from oauth2client.service_account import ServiceAccountCredentials

# スプレッドシートへの接続設定
def spreadsheet_reflect(calculate):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/service-account.json', scope) #jsonが配置されている場所を記入する
    client = gspread.authorize(creds)
    # スプレッドシートを開く
    spreadsheet = client.open('your_spreadsheet_name')  # スプレッドシート名を指定
    worksheet = spreadsheet.sheet1  # 最初のワークシートを選択
    #回答を列に追加していく。
    cells=[]
    for answer in calculate:
        cell=answer[]


# 回答を提出するボタンが押されたとき
    if st.button("回答を提出する"):
        # ユーザーの回答データをリストにまとめる
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
    # スプレッドシートにデータを追加
    worksheet.append_row(user_data)  # ユーザーの回答を追加
