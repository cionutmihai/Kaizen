import os
import signal
import psutil
import time

def kill_proc_tree(pid, sig=signal.SIGTERM, include_parent=True,
                   timeout=None, on_terminate=None):

    assert pid != os.getpid(), "won't kill myself"
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    if include_parent:
        children.append(parent)
    for p in children:
        p.send_signal(sig)
    gone, alive = psutil.wait_procs(children, timeout=timeout,
                                    callback=on_terminate)
    return (gone, alive)

def main():

    start = time.time()
    pid = int(input("Enter pid of the process tree you wish to terminate: "))
    kill_proc_tree(pid)
    print("Process tree terminated.")
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    main()
