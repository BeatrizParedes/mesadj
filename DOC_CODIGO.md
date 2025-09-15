# Mesa de DJ Interativa - Guia Completo

## 1️⃣ Bibliotecas Importadas

```python
import threading
import numpy as np
import pygame
import time
import os
```

* `threading`: permite criar vários “trabalhadores” (threads) que funcionam ao mesmo tempo.
* `numpy`: usado para criar sons do zero, gerando ondas sonoras.
* `pygame`: biblioteca que toca os sons.
* `time`: serve para pausar o programa por alguns segundos (`sleep`).
* `os`: usado para limpar a tela do terminal.

## 2️⃣ Inicialização do Som

```python
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
```

* Prepara o sistema de áudio.
* `frequency=44100`: qualidade do som.
* `size=-16`: 16 bits.
* `channels=2`: estéreo.
* `buffer=512`: ajuda o som a tocar sem travar.

## 3️⃣ Função para Criar Sons

```python
def criar_som(frequencia=440, duracao=500, volume=0.5):
    sample_rate = 44100
    n_samples = int(sample_rate * duracao / 1000)
    t = np.linspace(0, duracao / 1000, n_samples, False)
    onda = np.sin(frequencia * 2 * np.pi * t)
    onda = (onda * 32767 * volume).astype(np.int16)
    return pygame.sndarray.make_sound(np.column_stack([onda, onda]))
```

* Cria sons simples como instrumentos.
* `frequencia`: altura do som (grave/agudo).
* `duracao`: tempo do som.
* `volume`: intensidade do som.

## 4️⃣ Classe da Faixa (Instrumento)

```python
class InstrumentoThread(threading.Thread):
    def __init__(self, nome, frequencia):
        super().__init__()
        self.nome = nome
        self.frequencia = frequencia
        self.som = criar_som(frequencia, 300)
        self.tocando = False
        self.pausado = False
        self.lock = threading.Lock()
        self.running = True
```

* Cada instrumento é uma thread.
* `tocando`: True se o som estiver ligado.
* `pausado`: True se o som estiver pausado.
* `lock`: evita conflitos entre threads.
* `running`: True enquanto a thread estiver ativa.

## 5️⃣ Loop da Thread

```python
    def run(self):
        while self.running:
            with self.lock:
                if self.tocando and not self.pausado:
                    self.som.play()
            time.sleep(0.3)
```

* Executa continuamente enquanto a thread estiver ativa.
* Toca o som somente se estiver ligado e não pausado.
* `sleep(0.3)`: intervalo entre batidas.

## 6️⃣ Funções da Thread

```python
    def toggle(self):
        with self.lock:
            self.tocando = not self.tocando
            if not self.tocando:
                self.som.stop()

    def pausar(self):
        with self.lock:
            self.pausado = not self.pausado
            if self.pausado:
                self.som.stop()

    def parar(self):
        with self.lock:
            self.running = False
            self.som.stop()
```

* `toggle()`: liga/desliga a faixa.
* `pausar()`: pausa ou retoma sem desligar.
* `parar()`: encerra a thread com segurança.

## 7️⃣ Criando os Instrumentos

```python
instrumentos = {
    "1": InstrumentoThread("Bumbo", 100),
    "2": InstrumentoThread("Caixa", 200),
    "3": InstrumentoThread("Chimbal", 400),
    "4": InstrumentoThread("Sintetizador", 600),
}
for inst in instrumentos.values():
    inst.start()
```

* Cada faixa tem número, nome e frequência.
* Threads iniciam e ficam prontas para tocar.

## 8️⃣ Menu Interativo

```python
def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"🎧 Mesa de DJ Interativa 🎛️")
    for k, inst in instrumentos.items():
        status = "🎶 Tocando" if inst.tocando else "OFF"
        pause_status = " (Pausado)" if inst.pausado else ""
        print(f"[{k}] {inst.nome} - {status}{pause_status}")
    print("\n[P] Parar todas as faixas")
    print("[Q] Sair da mesa\n")
```

* Limpa a tela e mostra status de cada faixa.
* Mostra opções para o usuário.

## 9️⃣ Loop Principal do DJ

```python
while True:
    mostrar_menu()
    escolha = input("👉 Sua escolha: ").strip().upper()

    if escolha in instrumentos:
        instrumentos[escolha].toggle()
    elif escolha == "P":
        for inst in instrumentos.values():
            inst.tocando = False
            inst.pausado = False
            inst.som.stop()
    elif escolha == "Q":
        for inst in instrumentos.values():
            inst.parar()
        print("👋 Saindo da Mesa de DJ.")
        break
    else:
        print("❌ Opção inválida! Tente de novo.")
        time.sleep(0.8)
```

* Recebe a escolha do usuário e controla as faixas.
* `[1-4]`: liga/desliga a faixa.
* `P`: para todas as faixas.
* `Q`: encerra o programa.
* Entrada inválida gera aviso.

## ✅ Resumo Simples

* Cada instrumento é uma thread independente.
* Threads podem tocar, pausar ou parar sem atrapalhar outras faixas.
* Menu no terminal mostra status de todas as faixas em tempo real.
* Locks (`threading.Lock`) evitam conflitos entre threads.
* Sons são gerados pelo NumPy e tocados pelo Pygame, sem arquivos externos.
