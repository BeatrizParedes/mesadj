import threading
import numpy as np
import pygame
import time
import os

# Inicializa o mixer do Pygame
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

# Função para criar sons programaticamente
def criar_som(frequencia=440, duracao=500, volume=0.5):
    sample_rate = 44100
    n_samples = int(sample_rate * duracao / 1000)
    t = np.linspace(0, duracao / 1000, n_samples, False)
    onda = np.sin(frequencia * 2 * np.pi * t)
    onda = (onda * 32767 * volume).astype(np.int16)
    return pygame.sndarray.make_sound(np.column_stack([onda, onda]))

# --- Classe Thread para cada instrumento ---
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

    def run(self):
        while self.running:
            # Apenas toca se não estiver pausado
            with self.lock:
                if self.tocando and not self.pausado:
                    self.som.play()
            time.sleep(0.3)  # Simula BPM / intervalo entre batidas

    # Ligar/desligar faixa
    def toggle(self):
        with self.lock:
            self.tocando = not self.tocando
            if not self.tocando:
                self.som.stop()

    # Pausar/retomar faixa
    def pausar(self):
        with self.lock:
            self.pausado = not self.pausado
            if self.pausado:
                self.som.stop()

    # Encerrar thread
    def parar(self):
        with self.lock:
            self.running = False
            self.som.stop()

# --- Cria os instrumentos ---
instrumentos = {
    "1": InstrumentoThread("Bumbo", 100),
    "2": InstrumentoThread("Caixa", 200),
    "3": InstrumentoThread("Chimbal", 400),
    "4": InstrumentoThread("Sintetizador", 600),
}

# Inicia todas as threads
for inst in instrumentos.values():
    inst.start()

# --- Cores do menu do Dj ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{CYAN}🎧 Mesa de DJ Interativa 🎛️{RESET}")
    print(f"{YELLOW}Escolha sua faixa e divirta-se!{RESET}\n")
    for k, inst in instrumentos.items():
        status = f"{GREEN}🎶 Tocando{RESET}" if inst.tocando else f"{RED}OFF{RESET}"
        pause_status = " (Pausado)" if inst.pausado else ""
        print(f"[{k}] {inst.nome} - {status}{pause_status}")
    print("\n[P] Parar todas as faixas")
    print("[Q] Sair da mesa\n")

# --- Loop principal ---
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
        print(f"{CYAN}👋 Saindo da Mesa de DJ. Até mais!{RESET}")
        break
    else:
        print(f"{RED}❌ Opção inválida! Tente de novo.{RESET}")
        time.sleep(0.8)
