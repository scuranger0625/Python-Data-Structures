#   假若有一個二維串列是A[0:u1-1,0:u2-1]，表示此串列有u1列及u2行;也就是每一列是由u2個元素組成。二維串列化為一維串列時，
#   對應的方法有兩種:(1)以列為主，(2)以行為主


#   以列為主: 
#   視此串列有u1個元素0，1，2，.....，u1-1，每一元素有u2個單位，每個單位佔d個空間
#   A(i,j)=a0+i*u2*d+j*d

#   以行為主:
#   視此串列有u2個元素0，1，2，.....，u1-1，每一元素有u1個單位，每個單位佔d個空間
#   A(i,j)=a0+j*u1*d+i*d

def address_row_major(a0, i, j, u2, d):
    """
    計算二維串列以列為主（Row-Major Order）存儲時的地址

    :param a0: 起始地址（基地址）
    :param i: 目標元素的行索引
    :param j: 目標元素的列索引
    :param u2: 二維串列的列數
    :param d: 每個元素佔用的空間大小
    :return: 二維串列元素 A[i][j] 在一維記憶體中的地址
    """
    # 計算公式: A(i,j) = a0 + i * u2 * d + j * d
    address = a0 + i * u2 * d + j * d
    return address

def address_column_major(a0, i, j, u1, d):
    """
    計算二維串列以行為主（Column-Major Order）存儲時的地址

    :param a0: 起始地址（基地址）
    :param i: 目標元素的行索引
    :param j: 目標元素的列索引
    :param u1: 二維串列的行數
    :param d: 每個元素佔用的空間大小
    :return: 二維串列元素 A[i][j] 在一維記憶體中的地址
    """
    # 計算公式: A(i,j) = a0 + j * u1 * d + i * d
    address = a0 + j * u1 * d + i * d
    return address

# 範例數據設置
a0 = 1000  # 基地址，假設為 1000
u1 = 3     # 行數（例如，有 3 行）
u2 = 4     # 列數（例如，有 4 列）
d = 4      # 每個元素佔用 4 個字節（例如，整數類型）

# 目標元素的位置
i = 1  # 第 2 行（索引從 0 開始）
j = 2  # 第 3 列（索引從 0 開始）

# 計算以列為主時 A[i][j] 的地址
address_r = address_row_major(a0, i, j, u2, d)
print(f"以列為主時，A[{i}][{j}] 的地址為: {address_r}")
# 預期輸出: 以列為主時，A[1][2] 的地址為: 1024
# 計算過程:
# A(1,2) = 1000 + 1*4*4 + 2*4 = 1000 + 16 + 8 = 1024

# 計算以行為主時 A[i][j] 的地址
address_c = address_column_major(a0, i, j, u1, d)
print(f"以行為主時，A[{i}][{j}] 的地址為: {address_c}")
# 預期輸出: 以行為主時，A[1][2] 的地址為: 1016
# 計算過程:
# A(1,2) = 1000 + 2*3*4 + 1*4 = 1000 + 24 + 4 = 1028

# 進一步示範其他元素的地址計算
elements = [(0,0), (0,3), (2,1), (2,3)]

print("\n以列為主（Row-Major Order）存儲時的地址計算:")
for (row, col) in elements:
    addr = address_row_major(a0, row, col, u2, d)
    print(f"A[{row}][{col}] 的地址為: {addr}")

print("\n以行為主（Column-Major Order）存儲時的地址計算:")
for (row, col) in elements:
    addr = address_column_major(a0, row, col, u1, d)
    print(f"A[{row}][{col}] 的地址為: {addr}")
