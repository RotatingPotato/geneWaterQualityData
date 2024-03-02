import csv
from src.gene import geneData
from src.plot import plotPH, plotDO, plotEC, plotORP

def saveToCSV(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Location', 'pH', 'DO', 'EC',
                      'ORP', 'PHScore', 'DOScore', 'ECScore', 'ORPScore']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for record in data:
            writer.writerow(record)

if __name__ == "__main__":
    waterQualityData = geneData(500)
    try:
        saveToCSV(waterQualityData, 'output/data.csv')
        print('CSV文件儲存成功！')
    except Exception as e:
        print('CSV文件儲存失敗：', e)

    # 繪製折線圖
    plotPH(waterQualityData)
    plotDO(waterQualityData)
    plotEC(waterQualityData)
    plotORP(waterQualityData)