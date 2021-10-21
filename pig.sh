#!/bin/bash
gcloud dataproc jobs submit pig --cluster="$1" --file=/home/raph/Documents/M2/LSDM/PageRank-Pig-SPARK/pythonProject/src/PageRankPig.py --region=europe-west1 "$2"
