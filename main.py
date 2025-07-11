import system
import cpu
import threading
import ram
import numpy as np

# https://www.youtube.com/watch?v=rdxt6ntfX24

# https://thepythoncode.com/article/get-hardware-system-information-python

# threads
THD_GRAPH = 0

def setup():
    print("Program start...")
    # system.get_system_info()
    # cpu.get_cpu_info()
    #thread_instance = threading.Thread(target=cpu.get_cpu_usage(), args=None)
    #thread_instance.start()

def execute():
    threads = [None]
    running = True
    while running:
        system.print_header("Monitoring Software")
        system.print_main_options()
        running = handle_user_input(1, threads)

def handle_user_input(input_type, threads):
    user_input = int(input("Enter Decision ->: "))
    if input_type == 1:
        return main_menu_options(user_input, threads)

def main_menu_options(input, threads):
    if input == 1:
        thd_graph = threading.Thread(target=system.plot_component_usages_graph(), args=None)
        if threads[THD_GRAPH] is not None:
            print("Monitor is already open")
        else:
            threads[THD_GRAPH] = thd_graph
            thd_graph.start()
    elif input == 2:
        print("Implement ram manipulation")
    elif input == 3:
        print("Cleaning up thread if it exists")
        if threads[0] is not None:
            threads[0].join()
    else:
        return False

    return True


if __name__ == "__main__":
    setup()
    execute()