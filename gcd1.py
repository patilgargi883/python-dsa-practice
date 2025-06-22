def gcd (a,b):
  min = 0
  if a<b :
    min =a
  else:
    min =b 
    
  for i in range(min,0,-1):
      if (a%i==0 and b%i==0):
         return i 
         
def main():
 a =int(input())
 b=int(input())
 print(gcd(a,b))
if __name__=='__main__':
  main()