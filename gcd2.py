def euclid_gcd(a,b):
    while (a!=b):
        if a>b:
            a=a-b
        else :
            b=b-a
    return a
         
def main():
 a =int(input())
 b=int(input())
 print(euclid_gcd(a,b))
if __name__=='__main__':
  main()