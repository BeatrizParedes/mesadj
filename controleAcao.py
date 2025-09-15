import threading  # vai criar e controlar as threads - cada instrumento terá uma-
import time # controla o intervalo dos sons dos instrumentos
import logging #import provisório 

# Configura o logging para mostrar só a mensagem (sem hora, sem nível)
logging.basicConfig(level=logging.INFO, format="%(message)s")

class Instrumento(threading.Thread):
    def __init__(self, nome, som, intervalo=1.0):
        super().__init__()
        self.nome = nome
        self.som = som
        self.intervalo = intervalo

        self.playing = threading.Event()
        self.stop_flag = threading.Event()
        self.playing.set()  # começa tocando

    def pause(self):
        """Pausar o instrumento"""
        self.playing.clear()

    def retomar(self):
        """Retomar o instrumento"""
        self.playing.set()

    def stop(self):
        """Parar de vez"""
        self.stop_flag.set()
        self.playing.set()  # desbloqueia se estiver pausado

    def run(self):
        while not self.stop_flag.is_set():
            self.playing.wait()  # espera se estiver pausado
            logging.info(f"{self.nome}: {self.som}")
            time.sleep(self.intervalo)


# -----------------------------
# Console interativo do DJ
# -----------------------------
if __name__ == "__main__":
    # Criando os instrumentos
    instrumentos = {
        "bateria": Instrumento("Bateria", "🥁 Bum!", intervalo=1),
        "baixo": Instrumento("Baixo", "🎸 Dum-dum!", intervalo=2),
        "sintetizador": Instrumento("Synth", "🎹 piiii!", intervalo=1.5)
    }

    # Iniciando todos
    for inst in instrumentos.values():
        inst.start()

    print("\n🎶 Console do DJ 🎶")
    print("Comandos: pause <nome>, retomar <nome>, stop <nome>, exit\n")

    while True:
        comando = input(">> ").strip().lower()

        if comando == "exit":
            print("Encerrando todos os instrumentos...")
            for inst in instrumentos.values():
                inst.stop()
            break

        partes = comando.split()
        if len(partes) != 2:
            print("Comando inválido! Use: pause <nome>, retomar <nome>, stop <nome>")
            continue

        acao, nome = partes
        if nome not in instrumentos:
            print(f"Instrumento '{nome}' não encontrado.")
            continue

        inst = instrumentos[nome]

        if acao == "pause":
            inst.pause()
            print(f"{nome.capitalize()} pausado.")
        elif acao == "retomar":
            inst.retomar()
            print(f"{nome.capitalize()} retomado.")
        elif acao == "stop":
            inst.stop()
            print(f"{nome.capitalize()} parado.")
        else:
            print("Ação desconhecida! Use: pause, retomar ou stop.")
