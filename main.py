import system
import multiprocessing

# https://www.youtube.com/watch?v=rdxt6ntfX24

# https://thepythoncode.com/article/get-hardware-system-information-python

# processes
P_GRAPH = 0

def setup():
    print("Program start...")
    # system.get_system_info()
    # cpu.get_cpu_info()
    #thread_instance = threading.Thread(target=cpu.get_cpu_usage(), args=None)
    #thread_instance.start()

def execute():
    running = True
    processes = [None]
    while running:
        system.print_header("Monitoring Software")
        system.print_main_options()
        running = handle_user_input(1, processes)

def handle_user_input(input_type, processes):
    user_input = int(input("Enter Decision ->: "))
    # input type for type of options to display?
    if input_type == 1:
        return main_menu_options(user_input, processes)

def terminate_existing_process(processes, p_type):
    p = processes[p_type]
    assert isinstance(p, multiprocessing.process.BaseProcess)
    p.terminate()
    processes[p_type] = None
    return processes

def main_menu_options(input, processes):
    if input == 1:
        if processes[P_GRAPH] is None:
            p = multiprocessing.Process(target=system.plot_component_usages_graph())
            p.start()
            processes[P_GRAPH] = p
        else:
            print("Reopening graph process")
            processes = terminate_existing_process(processes, P_GRAPH)
            p = multiprocessing.Process(target=system.plot_component_usages_graph())
            processes[P_GRAPH] = p
    elif input == 2:
        print("join graph process")
        if processes[P_GRAPH] is not None:
            p = processes[P_GRAPH]
            assert isinstance(p, multiprocessing.process.BaseProcess)
            p.join()
    elif input == 3:
        print("Implement ram manipulation")
    elif input == 4:
        print("Shutting down")
        return False

    return True


if __name__ == "__main__":
    setup()
    execute()