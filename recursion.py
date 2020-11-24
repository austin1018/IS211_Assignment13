

def main():
    print(fibonnaci(8))
    print(gcd(270,192))
    print(compareTo('acc','acd'))

def fibonnaci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)

def gcd(a,b):
    if min(a,b)==0:
        return max(a,b)
    else:
        r=max(a,b)%min(a,b)
        return gcd(min(a,b),r)

def compareTo(s1,s2):
    if len(s1)==0 and len(s2)==0:
        return 0
    elif len(s1)>0 and (len(s2)==0 or s1[0]>s2[0]):
        return 1
    elif len(s2)>0 and (len(s1)==0 or s1[0]<s2[0]):
        return -1
    else:
        return compareTo(s1[1:],s2[1:])

if __name__ == "__main__":
    main()
