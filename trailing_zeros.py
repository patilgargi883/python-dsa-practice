def trailing_zeros(n):
    res = 0
    pow_of_5=5 
    while n>=pow_of_5 :
        
       res+=(n//pow_of_5)
       pow_of_5=pow_of_5*5 
    return res
         
def main():
    n=int(input())
    print(trailing_zeros(n))
    
if __name__=='__main__':
    main()