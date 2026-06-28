def veg():
	veg={"tomato":(2,50),"onion":(3,20),"chilli":(0.5,35)}
	sum=veg["tomato"][0]*veg["tomato"][1]+veg["onion"][0]*veg["onion"][1]+veg["chilli"][0]*veg["chilli"][1]
	return sum
s=veg()
print(s)
	