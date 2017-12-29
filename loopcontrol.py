#!/usr/bin/python
#author:murali
#pupose:find sum and avg using loop control statements
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
