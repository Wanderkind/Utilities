import math
i=1
while True:
 i+=1;l=[z**2 for z in range(i)]
 for j in range(1,i):
  K=i**2-j**2
  if K in l:
   k=round(math.sqrt(K))
   if math.gcd(j,k)==1:print(i,j,k)


# u=(j)/(i);v=(k)/(i);A=u*a-v*b;B=v*a+u*b;C=u*c-v*d;D=v*c+u*d
