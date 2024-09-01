def search(data, target, n):
    # 迴圈從索引 0 開始，遍歷列表 data 中的每一個元素，直到索引 n-1
    for i in range(n):
        # 檢查列表中的當前元素 (data[i]) 是否等於 target
        if target == data[i]:
            # 如果找到與 target 相等的元素，返回該元素的索引 i，並結束搜尋
            return i
    
    # 如果遍歷了整個列表仍未找到 target，函數默認返回 None
    # 注意：這裡沒有明確寫出 return None，但如果沒有找到，Python 會自動返回 None

# 示例使用
data = [10, 22, 35, 41, 55]
target = 35
n = len(data)

# 調用 search 函數
result = search(data, target, n)
print("元素索引:", result)  # 如果找到，輸出元素的索引；如果找不到，輸出 None
