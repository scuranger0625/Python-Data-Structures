def sum(arr, n):
    # 初始化變數 total 為 0，用來累積總和
    total = 0
    
    # 迴圈遍歷列表 arr 的前 n 個元素
    # 這個迴圈實際上會執行 n 次，其中 i 從 0 遍歷到 n-1
    # 當 i 等於 n 時，for 敘述已經執行了 n+1 次
    # 這是因為迴圈結束前會進行最後一次檢查，確認是否終止
    for i in range(n):
        # 將 arr[i] 的值加到 total 中
        total += arr[i]
    
    # 返回總和作為函數的結果
    return total

# 使用範例
# 假設有一個列表 arr = [1, 2, 3, 4, 5] 和 n = 3
# 函數將返回 1 + 2 + 3 = 6
