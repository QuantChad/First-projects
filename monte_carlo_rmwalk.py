import random
import matplotlib.pyplot as plt  # Correct import

def random_walk(n):
    """Return list of (x, y) coordinates after each step."""
    x = 0
    y = 0
    walk = [(x, y)]
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        elif step == 'W':
            x -= 1
        walk.append((x, y))
    return walk

if __name__ == '__main__':
    steps = 1000
    walk = random_walk(steps)
    x_vals, y_vals = zip(*walk)  

    plt.figure(figsize=(8, 8))
    plt.plot(x_vals, y_vals, marker='o', markersize=3)
    plt.title(f"2D Random Walk ({steps} steps)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.scatter([0], [0], c='green', label='Start')  # Start point
    plt.scatter([x_vals[-1]], [y_vals[-1]], c='red', label='End')  # End point
    plt.legend()
    plt.show()
    
