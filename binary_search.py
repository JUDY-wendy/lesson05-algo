"""输入必须升序；count 统计中点探查轮数，并非所有关系运算次数。"""
def search_with_count(rates, target):
    low, high, count = 0, len(rates)-1, 0
    while low <= high:
        count += 1
        mid = (low+high)//2
        if rates[mid] == target:
            return mid, count
        if rates[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1, count

def binary_search(rates, target):
    index, count = search_with_count(rates, target)
    print(f'下标 {index}，中点探查 {count} 次')
    return index

if __name__ == '__main__':
    # 单位为基点：375 表示 3.75%，避免浮点相等问题
    rates = list(range(1, 1025))
    assert binary_search(rates, 375) == 374
    bad = [3, 1, 2]
    print('未排序翻车:', bad, '目标 3:', search_with_count(bad, 3))
    print('1024 档右端边界:', search_with_count(rates, 1024))
