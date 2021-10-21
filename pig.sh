#!/bin/bash
start='date +%s'
gcloud dataproc jobs submit pig --cluster=cluster-pig-crawling --file=/home/raph/Documents/M2/LSDM/PageRank-Pig-SPARK/pythonProject/src/PageRankPig.py --region=europe-west1
end='date +%s'
echo The script ran for 'expr $end - $start' seconds.