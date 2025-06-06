import os

def solve():
    # Знаходимо абсолютний шлях до кореня проєкту (на один рівень вище, ніж src)
    base_dir = os.path.dirname(os.path.dirname(__file__))
    input_file = os.path.join(base_dir, "ijones.in")
    output_file = os.path.join(base_dir, "ijones.out")

    with open(input_file) as f:
        W, H = map(int, f.readline().split())
        grid = [f.readline().strip().split() for _ in range(H)]

    dp = [[0] * W for _ in range(H)]
    for y in range(H):
        dp[y][0] = 1

    for x in range(W - 1):
        letter_sum = {}
        for y in range(H):
            char = grid[y][x]
            val = dp[y][x]
            if val:
                dp[y][x + 1] += val
                if char in letter_sum:
                    letter_sum[char] += val
                else:
                    letter_sum[char] = val

        for y in range(H):
            char = grid[y][x + 1]
            if char in letter_sum:
                dp[y][x + 1] += letter_sum[char]

    result = dp[0][W - 1] + dp[H - 1][W - 1]

    with open(output_file, "w") as f:
        f.write(str(result) + "\n")

if __name__ == "__main__":
    solve()
    print(f"Результат записано у {os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ijones.out')}")