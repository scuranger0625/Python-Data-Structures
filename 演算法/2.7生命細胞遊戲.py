# 生命細胞遊戲規則：
# 1. 生命細胞遊戲是由英國數學家約翰·康威（John Conway）於1970年提出的，模擬生命繁衍和滅亡的過程。
# 2. 遊戲是在一個二維的網格上進行，每個單元格（細胞）有兩種狀態：存活或死亡。
# 3. 每個細胞根據以下規則進行狀態變化：
#    - 任何一個存活的細胞：
#      a. 當它周圍的活細胞數少於2個時，會因為孤立而死亡。
#      b. 當它周圍的活細胞數為2個或3個時，保持存活。
#      c. 當它周圍的活細胞數超過3個時，會因為過度擁擠而死亡。
#    - 任何一個死亡的細胞：
#      a. 當它周圍有剛好3個活細胞時，該細胞會復活。
# 4. 遊戲在不斷迭代中模擬生命的繁衍與消亡。

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 設定網格的大小
GRID_SIZE = 50

# 初始化隨機狀態
def random_grid(size):
    return np.random.choice([0, 1], size*size, p=[0.8, 0.2]).reshape(size, size)

# 計算周圍活細胞數量
def count_neighbors(grid, x, y):
    total = int(
        grid[x, (y-1)%GRID_SIZE] + grid[x, (y+1)%GRID_SIZE] +
        grid[(x-1)%GRID_SIZE, y] + grid[(x+1)%GRID_SIZE, y] +
        grid[(x-1)%GRID_SIZE, (y-1)%GRID_SIZE] + grid[(x-1)%GRID_SIZE, (y+1)%GRID_SIZE] +
        grid[(x+1)%GRID_SIZE, (y-1)%GRID_SIZE] + grid[(x+1)%GRID_SIZE, (y+1)%GRID_SIZE]
    )
    return total

# 更新網格
def update(grid):
    new_grid = grid.copy()
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            neighbors = count_neighbors(grid, i, j)
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1
    return new_grid

# 動畫顯示
def animate(frame, img, grid):
    new_grid = update(grid)
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

# 初始化網格
grid = random_grid(GRID_SIZE)

# 創建動畫
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='binary')

ani = animation.FuncAnimation(fig, animate, fargs=(img, grid), frames=10, interval=200, save_count=50)

plt.show()
