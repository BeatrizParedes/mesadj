import time
import sys
from mesa_dj import InstrumentoThread
import pygame
import os

# Inicializa mixer caso ainda não esteja ativo
if not pygame.mixer.get_init():
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

pygame.mixer.set_num_channels(8)

# Caminho da pasta de stems
pasta_stems = os.path.join(os.path.dirname(__file__), "stems")

# Cria os instrumentos (stems)
instrumentos = {
    "baixo": InstrumentoThread("Baixo", os.path.join(pasta_stems, "Clocks_coldplay_bass.wav")),
    "bateria": InstrumentoThread("Bateria", os.path.join(pasta_stems, "Clocks_coldplay_drums.wav")),
    "guitarra": InstrumentoThread("Guitarra", os.path.join(pasta_stems, "Clocks_coldplay_guitar.wav")),
    "piano": InstrumentoThread("Piano", os.path.join(pasta_stems, "Clocks_coldplay_piano.wav")),
    "voz": InstrumentoThread("Voz", os.path.join(pasta_stems, "Clocks_coldplay_vocals.wav"))
}

# Inicia as threads
for i in instrumentos.values():
    i.start()
print("\n🎛️ Console do DJ")
print("Comandos: play <nome>, pause <nome>, stop <nome>, sair")
print("Instrumentos disponíveis:", ", ".join(instrumentos.keys()))
print()

try:
    while True:
        comando = input("> ").strip().lower().split()

        if not comando:
            continue

        acao = comando[0]

        if acao == "sair":
            break

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
    print("Threads encerradas.")
    pygame.mixer.quit()
    print("Saindo...")
