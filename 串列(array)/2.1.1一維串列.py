def calculate_address_base_0(a0, i, d):
    """
    計算當索引從 0 開始的情況下，元素的記憶體地址

    :param a0: 第一個元素的基地址
    :param i: 目標元素的索引
    :param d: 每個元素佔用的空間大小
    :return: 索引 i 對應元素的記憶體地址
    """
    return a0 + i * d

def calculate_address_base_t(a0, i, t, d):
    """
    計算當索引從 t 開始的情況下，元素的記憶體地址

    :param a0: 基地址（A(t) 的地址）
    :param i: 目標元素的索引
    :param t: 串列的起始索引
    :param d: 每個元素佔用的空間大小
    :return: 索引 i 對應元素的記憶體地址
    """
    return a0 + (i - t) * d

# 範例數據
a0 = 1000  # 基地址（第一個元素的記憶體地址）
d = 4      # 每個元素佔用 4 個字節

# 情況 1: 索引從 0 開始
i = 3  # 目標元素的索引
address_base_0 = calculate_address_base_0(a0, i, d)
print(f"當索引從 0 開始時，A({i}) 的記憶體地址為: {address_base_0}")

# 情況 2: 索引從 t 開始（例如 t = 3）
t = 3  # 串列的起始索引
i = 5  # 目標元素的索引
address_base_t = calculate_address_base_t(a0, i, t, d)
print(f"當索引從 {t} 開始時，A({i}) 的記憶體地址為: {address_base_t}")
