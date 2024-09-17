# 魔術方陣規則：
# 1. 魔術方陣是一個 n x n 的方形矩陣，每行、每列以及兩條對角線的數字和都相等。
# 2. 本程式適用於奇數階的魔術方陣，使用的是“斜角法”（Siamese Method）。
# 3. 規則如下：
#    - 將數字從 1 到 n^2 依次填入方陣。
#    - 將第一個數字放在第一行的中間位置。
#    - 每次放置下一個數字時，向右上方移動一格。如果超出邊界，則繞回到方陣的另一邊。
#    - 如果目標格已經有數字，則回到上一步並向下移動一格，再繼續放置數字。
# 4. 當 n 為偶數時，會有不同的生成方法，這裡主要是針對奇數階的魔術方陣。

def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("此方法僅適用於奇數階的魔術方陣")

    magic_square = [[0] * n for _ in range(n)]

    # 初始化位置：第一行的中間
    row, col = 0, n // 2
    num = 1

    while num <= n**2:
        magic_square[row][col] = num
        num += 1

        # 下一個位置向右上移動
        new_row = (row - 1) % n
        new_col = (col + 1) % n

        # 如果目標格已經有數字，則下移一格
        if magic_square[new_row][new_col] != 0:
            row = (row + 1) % n
        else:
            row, col = new_row, new_col

    return magic_square

# 打印魔術方陣的函數
def print_magic_square(magic_square):
    n = len(magic_square)
    for row in magic_square:
        print(" ".join(f"{num:2}" for num in row))

# 測試：生成一個 5x5 的魔術方陣
n = 5
magic_square = generate_magic_square(n)
print(f"{n}x{n} 的魔術方陣：")
print_magic_square(magic_square)
