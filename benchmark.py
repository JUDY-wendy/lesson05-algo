"""固定种子、每档三次 timeit，原始读数和环境保存在 results/。"""
import csv, json, platform, random, statistics, sys, timeit
from pathlib import Path
from merge_sort import merge_sort

def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def main():
    out=Path(__file__).parent/'results'; out.mkdir(exist_ok=True)
    rng=random.Random(20261018); rows=[]
    for n in (1000,2000,4000,8000):
        arr=[rng.randint(0,100000) for _ in range(n)]
        expected=sorted(arr); row={'n':n}
        for name,fn in [('bubble',bubble_sort),('merge',merge_sort),('sorted',sorted)]:
            assert fn(arr[:]) == expected
            samples=timeit.repeat(lambda:fn(arr[:]),repeat=3,number=1)
            row[name+'_samples']=samples
            row[name]=statistics.mean(samples)
        rows.append(row); print(row,flush=True)
    data={'seed':20261018,'repeats':3,'python':sys.version,'platform':platform.platform(),
          'timer':'timeit.repeat number=1, input copy included','rows':rows}
    (out/'benchmark.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    with (out/'benchmark.csv').open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.writer(f); w.writerow(['n','bubble_s','merge_s','sorted_s','bubble/merge'])
        for r in rows:w.writerow([r['n'],r['bubble'],r['merge'],r['sorted'],r['bubble']/r['merge']])
if __name__=='__main__':main()
