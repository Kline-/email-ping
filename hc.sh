#!/bin/sh
DELTA=600
SFILE=/tmp/hc.timestamp
if [ -f $SFILE ] && [ $(expr $(date +%s) - $(stat -c %Y $SFILE)) -lt $DELTA ]; then
        exit 0
else
        exit 1
fi
