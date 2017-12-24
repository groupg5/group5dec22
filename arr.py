#!/usr/bin/python
#author:murali
#purpose:average and sum of numbers using array
arr=[1,2,3,0,4]
sum=0
cnt=0
for var in (arr):
 cnt=cnt+1
 if(var==0):
  continue
 sum=sum+var
print sum
avg=sum/cnt
print avg

