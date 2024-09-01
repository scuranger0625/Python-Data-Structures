def is_big_o(f, g, c, n0):
    """
    檢查函數 f(n) 是否為 O(g(n))，即檢查是否存在常數 c 和 n0，
    使得對於所有 n >= n0，f(n) <= c * g(n)。

    這是什麼意思呢？
    Big-O 告訴我們，當輸入 n 變得很大時，f(n) 的增長速度是否不會超過 g(n) 的某個常數倍。
    換句話說，如果我們可以找到一個常數 c 和起始點 n0，從這個 n0 開始，
    無論 n 多大，f(n) 都不會超過 c 倍的 g(n)，那麼我們就可以說 f(n) 是 O(g(n))。

    這段程式碼會：
    1. 從 n0 開始，計算 f(n) 和 c * g(n)。
    2. 檢查 f(n) 是否小於或等於 c * g(n)。
    3. 如果發現 f(n) 大於 c * g(n)，就返回 False，表示 f(n) 不是 O(g(n))。
    4. 如果所有測試都通過，返回 True，表示 f(n) 是 O(g(n))。

    參數:
    f : 函數，表示 f(n)
    g : 函數，表示 g(n)
    c : 正整數常數
    n0: 正整數，表示從哪個 n0 開始不等式成立
    
    返回:
    True 如果 f(n) 是 O(g(n))
    False 如果 f(n) 不是 O(g(n))
    """
    
    n = n0
    while True:
        fn = f(n)
        cg = c * g(n)
        
        # 如果 f(n) 超過了 c * g(n)，說明不符合 Big-O 的定義
        if fn > cg:
            return False
        
        n += 1
        
        # 這裡為了簡化，設置一個測試範圍，避免無限迴圈
        if n > 10 * n0:
            break
    
    return True

# 示例使用
# 假設 f(n) = 3n + 2 和 g(n) = n
f = lambda n: 3 * n + 2
g = lambda n: n

# 我們想知道 f(n) 是否是 O(g(n))，比如設 c = 4, n0 = 2
c = 4
n0 = 2

# 測試結果
result = is_big_o(f, g, c, n0)
print("f(n) 是否是 O(g(n)):", result)
