import threading
import time

saldo_conta = 0
NUM_OPERACOES = 100000
lock_bancario = threading.Lock()  # Mutex compartilhado pelas 3 threads

def depositar():
    global saldo_conta
    for _ in range(NUM_OPERACOES):
        with lock_bancario:  # Secao Critica
            temp = saldo_conta
            temp = temp + 1
            saldo_conta = temp

def sacar():
    global saldo_conta
    for _ in range(NUM_OPERACOES):
        with lock_bancario:  # Secao Critica
            temp = saldo_conta
            temp = temp - 1
            saldo_conta = temp

def main():
    global saldo_conta
    print(f" [*] Saldo Inicial: {saldo_conta}")

    t1 = threading.Thread(target=depositar, name="Thread-Deposito-1")
    t2 = threading.Thread(target=depositar, name="Thread-Deposito-2")
    t3 = threading.Thread(target=sacar, name="Thread-Saque-1")

    inicio = time.time()
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    fim = time.time()

    # 2 threads depositando e 1 sacando: (2 - 1) * NUM_OPERACOES
    saldo_esperado = NUM_OPERACOES * 2 - NUM_OPERACOES
    print(f" [*] Saldo Esperado: {saldo_esperado}")
    print(f" [*] Saldo Obtido: {saldo_conta}")
    print(f" [*] Tempo de Execucao: {fim - inicio:.4f} s")

if __name__ == "__main__":
    main()
