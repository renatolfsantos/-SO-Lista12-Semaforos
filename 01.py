import multiprocessing
import time
import random

sentido = None
semaforo = None

direcoes = ["NORTE -> SUL", "SUL -> NORTE","LESTE -> OESTE", "OESTE -> LESTE"]

def init(valor_sentido, s):
    global sentido
    global semaforo

    sentido = valor_sentido
    semaforo = s

def carro(id):
    global sentido
    global semaforo

    direcao = random.randint(0, 3)

    time.sleep(random.randint(1, 3))

    print(f'Carro {id} quer passar no sentido {direcoes[direcao]}')

    with semaforo:
        sentido.value = direcao
        print(f'Carro {id} passando no sentido {direcoes[sentido.value]}')

        time.sleep(2)

        print(f'Carro {id} saiu do cruzamento\n')

def main():
    j = 0
    params = [0] * 4

    valor_sentido = None
    sem = None

    valor_sentido = multiprocessing.Value('i', 0)

    for i in range(4):
        params[i] = i + 1

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)

        with multiprocessing.Pool(processes=4, initializer=init, initargs=(valor_sentido, sem)) as pool:
            pool.map(carro, params)

if __name__ == '__main__':
    main()