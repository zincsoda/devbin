target = 5
ways=[1]+[0]*target
coins =[1,2,5,10,20,50,100,200]

for coin in coins:
    print "Using coin ", coin
    for i in range(coin,target+1):
        print "Consider ", i
        print "ways[i] or ways[%d] = %d" % (i, ways[i])
        print "ways[i-coin] or ways[%d] = %d" %(i-coin,ways[i-coin])
        ways[i] += ways[i-coin]
        print "ways[i] or ways[%d] = %d" % (i, ways[i])


print ways[target]
