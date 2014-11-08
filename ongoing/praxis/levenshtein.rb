stringa = "Peter"
stringb = "Pilfer"

def leven(a, b)
	if a == b
		return 0
	elsif a.length == 0 or b.length == 0
		return a.length + b.length
	else
		truncA = leven(a[1..a.length], b)
		truncB = leven(a, b[1..b.length])
		truncAB = leven(a[1..a.length], b[1..b.length])
		if a[0] == b[0]
			truncAB -= 1
		end
		return 1 + [truncA, truncB, truncAB].min
	end
end

print leven(stringa, stringb)
