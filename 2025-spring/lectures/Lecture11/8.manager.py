from multiprocessing import Process, Manager


def worker(shared_dict: dict, shared_list: list, index: int):
    # Update shared dictionary
    shared_dict[index] = f"Process-{index}"
    # Append to shared list
    shared_list.append(index)


if __name__ == "__main__":
    with Manager() as manager:
        shared_dict = manager.dict() # Proxy for shared dictionary
        shared_list = manager.list() # Proxy for shared list

        processes = []
        for i in range(5):
            p = Process(target=worker, args=(shared_dict, shared_list, i))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        print("Final shared dict:", dict(shared_dict))
        print("Final shared list:", list(shared_list))
