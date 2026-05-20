import multiprocessing
import random
import time

semaforo = None
chegada:int = 50
ordem: int = 0

def init(s, o):
    global semaforo
    global ordem

    ordem = o
    semaforo = s

def sapo(id):
    global chegada
    global semaforo
    global ordem

    max:int = 0
    pos:int = 0
    pulo:int = 0
    
    
    while pos < chegada:
        pulo = random.randint(1, 5)
        pos += pulo

        print(f"O sapo {id} pulou {pulo}cm e está em {pos}cm")
        time.sleep(0.1)

    with semaforo:
        ordem.value += 1
        print(f'O sapo {id} cruzou a linha de chegada e ficou em {ordem.value} lugar')

def main():
    ordem_atual:int = 0
    i:int = 0
    parametros:list = [0] * 5

    ordem_atual = multiprocessing.Value('i', 0)
    
    for i in range(5):
        parametros[i] = i + 1

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)

        with multiprocessing.Pool(processes=5, initializer=init, initargs=(sem, ordem_atual)) as pool:
            pool.map(sapo, parametros)

if __name__ == '__main__':
    main()