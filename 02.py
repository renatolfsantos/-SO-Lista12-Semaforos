import multiprocessing
import time
import random

semaforo = None
pos_porta:int = 200

def init(s):
    global semaforo
    semaforo = s

def pessoa(id):
    global pos_porta
    global semaforo

    pos_atual:int = 0
    passo:int = 0

    while pos_atual < pos_porta:
        print(f"A pessoa {id} está em {pos_atual} metros")

        passo = random.randint(4, 6)
        pos_atual += passo

        time.sleep(0.1)
        
    
    print(f"A pessoa {id} chegou na porta\n")

    with semaforo:
        print(f"A pessoa {id} está abrindo a porta")

        time.sleep(random.randint(1, 2))

        print(f"A pessoa {id} passou pela porta\n")

def main():
    i:int = 0
    params = [0] * 4

    for i in range(4):
        params[i] = i + 1

    with multiprocessing.Manager() as manager:
        sem = multiprocessing.Semaphore(1)

        with multiprocessing.Pool(processes=4, initializer=init, initargs=(sem, )) as pool:
            pool.map(pessoa, params)

if __name__ == '__main__':
    main()