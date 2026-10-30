#gtnel michev 100 exac parz tver@
#func verdarc true ete parz e
#i<=x/2 payman
def ArdyoqParzE(x):
    if x<2:
        return False
    i=2
    while i<=x/2:
        if x%i==0:
            return False
        i=i+1
    return True

a=[]
for i in range(0,101):
    if ArdyoqParzE(i):
        a.append(i)

for i in a:
    print(i)


