a = 5.08
b = 5.33
c = 5.55
d = b - a
e = c - b
Compare = d - e
if Compare > 0:
	print("d is larger" )
elif Compare < 0:
       print("e is larger")
else:
	 print("d equals to e")
#population growth decelerating in Scotland




X = True
Y = False
W = X or Y
print("Result of W = X or Y:", W)
# COMMENT: W's truth table
# X=True, Y=True  → W=True
# X=True, Y=False → W=True
# X=False, Y=True → W=True
# X=False, Y=False → W=False