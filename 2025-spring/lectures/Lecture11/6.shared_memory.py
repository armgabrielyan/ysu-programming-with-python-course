import multiprocessing
import time


def worker(i_val, d_val, f_arr, c_val, b_arr, proc_num):
    with (
        i_val.get_lock(),
        d_val.get_lock(),
        f_arr.get_lock(),
        c_val.get_lock(),
        b_arr.get_lock(),
    ):
        i_val.value += 1
        d_val.value *= 2
        for i in range(len(f_arr)):
            f_arr[i] += 1.5
        c_val.value = b"Z"
        for i in range(len(b_arr)):
            b_arr[i] -= 1
        print(
            f"[Process {proc_num}] i={i_val.value}, d={d_val.value}, "
            f"f_arr={list(f_arr)}, c={c_val.value.decode()}, b_arr={list(b_arr)}"
        )
    time.sleep(0.1)


if __name__ == "__main__":
    # Shared memory setup
    i_val = multiprocessing.Value("i", 1)  # Integer
    d_val = multiprocessing.Value("d", 2.0)  # Double
    f_arr = multiprocessing.Array("f", [1.0, 2.0])  # Float array
    c_val = multiprocessing.Value("c", b"A")  # Char
    b_arr = multiprocessing.Array("b", [10, 20])  # (signed char) Byte array

    processes = []

    for i in range(3):
        p = multiprocessing.Process(
            target=worker, args=(i_val, d_val, f_arr, c_val, b_arr, i)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("\nFinal Values:")
    print(f"Int (i): {i_val.value}")
    print(f"Double (d): {d_val.value}")
    print(f"Float array: {list(f_arr)}")
    print(f"Char: {c_val.value.decode()}")
    print(f"Byte array: {list(b_arr)}")
