"""带深度观测的合并排序；根结点深度为 0。"""
def merge(a, b):
    result, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:  # 相等时先取左侧，保证稳定性
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:]); result.extend(b[j:])
    return result

def merge_sort(nums, *, observer=None, _depth=0):
    if observer is not None:
        observer(_depth, len(nums))
    if len(nums) <= 1:  # 基准情形
        return list(nums)
    # 分解 Divide：中点切分为两个更小的问题
    mid = len(nums) // 2
    # 解决 Conquer：分别递归排序
    left = merge_sort(nums[:mid], observer=observer, _depth=_depth+1)
    right = merge_sort(nums[mid:], observer=observer, _depth=_depth+1)
    # 合并 Combine：双指针合并两个有序子段
    return merge(left, right)

if __name__ == '__main__':
    print(merge_sort([8, 3, 5, 1, 9, 2]))
    depths = []
    merge_sort(list(range(8000, 0, -1)), observer=lambda d,n: depths.append(d))
    print('8000 元素最大递归边深度:', max(depths))
