def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"將圓盤 1 從 {source} 移到 {target}")
    else:
        hanoi(n - 1, source, target, auxiliary)  # 步驟 1
        print(f"將圓盤 {n} 從 {source} 移到 {target}")  # 步驟 2
        hanoi(n - 1, auxiliary, source, target)  # 步驟 3

# 範例：3 個圓盤 
hanoi(3, 'A', 'B', 'C')

# 時間複雜度
# 河內塔問題的時間複雜度是 O(2^n)，其中 n 是圓盤的數量。每多一個圓盤，操作數就會大約加倍。

# 河內塔的應用
# 河內塔問題常用於學習遞迴、資料結構、演算法分析，也可以用來理解計算機科學中的堆疊（stack）概念。
