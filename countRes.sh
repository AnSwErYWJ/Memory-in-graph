#!/bin/bash

if [ $# -ne 1 ];then
    echo -e "Usage: sh watchRes.sh [program]"
    exit
fi

# get pids
pids=`pidof $1`

if [ $? -ne 0 ];then
    echo -e "Usage: sh watchRes.sh [program]"
    exit
fi

: > usage.txt

while :
do
    total=0
    
    for i in $pids
    do
        
        # display content
        line=`cat /proc/$i/status | grep "VmRSS" | cut -d ":" -f2 `
        #echo ${line}

        # res value
        value=`echo ${line} | grep -o "[0-9]\+"`
        #echo ${value}

        total=$(($total+$value))
    done
    
    # get time
    h=$(date +%H)
    m=$(date +%M)
    s=$(date +%S)
    h=`awk 'BEGIN{printf "%.4f",'$h'}'`
    m=`awk 'BEGIN{printf "%.4f",('$m'/60)}'`
    s=`awk 'BEGIN{printf "%.4f",('$s'/3600)}'`
    t=`awk 'BEGIN{printf "%.4f\n",('$m'+'$s'+'$h')}'`
    #echo $s $m $h $t

    # convert kb to mb
    total=$(($total/1024))

    echo ${t} ${total} >> usage.txt

    sleep 10
done

