
#領域Bの合計点数が77点以上
#領域AとCの合算が76点以上、かつ、領域Bの合計が63点以上
#領域Bの点数
def b_stress_score(calculate):
    # 初期スコア
    b_stress_score = 0
    # 5から引く必要があるインデックスのリスト
    subtract_indices = [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 15]
    # 合計計算
    for i in range(1, 18):  # 1から17まで (calculate[1] から calculate[17] まで)
        if i in subtract_indices:
            b_stress_score += (5 - calculate[i])
        else:
            b_stress_score += calculate[i]
    return b_stress_score
#領域Aの点数
def a_stress_score(calculate):
    # 初期スコア
    a_stress_score = 0
    # 5から引く必要があるインデックスのリスト
    subtract_indices = [18, 19, 20]
    # 合計計算
    for i in range(18, 47):  
        if i in subtract_indices:
            a_stress_score += (5 - calculate[i])
        else:
            a_stress_score += calculate[i]
    return a_stress_score

#領域Cの点数
def c_stress_score(calculate):
    # 初期スコア
    c_stress_score = 0
    # 合計計算
    for i in range(47, 55):  
        c_stress_score += calculate[i]
    return c_stress_score
