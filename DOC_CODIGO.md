# Mesa de DJ Interativa - Guia Completo

## 1️⃣ Bibliotecas Importadas

```python
import threading
import pygame
import time
import os
```

* `threading`: permite criar várias threads para tocar sons simultaneamente.
* `pygame`: biblioteca que toca sons a partir de arquivos `.wav`.
* `time`: usado para pausas (`sleep`) no loop principal.
* `os`: manipula caminhos de arquivos e pastas.

---

## 2️⃣ Inicialização do Som

```python
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(8)
```

* Inicializa o mixer do Pygame para tocar múltiplos sons simultaneamente.
* `frequency=44100`: qualidade do áudio.
* `size=-16`: 16 bits.
* `channels=2`: estéreo.
* `buffer=512`: evita travamentos no som.
* `set_num_channels(8)`: permite até 8 canais simultâneos.

---

## 3️⃣ Classe do Instrumento

```python
class InstrumentoThread(threading.Thread):
    channel_index = 0

    def __init__(self, nome, arquivo_mp3):
        super().__init__()
        self.nome = nome
        self.arquivo = arquivo_mp3
        self.som = pygame.mixer.Sound(arquivo_mp3)
        self.tocando = False
        self.pausado = False
        self.lock = threading.Lock()
        self.running = True

        self.channel = pygame.mixer.Channel(InstrumentoThread.channel_index)
        InstrumentoThread.channel_index += 1
```

* Cada instrumento é uma thread independente.
* `tocando`: indica se o som está ativo.
* `pausado`: indica se a faixa está pausada.
* `lock`: evita conflitos entre threads.
* `channel`: canal específico do Pygame para cada instrumento.

---

## 4️⃣ Loop da Thread

```python
def run(self):
    while self.running:
        with self.lock:
            if self.tocando and not self.pausado:
                if not self.channel.get_busy():
                    self.channel.play(self.som, loops=-1)
        time.sleep(0.2)
```

* Executa continuamente enquanto a thread estiver ativa.
* Reproduz o som se estiver tocando e não estiver pausado.
* `loops=-1` toca o som em loop infinito.
* `sleep(0.2)` evita sobrecarga do processador.

---

## 5️⃣ Funções do Instrumento

```python
def play(self):
    with self.lock:
        if self.pausado:
            self.channel.unpause()
            self.pausado = False
        else:
            self.channel.play(self.som, loops=-1)
        self.tocando = True

def pausar(self):
    with self.lock:
        if self.tocando:
            if not self.pausado:
                self.channel.pause()
                self.pausado = True
            else:
                self.channel.unpause()
                self.pausado = False

def parar(self):
    with self.lock:
        self.channel.stop()
        self.tocando = False
        self.pausado = False
        self.running = False
```

* `play()`: toca ou retoma a faixa.
* `pausar()`: pausa ou retoma a faixa sem reiniciar.
* `parar()`: interrompe totalmente a faixa e encerra a thread.

---

## 6️⃣ Criando os Instrumentos

```python
pasta_stems = os.path.join(os.path.dirname(__file__), "stems")

instrumentos = {
    "baixo": InstrumentoThread("Baixo", os.path.join(pasta_stems, "Clocks_coldplay_bass.wav")),
    "bateria": InstrumentoThread("Bateria", os.path.join(pasta_stems, "Clocks_coldplay_drums.wav")),
    "guitarra": InstrumentoThread("Guitarra", os.path.join(pasta_stems, "Clocks_coldplay_guitar.wav")),
    "piano": InstrumentoThread("Piano", os.path.join(pasta_stems, "Clocks_coldplay_piano.wav")),
    "voz": InstrumentoThread("Voz", os.path.join(pasta_stems, "Clocks_coldplay_vocals.wav"))
}

for inst in instrumentos.values():
    inst.start()
```

* Cada instrumento recebe um arquivo `.wav`.
* Threads são iniciadas, prontas para tocar.

---

## 7️⃣ Menu Interativo

```python
print("\n🎛️ Console do DJ")
print("Comandos:")
print("  play <nome>   - tocar instrumento")
print("  pause <nome>  - pausar/resumir instrumento")
print("  stop <nome>   - parar instrumento")
print("  all play      - tocar todos os instrumentos")
print("  all stop      - parar todos os instrumentos")
print("  sair          - sair do programa")
print("Instrumentos disponíveis:", ", ".join(instrumentos.keys()))
```

* O usuário digita comandos para controlar cada faixa ou todos os instrumentos.
* `all play` e `all stop` controlam todos os instrumentos simultaneamente.

---

## 8️⃣ Loop Principal do DJ

```python
try:
    while True:
        comando = input("> ").strip().lower().split()

        if not comando:
            continue

        acao = comando[0]

        if acao == "sair":
            break

        if acao == "all":
            if len(comando) < 2:
                print("Use: all play / all stop")
                continue
            if comando[1] == "play":
                for inst in instrumentos.values():
                    inst.play()
            elif comando[1] == "stop":
                for inst in instrumentos.values():
                    inst.parar()
            continue

        if len(comando) < 2:
            print("Use: play/pause/stop <nome>")
            continue

        nome = comando[1]
        if nome not in instrumentos:
            print("Instrumento inválido.")
            continue

        inst = instrumentos[nome]

        if acao == "play":
            inst.play()
        elif acao == "pause":
            inst.pausar()
        elif acao == "stop":
            inst.parar()
        else:
            print("Ação desconhecida.")

except KeyboardInterrupt:
    pass

finally:
    for i in instrumentos.values():
        i.parar()
    for i in instrumentos.values():
        i.join()
    pygame.mixer.quit()
    print("👋 Saindo da Mesa de DJ.")
```

* Recebe e interpreta os comandos do usuário.
* Permite tocar, pausar e parar instrumentos individuais ou todos ao mesmo tempo.
* Ao sair, encerra todas as threads e libera o mixer do Pygame.

---

## ✅ Resumo Final

* Cada instrumento é uma thread independente.
* Suporta tocar, pausar e parar instrumentos individualmente ou todos juntos.
* Menu interativo em texto no terminal.
* `threading.Lock` garante segurança entre threads.
* Sons são arquivos `.wav` externos carregados pelo Pygame.
* Permite criar uma **mesa de DJ interativa** totalmente funcional no console.
