def mul(a, b, c, n):
    # 外層迴圈，遍歷矩陣 c 的每一行
    for i in range(n):
        # 內層迴圈，遍歷矩陣 c 的每一列
        for j in range(n):
            # 初始化 sum 變數為 0，用來累加 a 的第 i 行與 b 的第 j 列的乘積和
            sum = 0
            # 第三層迴圈，遍歷 a 的第 i 行和 b 的第 j 列
            for k in range(n):
                # 將 a[i][k] 與 b[k][j] 相乘，並將結果累加到 sum 中
                sum += a[i][k] * b[k][j]
            # 將累加的結果 sum 存儲到矩陣 c 的位置 [i][j]
            # 這表示矩陣 C 的元素 c[i][j] 是 A 的第 i 行和 B 的第 j 列的乘積之和
            c[i][j] = sum

# 使用範例
# 假設有兩個 3x3 的矩陣 A 和 B，C = A * B 表示 A 和 B 的矩陣相乘
# C[i][j] 表示 A 的第 i 行和 B 的第 j 列的對應元素相乘並累加的結果
# 例如，如果 i = 0, j = 0，則 C00 = A00 * B00 + A01 * B10 + A02 * B20
