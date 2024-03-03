import random
from datetime import datetime, timedelta

# 生成水質資料
def geneData(nums):
    data = []
    todayDate = datetime.today().strftime('%Y-%m-%d')
    previous_pH = random.uniform(6.5, 8.5)
    previous_EC = random.uniform(200, 400)  # 將起始 EC 調整為合理範圍

    for i in range(nums - 1, -1, -1):
        # 生成新的水質數據，跟隨前一筆數據的正負波動
        pH = max(min(previous_pH + random.uniform(-0.1, 0.1), 9.0), 5.0)  # 限制 pH 在 5.0 到 9.0 之間
        EC = max(min(previous_EC + random.uniform(-10, 10), 600), 100)  # 限制 EC 在 100 到 600 之間

        # 基於 pH 生成 DO，根據正比關係
        DO = min(max((pH - 6.5) * 1.5 + 5, 0), 10)

        # 基於 EC 生成 ORP，根據正比關係
        ORP = min(max((EC - 100) * 0.75 + 150, -200), 800)  # 限制 ORP 在 -200 到 800 之間

        # 更新上一筆數據
        previous_pH = pH
        previous_EC = EC

        pH = round(pH, 2)
        DO = round(DO, 2)
        EC = round(EC, 2)
        ORP = round(ORP, 2)

        pHScore = calcPHScore(pH)
        DOScore = calcDOScore(DO)
        ECScore = calcECScore(EC)
        ORPScore = calcORPScore(ORP)

        # 將日期從最後一筆開始向前推
        date = (datetime.strptime(todayDate, '%Y-%m-%d') -
                timedelta(days=i)).strftime('%Y-%m-%d')

        data.append({'Date': date, 'Location': 'CodeRyo Lake', 'pH': pH, 'DO': DO, 'EC': EC, 'ORP': ORP,
                     'PHScore': pHScore, 'DOScore': DOScore,
                     'ECScore': ECScore, 'ORPScore': ORPScore})

    return data

# 計算 pH 分數
def calcPHScore(pH):
    if 7.0 <= pH <= 7.5:
        return 5
    elif (6.5 <= pH < 7.0) or (7.5 < pH <= 8.0):
        return 4
    elif (6.0 <= pH < 6.5) or (8.0 < pH <= 8.5):
        return 3
    elif (5.5 <= pH < 6.0) or (8.5 < pH <= 9.0):
        return 2
    else:
        return 1

# 計算 DO 分數
def calcDOScore(DO):
    if DO >= 5.0:
        return 4
    elif 4.0 <= DO < 5.0:
        return 3
    elif 2.5 <= DO < 4.0:
        return 2
    else:
        return 1

# 計算 EC 分數
def calcECScore(EC):
    if 100 <= EC < 500:
        return 4
    elif 500 <= EC < 750:
        return 3
    elif 750 <= EC < 1200:
        return 2
    else:
        return 1

# 計算 ORP 分數
def calcORPScore(ORP):
    if 300 <= ORP < 450:
        return 3
    elif (0 <= ORP < 300) or (450 <= ORP < 800):
        return 2
    else:
        return 1