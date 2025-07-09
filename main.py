import system
import cpu
import threading
import ram
import numpy as np

# https://www.youtube.com/watch?v=rdxt6ntfX24

# https://thepythoncode.com/article/get-hardware-system-information-python

def setup():
    print("Program start...")
    # system.get_system_info()
    # cpu.get_cpu_info()
    #thread_instance = threading.Thread(target=cpu.get_cpu_usage(), args=None)
    #thread_instance.start()

def execute():
    system.plot_component_usages_graph()
    # while True:
        # system.monitor_usages_bar()


if __name__ == "__main__":
    setup()
    execute()

    #TODO fix  raise ADLError("Failed to get CurrentUsage")  pyadl.pyadl.ADLError: Failed to get CurrentUsage