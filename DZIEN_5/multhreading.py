import threading

def worker(num,shared_variable):
    shared_variable.append(num)
    print(f'Wątek {threading.current_thread().name} dodał {num} do zmiennej współdzielonej!')


schared_variable = []
threads = []

for i in range(5):
    t = threading.Thread(target=worker,args=(i,schared_variable,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"zmienna współdzielona po zakończeniu pracy wątków: {schared_variable}")
