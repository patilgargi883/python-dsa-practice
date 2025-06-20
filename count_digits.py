def count_digits(n):
    count = 0
    while n>0:
        n=n//10
        count+=1
    return count
def main():
    n=int(input())
    print(count_digits(n))
if __name__=='__main__':
    main()