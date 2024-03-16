from soten_calculate import get_score_level
#answersはユーザーの回答を保存する辞書
#answers辞書は、キーにNo、要素に回答の点数が入るようになった
def calculate_score(answers, questions):
    total_score_a = 0
    # ユーザーの回答と質問データを照合してスコアを計算
    for question in questions:
        q_id = question['No']
        user_answer = answers[q_id]
        question_score = question['選択肢'][user_answer]
        total_score_a += question_score
    return total_score_a


#calculate辞書には回答結果が入っている
#calculate辞書のキーには問題の番号と回答者の点数が入っている
    #output
    #for で尺度毎に出していって、ifで計算ロジックだけ変更させる形にする。

def calculate_soten_score(calculate, outputs):
    results={}
    syakudo_value={}
    score = 0
    # ユーザーの回答と質問データを照合してスコアを計算
    for output in outputs:
        score = 0
        o_id = output['番号']
        if o_id==1:
            score = 15 - (calculate[1] + calculate[2] + calculate[3])
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==2:
            score = 15 - (calculate[4] + calculate[5] + calculate[6])
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==3:
            score = 5 - calculate[7]
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==4:
            score = 10 -(calculate[12] + calculate[13]) +calculate[14]
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==5:
            score = 5- calculate[15]
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==6:
            score = 15 - (calculate[8] + calculate[9] + calculate[10])
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==7:
            score = calculate[11]
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==8:
            score = 5 - calculate[16]
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==9:
            score =5 - calculate[17]
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==10:
            score =calculate[18]+calculate[19]+calculate[20]
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==11:
            score=calculate[21]+calculate[22]+calculate[23]
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==12:
            score=calculate[24]+calculate[25]+calculate[26]
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==13:
            score=calculate[27]+calculate[28]+calculate[29]
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==14:
            score=calculate[30]+calculate[31]+calculate[32]+calculate[33]+calculate[34]+calculate[35]
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==15:
            score=calculate[36]+calculate[37]+calculate[38]+calculate[39]+calculate[40]+calculate[41]+calculate[42]+calculate[43]+calculate[44]+calculate[45]+calculate[46]
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==16:
            score=15-(calculate[47]+calculate[50]+calculate[53])
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==17:
            score=15-(calculate[48]+calculate[51]+calculate[54])
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==18:
            score=15-(calculate[49]+calculate[52]+calculate[55])
            results[output['尺度']] = get_score_level(score, output['選択肢'])
        elif o_id==19:
            score=10-(calculate[56]+calculate[57])
            results[output['尺度']] = get_score_level(score, output['選択肢'])

    return results


#results辞書の中身
    #キーに尺度の名前が入り、値にはlevel = ["低い／少ない", "やや低い／少ない", "普通", "やや高い／多い", "高い／多い"]の何れかが入る

#其々の列の指定方法
    # output["選択肢"][0]: '低い／少ない'
    # output["選択肢"][1]: 'やや低い／少ない'
    # output["選択肢"][2]: '普通'
    # output["選択肢"][3]: 'やや高い／多い'
    # output["選択肢"][4]: '高い／多い'


def syakudo_values_test(calculate, outputs):
    syakudo_value={}
    score = 0
    # ユーザーの回答と質問データを照合してスコアを計算
    for output in outputs:
        score = 0
        o_id = output['番号']
        if o_id==1:
            score = 15 - (calculate[1] + calculate[2] + calculate[3])
            syakudo_value[output[o_id]] = score
        elif o_id==2:
            score = 15 - (calculate[4] + calculate[5] + calculate[6])
            syakudo_value[output[o_id]] = score
        elif o_id==3:
            score = 5 - calculate[7]
            syakudo_value[output[o_id]] = score
        elif o_id==4:
            score = 10 -(calculate[12] + calculate[13]) +calculate[14]
            syakudo_value[output[o_id]] = score
        elif o_id==5:
            score = 5- calculate[15]
            syakudo_value[output[o_id]] = score
        elif o_id==6:
            score = 15 - (calculate[8] + calculate[9] + calculate[10])
            syakudo_value[output[o_id]] = score
        elif o_id==7:
            score = calculate[11]
            syakudo_value[output[o_id]] = score                
        elif o_id==8:
            score = 5 - calculate[16]
            syakudo_value[output[o_id]] = score
        elif o_id==9:
            score =5 - calculate[17]
            syakudo_value[output[o_id]] = score
        elif o_id==10:
            score =calculate[18]+calculate[19]+calculate[20]
            syakudo_value[output[o_id]] = score
        elif o_id==11:
            score=calculate[21]+calculate[22]+calculate[23]
            syakudo_value[output[o_id]] = score
        elif o_id==12:
            score=calculate[24]+calculate[25]+calculate[26]
            syakudo_value[output[o_id]] = score
        elif o_id==13:
            score=calculate[27]+calculate[28]+calculate[29]
            syakudo_value[output[o_id]] = score
        elif o_id==14:
            score=calculate[30]+calculate[31]+calculate[32]+calculate[33]+calculate[34]+calculate[35]
            syakudo_value[output[o_id]] = score
        elif o_id==15:
            score=calculate[36]+calculate[37]+calculate[38]+calculate[39]+calculate[40]+calculate[41]+calculate[42]+calculate[43]+calculate[44]+calculate[45]+calculate[46]
            syakudo_value[output[o_id]] = score
        elif o_id==16:
            score=15-(calculate[47]+calculate[50]+calculate[53])
            syakudo_value[output[o_id]] = score
        elif o_id==17:
            score=15-(calculate[48]+calculate[51]+calculate[54])
            syakudo_value[output[o_id]] = score
        elif o_id==18:
            score=15-(calculate[49]+calculate[52]+calculate[55])
            syakudo_value[output[o_id]] = score
        elif o_id==19:
            score=10-(calculate[56]+calculate[57])
            syakudo_value[output[o_id]] = score

    return syakudo_value