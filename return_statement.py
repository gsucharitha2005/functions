def sum(a,b):
	c=a+b
	return c
s=sum(10,20)
print(s)

print("______")
def sum(a,b):
	c=a+b
	return c
print(sum(10,20))

print("________")
def mul(s,j):
	c=s*j
	return c
print(mul(1,3))

print("________")
def cloths_price_cal(original,discount):
	discount_price=original*(discount / 100)
	final_price=original-discount_price
	return final_price
bill=cloths_price_cal(200,15)
print(bill)

print("_______")
def even_num():
	num=int(input("enter number:"))
	if num%2==0:
		print("even number")
	else:
		print("odd number")
even_num()
even_num()

print("________")
def even_num(num):
	
	if num%2==0:
		print("even number")
	else:
		print("odd number")
even_num(12)
even_num(13)
	


	
