import random, unittest
from merge_sort import merge_sort, merge
from binary_search import search_with_count
from benchmark import bubble_sort
from experiments import nearest_payment, payment
class Checks(unittest.TestCase):
    def test_sorting(self):
        cases=[[],[1],[2,1],[1,1],[-2,0,-1],[8,3,5,1,9,2]]
        rng=random.Random(42)
        cases += [[rng.randrange(-10,11) for _ in range(n)] for n in range(100)]
        for arr in cases:
            original=arr[:]
            self.assertEqual(merge_sort(arr),sorted(arr))
            self.assertEqual(arr,original)
            self.assertEqual(bubble_sort(arr[:]),sorted(arr))
    def test_search(self):
        for n in range(65):
            a=list(range(0,2*n,2))
            for t in range(-1,2*n+1):
                i,c=search_with_count(a,t)
                self.assertEqual(i,a.index(t) if t in a else -1)
        self.assertLessEqual(search_with_count(list(range(1,1025)),375)[1],10)
    def test_loan(self):
        rates=[(100+5*i)/10000 for i in range(100)]
        for target in (0,5000,100000):
            idx,_,_=nearest_payment(rates,target)
            self.assertEqual(idx,min(range(100),key=lambda i:abs(payment(1000000,rates[i],360)-target)))
    def test_stability(self):
        class Item:
            def __init__(self,key,tag):self.key,self.tag=key,tag
            def __le__(self,other):return self.key<=other.key
        a=[Item(2,'a'),Item(1,'b'),Item(2,'c'),Item(1,'d')]
        self.assertEqual([x.tag for x in merge_sort(a)],['b','d','a','c'])
if __name__=='__main__':unittest.main(verbosity=2)
