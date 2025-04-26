import multiprocessing
import multiprocessing.connection
from multiprocessing import Process, Pipe
import time


def child(conn: multiprocessing.connection.Connection):
    for i in range(3):
        msg = conn.recv()
        print(f"[Child] Received: {msg}")

        reply = f"Child reply {i}"
        conn.send(reply)

        time.sleep(1)
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    p = Process(target=child, args=(child_conn,))
    p.start()

    for i in range(3):
        msg = f"Parent message {i}"
        print(f"[Parent] Sending: {msg}")
        
        parent_conn.send(msg)
        reply = parent_conn.recv()
        
        print(f"[Parent] Received: {reply}")

        time.sleep(1)

    p.join()
