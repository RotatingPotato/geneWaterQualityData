import random
from datetime import datetime, timedelta

# 生成水質資料
def geneData(nums):
    data = []
    todayDate = datetime.today().strftime('%Y-%m-%d')

    print("模式選擇：")
    print("1. 維持偏中性的水質")
    print("2. 維持偏酸性的水質")
    print("3. 維持偏鹼性的水質")
    print("4. 偏酸性的水質逐漸轉為偏中性")
    print("5. 偏鹼性的水質逐漸轉為偏中性")
    print("6. 偏中性的水質逐漸轉為偏酸性")
    print("7. 偏中性的水質逐漸轉為偏鹼性")
    print("0. 離開程式")
    mode = int(input("請選擇模式（0-7）："))

    # 根據不同模式初始化起始值
    if mode == 1:  # 維持偏中性的水質
        previous_pH = random.uniform(6.5, 8.5)
        previous_EC = random.uniform(300, 600)
    elif mode == 2:  # 維持偏酸性的水質
        previous_pH = random.uniform(5.5, 7.0)
        previous_EC = random.uniform(100, 300)
    elif mode == 3:  # 維持偏鹼性的水質
        previous_pH = random.uniform(7.5, 9.0)
        previous_EC = random.uniform(500, 900)
    elif mode == 4:  # 偏酸性的水質逐漸轉為偏中性
        previous_pH = random.uniform(5.0, 7.0)
        previous_EC = random.uniform(100, 300)
    elif mode == 5:  # 偏鹼性的水質逐漸轉為偏中性
        previous_pH = random.uniform(8.0, 9.0)
        previous_EC = random.uniform(600, 900)
    elif mode == 6:  # 偏中性的水質逐漸轉為偏酸性
        previous_pH = random.uniform(6.5, 8.5)
        previous_EC = random.uniform(500, 700)
    elif mode == 7:  # 偏中性的水質逐漸轉為偏鹼性
        previous_pH = random.uniform(6.5, 8.5)
        previous_EC = random.uniform(300, 500)
    elif mode == 0:  # 離開程式
        print("程式已結束。")
        return None
    else:
        print("無效的模式選擇。請選擇 0 到 7 之間的數字。")
        return None

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