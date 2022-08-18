#!/bin/bash

echo This is about your session
echo User Name is `logname`
echo Current Date is `date +%d-%m-%Y`
echo The time is `date +%T`
echo Current working directory is `pwd`
echo Number of files in directory: `ls | wc -l`
echo Biggest file in current directory: `du -ah . | sort -n -r | head -1`
