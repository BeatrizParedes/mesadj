import threading
import pygame
import time
import os

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

class InstrumentoThread(threading.Thread):
    channel_index = 0

    def __init__(self, nome, arquivo_mp3):
        super().__init__()
        self.nome = nome
        self.arquivo = arquivo_mp3
        self.som = pygame.mixer.Sound(arquivo_mp3)
        self.arquivo = arquivo_mp3
        self.som = pygame.mixer.Sound(arquivo_mp3)
        self.tocando = False
        self.pausado = False
        self.lock = threading.Lock()
        self.running = True

        self.channel = pygame.mixer.Channel(InstrumentoThread.channel_index)
        InstrumentoThread.channel_index += 1

    def run(self):
        while self.running:
            with self.lock:
                if self.tocando and not self.pausado:
                    if not self.channel.get_busy():
                        self.channel.play(self.som, loops=-1)
            time.sleep(0.2)

    def play(self):

        with self.lock:
            if self.pausado:
                self.channel.unpause()
                self.pausado = False
            else:
                self.channel.play(self.som, loops=-1)
            self.tocando = True

    def pausar(self):
        """Pausa se tocando, despausa se já estava pausado."""
        with self.lock:
            if self.tocando:
                if not self.pausado:
                    self.channel.pause()
                    self.pausado = True
                else:
                    self.channel.unpause()
                    self.pausado = False
    def parar(self):
        """Para completamente e reinicia o áudio do zero."""
        with self.lock:
            self.channel.stop()
            self.tocando = False
            self.pausado = False
            self.running = False  

if __name__ == "__main__":
   
    pasta_stems = os.path.join(os.path.dirname(__file__), "stems")

   
    instrumentos = [
        InstrumentoThread("Baixo", os.path.join(pasta_stems, "Clocks_coldplay_bass.wav")),
        InstrumentoThread("Bateria", os.path.join(pasta_stems, "Clocks_coldplay_drums.wav")),
        InstrumentoThread("Guitarra", os.path.join(pasta_stems, "Clocks_coldplay_guitar.wav")),
        InstrumentoThread("Piano", os.path.join(pasta_stems, "Clocks_coldplay_piano.wav")),
        InstrumentoThread("Voz", os.path.join(pasta_stems, "Clocks_coldplay_vocals.wav"))
    ]

   
    for i in instrumentos:
        i.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for i in instrumentos:
            i.parar()
        pygame.mixer.quit()
