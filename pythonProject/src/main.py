import csv
import random
import os

if __name__ == "__main__":
    home_path = os.path.dirname(os.path.abspath(__file__))
    f = open('crawl.csv', "w")
    csv_writer = csv.writer(f, delimiter="\t")
    nbURL = 1000
    percentNetwork = 0.70
    probDiffPerLoop = percentNetwork/nbURL
    tabTargetUrl = ['']*nbURL
    for i in range(len(tabTargetUrl)):
        percentNetwork = 0.70
        for j in range(len(tabTargetUrl)):
            temp = random.random()
            if temp <= percentNetwork:
                if tabTargetUrl[i] == '':
                    tabTargetUrl[i] = '(x'+str(j)+')'
                else:
                    tabTargetUrl[i] = tabTargetUrl[i] + ', (x'+str(j)+')'
            percentNetwork -= probDiffPerLoop

    for i in range(len(tabTargetUrl)):
        baseUrl = 'x'+ str(i)
        targetUrl = '{ '+ tabTargetUrl[i] + ' }'
        row = [baseUrl, 1, targetUrl]
        csv_writer.writerow(row)

