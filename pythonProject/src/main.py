import csv
import random
import os


def goodGenCrawl(nbURL):
    home_path = os.path.dirname(os.path.abspath(__file__))
    f = open('crawl.csv', "w")
    csv_writer = csv.writer(f, delimiter="\t")
    percentNetwork = 0.70
    probDiffPerLoop = percentNetwork / nbURL
    tabTargetUrl = [''] * nbURL
    for i in range(len(tabTargetUrl)):
        percentNetwork = 0.70
        for j in range(len(tabTargetUrl)):
            temp = random.random()
            if temp <= percentNetwork:
                if tabTargetUrl[i] == '':
                    tabTargetUrl[i] = '(x' + str(j) + ')'
                else:
                    tabTargetUrl[i] = tabTargetUrl[i] + ', (x' + str(j) + ')'
            percentNetwork -= probDiffPerLoop

    for i in range(len(tabTargetUrl)):
        baseUrl = 'x' + str(i)
        targetUrl = '{ ' + tabTargetUrl[i] + ' }'
        row = [baseUrl, 1, targetUrl]
        csv_writer.writerow(row)


def randomGenCrawl(nbURL):
    home_path = os.path.dirname(os.path.abspath(__file__))
    f = open('crawl.csv', "w")
    csv_writer = csv.writer(f, delimiter="\t")
    percentNetwork = 0.70
    for i in range(nbURL):
        baseUrl = 'x' + str(i)
        targetUrl = ''
        while random.random() <= percentNetwork:
            if targetUrl == '':
                targetUrl = '(x' + str(random.random()*nbURL) + ')'
            else:
                targetUrl = targetUrl + ', (x' + str(random.random()*nbURL) + ')'
        row = [baseUrl, 1, '{ '+targetUrl + ' }']
        csv_writer.writerow(row)


if __name__ == "__main__":
    #goodGenCrawl(10000)
    randomGenCrawl(10000)


