def arm(n):
    t=0
    while(n>0):
        rem=n%10
        n=n/10
        t+=(rem**3)
        if n==t:
            return True
        return False

n=121
if(arm(n)):
    print(n,"Armstrong number")
else:
    print(n,"Not Armstrong number")
