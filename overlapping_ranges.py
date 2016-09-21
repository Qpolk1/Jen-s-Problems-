def ov_range(a_1,a_2,b_1,b_2):
	big_a=a_1
	small_a=a_2
	big_b=b_1
	small_b=b_1
	if a_1<a_2:
		big_a=a_2
		small_a=a_1
		
	elif a_1>a_2:
		big_a=a_1
		small_a=a_2
		
	if b_1>b_2:
		big_b=b_1
		small_b=b_2
		
	elif b_1<b_2:
		big_b=b_2
		small_b=b_1
	#print(big_a, '\n', small_a, '\n', big_b, '\n', small_b)

	interval_1=big_a - small_a
	interval_2=big_b - small_b
	# when they dont overlap 
	if small_a > big_b:
		return 0  
	elif small_b>big_a:
		return 0
		
	# When a dips into b	
	if big_b>big_a and small_a>small_b:
		interval_1 = big_a - small_a
		return interval_1
	
	#when b completly overlaps a	
	if big_a>big_b and small_b>small_a:
		interval_1 = big_b - small_b
		return interval_1
		
	elif big_a>big_b and big_b>small_a:
		interval_1= big_b - small_a
		return interval_1
		
	#when a overlaps in b	
	if small_b<big_a:
		interval_1=big_a - small_b
		return interval_1
		
	if small_b<big_b:
		interval_2=big_b - small_a
	#when b overlap in a
	if big_a>big_b and big_b>small_a:
		interval_1= big_b - small_a
		return interval_1

	
	#Good job 
	
	
		# Test function
def test(a1, a2, b1, b2, expected):
	print(a1, a2, '&', b1, b2, '=>',
		ov_range(a1, a2, b1, b2), '\t',
		ov_range(a1, a2, b1, b2) == expected)

test(2,5,-1,3, 1)
test(3, 0, 2, 4, 1)
test(0, 5, 0, 1000, 5)
test(0, 1000, 0, 5, 5)
test(1, 4, 0, 5, 3)
test(0, 5, 2, 4, 2)
test(2,4,0,5, 2)
test(1,10,-5,-5,0)
test(10,1,5,15,5)
test(-5, 0, 2, 4, 0)
test(-5, -5, 2, 4, 0)
test(5, 0, 1, 1, 0)
test(7, -2, -1, 4, 5)




