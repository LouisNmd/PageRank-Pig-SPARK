#!/bin/bash
if [ $# -lt 1 ]
  then echo "Call generateCrawl.sh with <number of URL>"
else
  STARTTIME=$(date +%s)
  python "$PWD"/pythonProject/src/genCrawl.py "$1"
  ENDTIME=$(date +%s)
  echo "It takes $(($ENDTIME - $STARTTIME)) seconds to complete this task..."
fi
