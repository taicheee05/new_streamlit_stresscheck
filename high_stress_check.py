
#領域Bの合計点数が77点以上
#領域AとCの合算が76点以上、かつ、領域Bの合計が63点以上
#領域aの点数
def a_stress_score(calculate):
    # 初期スコア
    a_stress_score = 0
    # 5から引く必要があるインデックスのリスト
    subtract_indices = [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 15]
    # 合計計算
    for i in range(1, 18):  # 1から17まで (calculate[1] から calculate[17] まで)
        if i in subtract_indices:
            a_stress_score += (5 - calculate[i])
        else:
            a_stress_score += calculate[i]
    return a_stress_score
#領域bの点数
def b_stress_score(calculate):
    # 初期スコア
    b_stress_score = 0
    # 5から引く必要があるインデックスのリスト
    subtract_indices = [18, 19, 20]
    # 合計計算
    for i in range(18, 47):  
        if i in subtract_indices:
            b_stress_score += (5 - calculate[i])
        else:
            b_stress_score += calculate[i]
    return b_stress_score

#領域Cの点数
def c_stress_score(calculate):
    # 初期スコア
    c_stress_score = 0
    # 合計計算
    for i in range(47, 56):  
        c_stress_score += calculate[i]
    return c_stress_score

#ストレスチェックの結果をスプレッドシートに反映するための関数
def stress_check_spreadsheetreflect(calculate):
    test_list={}
    b_stress_score = 0
    # 5から引く必要があるインデックスのリスト
    subtract_indices = [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 15]
    # 合計計算
    for i in range(1, 18):  # 1から17まで (calculate[1] から calculate[17] まで)
        if i in subtract_indices:
            b_stress_score += (5 - calculate[i])
        else:
            b_stress_score += calculate[i]

    a_stress_score = 0
    # 5から引く必要があるインデックスのリスト
    subtract_indices_a = [18, 19, 20]
    # 合計計算
    for s in range(18, 47):  
        if s in subtract_indices_a:
            a_stress_score += (5 - calculate[s])
        else:
            a_stress_score += calculate[s]
#領域Cの点数
    c_stress_score = 0
    # 合計計算
    for t in range(47, 55):  
        c_stress_score += calculate[t]

    if (b_stress_score >= 77) or ((a_stress_score + c_stress_score >= 76) and (b_stress_score >= 63)):
        test_list={'判定':'高ストレス者'}
    else: test_list= {'判定':'非高ストレス者'}
    return test_list