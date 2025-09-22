# ConsoleGroove - Mesa de DJ Interativa

![Capa ConsoleGroove](https://github.com/user-attachments/assets/f1fa43ba-f9b6-483b-8bc2-67ae9cf21fc9)

🎧 Transforme seu terminal em uma mesa de DJ! Controle instrumentos independentes que tocam simultaneamente.

## Descrição do Projeto

Este projeto cria uma mesa de DJ interativa usando **Python**, **Pygame** e **Threads**. Cada faixa musical (Baixo, Bateria, Guitarra, Piano, Voz) roda de forma independente, permitindo que o DJ controle cada instrumento individualmente. Você pode tocar cada faixa isoladamente ou todos os instrumentos ao mesmo tempo.

## Funcionalidades

* Cada instrumento é uma **thread independente**, tocando em loop contínuo.
* Pausar, retomar e desligar cada faixa sem afetar as outras.
* Tocar todos os instrumentos simultaneamente com o comando `all play`.
* Parar todos os instrumentos com `all stop`.
* Menu interativo no console mostrando status de todas as faixas.
* Controle seguro usando **Locks** para evitar conflitos entre threads.

## Tecnologias

* Python 3.x
* Pygame (para tocar arquivos `.wav`)
* Threading (para executar faixas simultaneamente)

## Como Rodar

1. Clone este repositório ou baixe os arquivos.
2. Instale a dependência:

```bash
pip install pygame
```

3. Execute o programa:

```bash
python mesa_dj.py
```

4. Use o menu interativo:

* `play <nome>` → Toca o instrumento selecionado.
* `pause <nome>` → Pausa ou retoma o instrumento.
* `stop <nome>` → Para o instrumento.
* `all play` → Toca todos os instrumentos simultaneamente.
* `all stop` → Para todos os instrumentos.
* `sair` → Sai do programa.

Instrumentos disponíveis: **baixo, bateria, guitarra, piano, voz**.

## Estrutura do Código

1. **Bibliotecas:** `threading`, `pygame`, `time`, `os`.
2. **Classe `InstrumentoThread`:** controla cada faixa com métodos para ligar, pausar, parar e alternar status.
3. **Dicionário `instrumentos`:** armazena todas as threads.
4. **Loop principal:** interpreta comandos do usuário e controla os instrumentos em tempo real.

## Conceitos Abordados

* **Threads:** cada instrumento toca de forma independente.
* **Lock/Sincronização:** evita conflitos ao alterar estado das faixas.
* **Loop principal:** controla a interação do usuário.
* **Áudio com Pygame:** reprodução de arquivos `.wav` com múltiplos canais.

## Resumo

Este projeto demonstra como criar um sistema interativo multithreaded, permitindo que o usuário controle diferentes instrumentos simultaneamente em um console. É uma introdução prática a conceitos de **programação concorrente**, **controle de áudio** e **interação em tempo real**.

---

## Equipe e Contato

| Integrante | Perfil |
|------------|--------|
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/ab3d5f4b-1a84-4660-b6ec-bae496e9dc1a" width="80" style="object-fit:cover;"> </div> | **Beatriz Paredes** <br> [LinkedIn](https://www.linkedin.com/in/beatriz-paredes-do-nascimento-91664a182/) |
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/c3b643ec-ebe1-4c73-991f-b7b60d6045bb" width="80" style="object-fit:cover;"> </div> | **Catarina Loureiro** <br> [LinkedIn](https://www.linkedin.com/in/catarina-virginia-lima-loureiro-xavier-439731338/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app) |
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/5c5ebd9a-bd8d-4600-bf45-ae54c9ccd5bc" width="80" style="object-fit:cover;"> </div> | **Cecília Medeiros** <br> [LinkedIn](https://www.linkedin.com/in/medeiroscecilia22) |
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/73402bd7-f077-4679-9cbe-57bcbb939b29" width="80" style="object-fit:cover;"> </div> | **Isabella Batista** <br> [LinkedIn](https://www.linkedin.com/in/isabella-b-a096452b2/) |
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/02960a81-8439-47f8-bf8a-8cac7e296595" width="80" style="object-fit:cover;"> </div> | **Melissa Filgueiras** <br> [LinkedIn](https://www.linkedin.com/in/melissafilgueiras/) |

Para ver o guia completo do código, [clique aqui](DOC_CODIGO.md)

