def euclid_gcd(a,b):
    while (a!=0 and b!=0):
        if a>b:
            a=a%b
        else :
            b=b%a
    if a!=0:
        return a
    else:
        return b
         
def main():
 a =int(input())
 b=int(input())
 print(euclid_gcd(a,b))
 
if __name__=='__main__':
  main()