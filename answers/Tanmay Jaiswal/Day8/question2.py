arr = list(map(int, input("Nums(Kindly, give space after each number): ").split()))

out=[]
l=len(arr)
sum=[]
    
for i in range(l):
        for j in range(i+1,l):
            out.append((arr[i],arr[j]))
            
for i in range(int(len(out))):
    sum.append(min(out[i]) + min(out[len(out) - i - 1]))

print("Maximum possible sum is:",max(sum))
