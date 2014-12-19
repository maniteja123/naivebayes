with open('manibackup1.txt','r') as f:
    l=f.read()
    w=l.split(',')
    a={}
    sum=0
    print len(w)
    for i in w:
        print i.split("\'")[1]
        sum += int(i.split()[-1])
    print sum
    #print len(a.keys())
