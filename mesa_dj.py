import threading
import pygame
import time
import os

# Inicializa o mixer do Pygame
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

# --- Classe Thread para cada instrumento ---
class InstrumentoThread(threading.Thread):
    def __init__(self, nome, arquivo_mp3):
        super().__init__()
        self.nome = nome
        self.arquivo = arquivo_mp3
        self.som = pygame.mixer.Sound(arquivo_mp3)
        self.tocando = False
        self.pausado = False
        self.lock = threading.Lock()
        self.running = True

    def run(self):
        while self.running:
            with self.lock:
                if self.tocando and not self.pausado:
                    # Se não estiver tocando, começa em loop
                    if not pygame.mixer.Channel(self._ident % 8).get_busy():
                        pygame.mixer.Channel(self._ident % 8).play(self.som, loops=-1)
            time.sleep(0.5)  # Intervalo para evitar loop apertado demais

    def toggle(self):
        with self.lock:
            self.tocando = not self.tocando
            if not self.tocando:
                pygame.mixer.Channel(self._ident % 8).stop()

    def pausar(self):
        with self.lock:
            self.pausado = not self.pausado
            if self.pausado:
                pygame.mixer.Channel(self._ident % 8).pause()
            else:
                pygame.mixer.Channel(self._ident % 8).unpause()

    def parar(self):
        with self.lock:
            self.running = False
            pygame.mixer.Channel(self._ident % 8).stop()

# -----------------------------
# Exemplo de uso
# -----------------------------
if __name__ == "__main__":
    # Caminho da pasta de stems
    pasta_stems = os.path.join(os.path.dirname(__file__), "stems")

    # Cria threads para cada stem
    instrumentos = [
        InstrumentoThread("Baixo", os.path.join(pasta_stems, "TwisTandShout_bass.mp3")),
        InstrumentoThread("Bateria", os.path.join(pasta_stems, "TwisTandShout_drums.mp3")),
        InstrumentoThread("Guitarra", os.path.join(pasta_stems, "TwisTandShout_guitar.mp3")),
        InstrumentoThread("Piano", os.path.join(pasta_stems, "TwisTandShout_piano.mp3")),
        InstrumentoThread("Voz", os.path.join(pasta_stems, "TwisTandShout_vocals.mp3"))
    ]

    # Inicia as threads
    for i in instrumentos:
        i.start()
        i.toggle()  # começa tocando

    print("Stems tocando... pressione Ctrl+C para parar.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for i in instrumentos:
            i.parar()
        pygame.mixer.quit()
