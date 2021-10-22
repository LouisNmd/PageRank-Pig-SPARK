#!/bin/bash
if [ $# -lt 2 ]
  then echo "Call spark.sh with <cluster_id> <cloudstorage bucket name>"
else
  STARTTIME=$(date +%s)
  gcloud dataproc jobs submit pyspark --cluster="$1" "$PWD"/pythonProject/src/PageRankSpark.py --region=europe-west1 -- gs://"$2"/crawl.csv 10
  ENDTIME=$(date +%s)
  echo "It takes $(($ENDTIME - $STARTTIME)) seconds to complete this task..."
fi