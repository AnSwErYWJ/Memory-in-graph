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

: > usage.txt # for graph,empty file
echo "time        memory" > raw.log # for admin

while :
do
    total=0
    
    for i in $pids # mutil process, same name
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
    
    # transform for usage.txt
    H=`awk 'BEGIN{printf "%.4f",'$h'}'`
    M=`awk 'BEGIN{printf "%.4f",('$m'/60)}'`
    S=`awk 'BEGIN{printf "%.4f",('$s'/3600)}'`
    t=`awk 'BEGIN{printf "%.4f\n",('$M'+'$S'+'$H')}'`
    #echo $s $m $h $t
    total=$(($total/1024))

    echo ${t} ${total} >> usage.txt
    echo ${h}:${m}:${s} "   "${total}m >> raw.log

    sleep 10 # interval
done

