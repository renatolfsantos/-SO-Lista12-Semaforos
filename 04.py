import multiprocessing
import time
import random

semaforo_carros = None
semaforo_times = None

def carro_andando(id_carro, id_time):
    global semaforo_times

    tempo:float = 0.0

    with semaforo_times[id_time - 1]:
        for n_volta in range (1, 4):
            print(f'O carro {id_carro} da escuderia {id_time} iniciou a {n_volta} volta')
            tempo = random.randint(100, 300)
            tempo /= 100

            time.sleep(tempo)
            print(f'O carro {id_carro} da escuderia {id_time} completou a {n_volta} volta em {tempo} segundos')

        print(f'O carro {id_carro} da escuderia {id_time} terminou a corrida')

def carro(params):
    global semaforo_carros

    id_carro = params[0]
    id_time = params[1]

    with semaforo_carros:
        carro_andando(id_carro, id_time)

def init(c, t):
    global semaforo_carros
    global semaforo_times

    semaforo_carros = c
    semaforo_times = t

def main():
    params = [0] * 14
    i:int = 0

    for i in range(14):
        if i < 7:
            params[i] = [1, i + 1]
        else:
            params[i] = [2, i - 6]

    with multiprocessing.Manager() as manager:
        times = [0] * 7
        carros = manager.Semaphore(5)

        for i in range(7):
            times[i] = manager.Semaphore(1)

        with multiprocessing.Pool(processes=14, initializer=init, initargs=(carros, times)) as pool:
            pool.map(carro, params)

if __name__ == '__main__':
    main()