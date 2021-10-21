#!/bin/bash
gcloud dataproc jobs submit pyspark --cluster="$1" /home/raph/Documents/M2/LSDM/PageRank-Pig-SPARK/pythonProject/src/PageRankSpark.py --region=europe-west1 -- gs://"$2"/crawl.csv 10