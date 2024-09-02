arr=[0,2,6,8]
n=len(arr)1
sum_of_n=n*(n+1)/2
current_sum=sum(arr)
missing_num=sum_of_n-current_sum
print(int(missing_num))