import psutil

def get_memory_usage():
    print(psutil.virtual_memory().percent)
