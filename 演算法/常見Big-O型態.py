import math

def constant_time_operation(arr):
    # 常數型態 - O(1)
    # 無論輸入大小如何，這段代碼總是執行一次，時間複雜度為 O(1)
    return arr[0]  # 獲取第一個元素

def logarithmic_time_operation(n):
    # 對數型態 - O(log n)
    # 這段代碼的執行時間隨著 n 的增長按對數速度增長
    i = 1
    while i < n:
        i *= 2  # 每次 i 乘以 2，因此迴圈次數為 log(n)
    return i

def linear_time_operation(arr):
    # 線性型態 - O(n)
    # 這段代碼遍歷整個列表，因此時間複雜度為 O(n)
    total = 0
    for x in arr:
        total += x
    return total

def linear_logarithmic_time_operation(arr):
    # 對數線性型態 - O(n log n)
    # 這段代碼示範了一個典型的對數線性型態操作，如合併排序
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = linear_logarithmic_time_operation(arr[:mid])
    right = linear_logarithmic_time_operation(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quadratic_time_operation(arr):
    # 平方型態 - O(n^2)
    # 這段代碼使用巢狀迴圈遍歷列表中的每一對元素，時間複雜度為 O(n^2)
    n = len(arr)
    for i in range(n):
        for j in range(n):
            # 這裡進行一些操作，例如比較 arr[i] 和 arr[j]
            if arr[i] > arr[j]:
                pass  # 僅作為示範，這裡未執行實際操作
    return arr

def cubic_time_operation(arr):
    # 立方型態 - O(n^3)
    # 這段代碼使用三重巢狀迴圈，時間複雜度為 O(n^3)
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # 這裡進行一些操作，例如計算 arr[i] + arr[j] + arr[k]
                pass  # 僅作為示範，這裡未執行實際操作
    return arr

def exponential_time_operation(n):
    # 指數型態 - O(2^n)
    # 這段代碼示範了一個指數時間複雜度的遞迴操作，例如計算費氏數列
    if n <= 1:
        return n
    return exponential_time_operation(n-1) + exponential_time_operation(n-2)

def factorial_time_operation(n):
    # 階乘型態 - O(n!)
    # 這段代碼示範了一個計算排列的操作，時間複雜度為 O(n!)
    if n == 0:
        return [[]]
    prev_permutations = factorial_time_operation(n-1)
    result = []
    for perm in prev_permutations:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + [n] + perm[i:])
    return result

def power_n_time_operation(n):
    # n 的 n 次方型態 - O(n^n)
    # 這段代碼示範了一個 O(n^n) 的操作，例如生成長度為 n 的所有可能字母排列
    def helper(current, remaining):
        if len(current) == n:
            return [current]
        results = []
        for r in remaining:
            new_remaining = remaining[:]
            new_remaining.remove(r)
            results.extend(helper(current + [r], new_remaining))
        return results

    return helper([], list(range(n)))

# 範例執行
n = 4
arr = [1, 2, 3, 4]

print("常數型態:", constant_time_operation(arr))
print("對數型態:", logarithmic_time_operation(n))
print("線性型態:", linear_time_operation(arr))
print("對數線性型態:", linear_logarithmic_time_operation(arr))
print("平方型態:", quadratic_time_operation(arr))
print("立方型態:", cubic_time_operation(arr))
print("指數型態:", exponential_time_operation(n))
print("階乘型態:", factorial_time_operation(n))
print("n 的 n 次方型態:", power_n_time_operation(n))
