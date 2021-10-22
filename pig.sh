#!/bin/bash

if [ $# -lt 1 ]
  then echo "Call pig.sh with <cluster_id>"
else
  STARTTIME=$(date +%s)
  gcloud dataproc jobs submit pig --cluster="$1" --file="$PWD"/pythonProject/src/PageRankPig.py --region=europe-west1
  ENDTIME=$(date +%s)
  echo "It takes $(($ENDTIME - $STARTTIME)) seconds to complete this task..."
fi

