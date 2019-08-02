string=int(input())
if (string<=1000):
   for i in range(2,string):
       if(string %i==0):
         print("no")
         break
   else:
       print("yes")
else:
    print("no")
