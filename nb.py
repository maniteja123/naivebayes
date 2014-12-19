from collections import Counter as C
import math,sys

class Vocab:

    def __repr__(self):
        return 'The vocabulary'

    def __init__(self,docs):
        self.vocabs = {}
        self.vocab=C()
        self.sizes = {}
        self.number = {}
        for doc,target,num in docs:
            self.number[target] = num
            f = open(doc,'r')
            l=f.read()
            w=l.split(',')
            self.vocabs[target] = C()
            for i in w:
                self.vocabs[target].update({i.split("\'")[1]:int(i.split()[-1])})
            self.sizes[target]=sum(self.vocabs[target].values())
            self.vocab.update(self.vocabs[target])
            f.close()
        self.size = len(self.vocab.keys())
        self.total = sum(self.number.values())
        
class Naive_Bayes:

    def __init__(self,vocabulary,targets):
        self.vocab = vocabulary.vocab
        self.vocabsize = vocabulary.size
        self.vocabs = vocabulary.vocabs
        self.count = vocabulary.sizes
        self.targets = targets
        self.targ_prob = {}
        self.word_prob = {}
        self.numbers = vocabulary.number
        self.total = vocabulary.total
        self.build_naive_bayes()

    def build_naive_bayes(self):
        for target in self.targets:
            self.targ_prob[target]=float(self.numbers[target])/self.total
            self.word_prob[target]={}
            for word in self.vocab.keys():
                try:
                    self.word_prob[target][word] = float(self.vocabs[target][word]+1)/(self.count[target]+self.vocabsize)
                except KeyError:
                    self.word_prob[target][word] = float(1)/(self.count[target]+self.vocabsize)
            print len(self.word_prob[target])

    def test_naive_bayes(self,doc):
        with open(doc,'r') as f:
            w = f.read().split()
        output = None
        final = -1*sys.maxint
        for target in self.targets:
            prob = 0
            for word in w:
                if word in self.vocab.keys():
                    print target , word , self.word_prob[target][word],prob
                    prob += math.log(self.word_prob[target][word])
            prob += math.log(self.targ_prob[target])
            #print prob
            if prob > final:
                output = target
                final = prob
        print output
        
v = Vocab([('manisports.txt','s',350),('manipolitics.txt','p',450)])
print v.size
print v.sizes
f = open('testing1.txt','w+')
f.write(str(v.vocab))
n = Naive_Bayes(v,['s','p'])
n.test_naive_bayes('test.txt')
print n.word_prob['s']['test']
