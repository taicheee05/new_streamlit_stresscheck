import pandas as pd

def load_questions(filename):
    # CSVファイルを読み込む
    df = pd.read_csv(filename)
    questions = []

    for _, row in df.iterrows():
        question = {}
        question['No'] = row['No']
        question['質問文'] = row['質問文']
        
        #row['質問ID']という表現では、rowはDataFrameから取り出された各行を表すPandasのSeriesオブジェクトで、['質問ID']はそのSeriesオブジェクトから特定のデータを取り出すためのキー（カラム名）です。ここで言う「質問ID」は、あなたが読み込むCSVファイルのカラム名の一つを指します。
        #CSVファイルには複数のカラムが存在し、各カラムにはユニークな名前があります。例えば、あるアンケートの質問IDを格納するカラムがある場合、そのカラムの名前が「質問ID」であることを示します。したがって、「’」と「’」の間には、CSVファイルのカラム名を正確に入れる必要があります。
        #「question」という辞書の「選択肢」というキー名に、スコアが辞書形式で格納されている
        # 選択肢とスコアを辞書形式で格納
        question['選択肢'] = {
            row['選択肢1']: row['選択肢1_スコア'],
            row['選択肢2']: row['選択肢2_スコア'],
            row['選択肢3']: row['選択肢3_スコア'],
            row['選択肢4']: row['選択肢4_スコア'],
        }
        questions.append(question)

    return questions

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


def load_output(filename):
    df = pd.read_csv(filename)
    outputs = []

    for _, row in df.iterrows():
        output = {}
        output['番号'] = row['番号']
        output['尺度'] = row['尺度']
        
        output['選択肢'] = [
            row['低い／少ない'], row['やや低い／少ない'],row['普通'],row['やや高い／多い'],row['高い／多い']
        ]
        outputs.append(output)
    return outputs

#outputs_manは、CSVファイルから読み込んだデータを元に、各行ごとに辞書形式で格納されたリストになります。各辞書には番号、尺度、そして選択肢のキーが含まれ、選択肢は「低い／少ない」から「高い／多い」までのカテゴリをリスト形式で格納します。この構造により、尺度ごとの評価結果を効率的に管理・アクセスできるようになります。