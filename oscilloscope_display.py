import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

import pandas as pd
def test1():
    # 1. Set up the figure and axis with a dark "oscilloscope" theme
    print(plt.style.available)
    # plt.style.use('dark_background')
    fig, ax = plt.subplots()
    # fig.patch.set_facecolor('black')

    # 2. Configure axes for oscilloscope look
    # ax.set_facecolor('black')
    ax.grid(color='green', linestyle='--', linewidth=0.5)
    # ax.grid(color='green', linestyle=)
    ax.set_title('Python Simulated Oscilloscope')
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Voltage (V)')

    # 3. Initialize plot line
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x)
    line, = ax.plot(x, y, color='cyan', lw=2)

    # Set static limits for the "screen"
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlim(0, 2 * np.pi)

    # 4. Animation function
    def animate(i):
        # Simulate changing signal
        y = np.sin(x + i / 10.0)
        line.set_ydata(y)
        return line,

    # 5. Run animation
    ani = FuncAnimation(fig, animate, interval=20, blit=True)
    plt.show()

def test2():
    import matplotlib.pyplot as plt
    import numpy as np

    # Sample data
    x = np.arange(0, 10, 0.5)
    y1 = np.sin(x)
    y2 = np.cos(x) - 0.5
    y3 = np.tan(x/5)

    # 1. Create figure and axes
    fig, ax = plt.subplots()

    # 2. Plot multiple lines
    ax.plot(x, y1, label='Sine', color='blue')
    ax.plot(x, y2, label='Cosine - 0.5', color='green')
    ax.plot(x, y3, label='Tangent/5', color='red')

    # 3. Add a horizontal line at y=0
    ax.axhline(y=0, color='gray', linestyle='--', linewidth=1.5, label='Zero line')

    # 4. Add plot details (optional but recommended)
    ax.set_xlabel('X values')
    ax.set_ylabel('Y values')
    ax.set_title('Multiple Lines with a Zero Baseline')
    ax.legend() # Shows the labels for each line
    ax.grid(True, linestyle=':', alpha=0.6) # Add a grid for better readability

    # 5. Display the plot
    plt.show()

def load_excel(file:str):
    data = pd.read_html(file)
    print(data)

if __name__ == "__main__":
    load_excel("./saved_waveforms/1-c1.xls")