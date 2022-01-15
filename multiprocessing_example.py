from multiprocessing import Process

def func1():
    counter = 0
    print("start func 1")
    while counter < 100:
        counter += 1
        print("func 1", counter)
    print("end func 1")

def func2():
    counter = 0
    print("start func 2")
    while counter < 100:
        counter += 1
        print("func 2", counter)
    print("end func 2")

if __name__ == "__main__":
    p1 = Process(target = func1)
    p2 = Process(target = func2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()