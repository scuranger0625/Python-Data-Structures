def add(a, b, c, n):
    # 外層迴圈，遍歷矩陣的每一行
    for i in range(n):
        # 內層迴圈，遍歷矩陣的每一列
        for j in range(n):
            # 將矩陣 a 和 b 在位置 [i][j] 的元素相加
            # 並將結果存儲到矩陣 c 的對應位置 [i][j]
            # 這裡表示：若 C = A + B，則 C[i][j] = A[i][j] + B[i][j]
            # 例如，C00 = A00 + B00，C01 = A01 + B01，依此類推
            c[i][j] = a[i][j] + b[i][j]

# 使用範例
# 假設有兩個 3x3 的矩陣 A 和 B，C = A + B 表示對應位置的元素相加
# 例如，C00 = A00 + B00 表示 C 矩陣的第一行第一列的元素等於 A 和 B 矩陣的第一行第一列元素的和
# 這個函數會遍歷矩陣中的所有元素，並將 A 和 B 的對應元素相加後存入 C 中

