# http://programmingpraxis.com/2014/09/09/drawing-diamonds/
# 
#Given a small positive integer n, write a function that draws a diamond, either filled or in outline as specified by the user. For instance, here are filled and outline diamonds for n = 5:

    #*              *
   #* *            * *
  #* * *          *   *
 #* * * *        *     *
#* * * * *      *       *
 #* * * *        *     *
  #* * *          *   *
   #* *            * *
    #*              *
#Note that there is a single space between asterisks in the filled version of the diamond.

n = 25

# Write lines for 1...5...1, this will result in 2n-1 lines
# The max widths will be n+(n-1) characters, which is to say, also 2n-1

# For l={1 to n}, then r={n-1 to 1}, write a line that is 2r-1 wide, preceded by ((2n-1)-(2r-1))/2 blank spaces
# So, 
# ((2n-1)-(2r-1))/2=n-r

# Filled
for r in range(1,n+1)+range(n-1,0,-1):
    print " "*(n-r)+" ".join(['*']*r)

# Unfilled
for r in range(1,n+1)+range(n-1,0,-1):
    line = " "*(n-r) + "*"
    if r > 1:
        line += " "*(2*r-3) + "*"
    print line
