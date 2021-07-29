## bubble sort 
arr=[1,2,13,4,1230,12,54,1,64,4]
for i in range(len(arr)):
	for j in range(0,len(arr)-i-1):
		#print(len(arr)-i-1)
		if(arr[j]>arr[j+1]):
			temp=arr[j+1]
			arr[j+1]=arr[j]
			arr[j]=temp

