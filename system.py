import time
import random
from itertools import count

import psutil
import platform
from datetime import datetime
import os
import yaml
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.animation import FuncAnimation

UNIT_SIZES = ["", "K", "M", "G", "T", "P"]

# some details for yaml file
CONFIG = "config.yaml"
CONSTANTS = "constants"
PROGRESS_BAR = "progress_bar"

# components
CPU = "cpu"
RAM = "ram"

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in UNIT_SIZES:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def get_system_info():
    print("=" * 40, "System Information", "=" * 40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

    print("=" * 40, "Boot Time", "=" * 40)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

def display_usage(component, usage, should_clear_line=False, bars=50):
    # https://www.youtube.com/watch?v=rdxt6ntfX24
    bar_percent = usage/100.0
    bars_complete = int(bar_percent * bars)
    bar = '█' * bars_complete + '-' * (bars - bars_complete)
    if should_clear_line:
        print(f"{component} usage: |{bar}| {usage:.2f}%  ", end="")
    else:
        print(f"{component} usage: |{bar}| {usage:.2f}%  ", end="\n")

def monitor_usages_bar():
    max_progress_bar = 30
    try:
        with open(os.getcwd() + "\\" + CONFIG, 'r') as file:
            data = yaml.safe_load(file)
            max_progress_bar = data[CONSTANTS][PROGRESS_BAR]
    except FileNotFoundError:
        print("config file not found in current working directory, please create config.yaml file and add the details")
    except Exception as exc:
        print(f"unexpected exception occurred: {exc}")

    while True:
        ram_usage = psutil.virtual_memory().percent
        cpu_usage = psutil.cpu_percent()
        display_usage(RAM, ram_usage, True, max_progress_bar)
        display_usage(CPU, cpu_usage,False, max_progress_bar)
        time.sleep(0.5)

def plot_component_usages_graph():
    # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
    # plt.style.use('fivethirtyeight')
    fig, (ram_chart, cpu_chart) = plt.subplots(2)
    fig.suptitle('PC Components Usages')

    x_vals = []
    ram_usage = []
    cpu_usage = []

    index = count()

    def plot_chart(chart, usage, title):
        chart.cla()
        chart.set_ylim(0, 100.0)
        chart.plot(x_vals, usage)
        chart.set_title(title)
        chart.set_xlabel("")
        chart.set_ylabel("Percent %")
        chart.get_xaxis().set_visible(False)


    def animate(i):
        x_vals.append(next(index)) # count
        ram_usage.append(psutil.virtual_memory().percent)
        cpu_usage.append(psutil.cpu_percent())

        # https://www.youtube.com/watch?v=Ercd-Ip5PfQ
        plot_chart(ram_chart, ram_usage, 'Memory')
        plot_chart(cpu_chart, cpu_usage, 'CPU')

    # get current figure gcf
    ani = FuncAnimation(plt.gcf(), animate, interval=250, cache_frame_data=False)

    plt.title("Changing Line Graph")
    plt.tight_layout()
    plt.show()



