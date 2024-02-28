def get_score_level(score, choices):
    level = ["低い／少ない", "やや低い／少ない", "普通", "やや高い／多い", "高い／多い"]
    if score < choices[0]:
        return level[0]
    elif choices[0] <= score < choices[1]:
        return level[1]
    elif choices[1] <= score < choices[2]:
        return level[2]
    elif choices[2] <= score < choices[3]:
        return level[3]
    else:
        return level[4]
