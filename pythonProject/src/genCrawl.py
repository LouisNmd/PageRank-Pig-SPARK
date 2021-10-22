import csv
import math
import random
import os
import sys


def goodGenCrawl(nbURL):
    f = open('crawl.csv', "w")
    csv_writer = csv.writer(f, delimiter="\t")
    percentNetwork = 0.70
    probDiffPerLoop = percentNetwork / nbURL
    for i in range(nbURL):
        baseUrl = 'x' + str(i)
        percentNetwork = 0.70
        for j in range(nbURL):
            if random.random() <= percentNetwork:
                targetUrl = 'x' + str(j)
                row = [baseUrl, targetUrl]
                csv_writer.writerow(row)
            percentNetwork -= probDiffPerLoop


def randomGenCrawl(nbURL):
    home_path = os.path.dirname(os.path.abspath(__file__))
    f = open('crawl.csv', "w")
    csv_writer = csv.writer(f, delimiter="\t")
    percentNetwork = 0.90
    for i in range(nbURL):
        baseUrl = 'x' + str(i)
        targetUrl = ''
        while random.random() <= percentNetwork:
            if targetUrl == '':
                targetUrl = '(x' + str(math.floor(random.random() * nbURL)) + ')'
            else:
                targetUrl = targetUrl + ', (x' + str(math.floor(random.random() * nbURL)) + ')'
        row = [baseUrl, 1, '{ ' + targetUrl + ' }']
        csv_writer.writerow(row)


if __name__ == "__main__":
    goodGenCrawl(int(sys.argv[1]))
    # randomGenCrawl(100000)
