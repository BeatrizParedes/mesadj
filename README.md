
<img width="851" height="315" alt="capamesadj" src="https://github.com/user-attachments/assets/f1fa43ba-f9b6-483b-8bc2-67ae9cf21fc9" />

# ConsoleGroove

🎧 Transforme seu terminal em uma mesa de DJ! Controle instrumentos independentes que tocam simultaneamente.

## Descrição do Projeto

Este projeto cria uma mesa de DJ interativa usando **Python**, **Pygame** e **Threads**. Cada faixa musical (Bumbo, Caixa, Chimbal, Sintetizador) roda de forma independente, permitindo que o DJ controle cada instrumento individualmente. Os sons são gerados programaticamente pelo NumPy, sem necessidade de arquivos externos.

## Funcionalidades

* Cada instrumento é uma **thread independente**, tocando em loop contínuo.
* Pausar, retomar e desligar cada faixa sem afetar as outras.
* Menu interativo no console mostrando status de todas as faixas.
* Sons gerados com ondas senoidais simulando diferentes instrumentos.
* Controle seguro usando Locks para evitar conflitos entre threads.

## Tecnologias

* Python 3.x
* Pygame (para tocar sons)
* NumPy (para gerar sons programaticamente)
* Threading (para executar faixas simultaneamente)

## Como Rodar

1. Clone este repositório ou baixe os arquivos.
2. Instale as dependências:

```bash
pip install pygame numpy
```

3. Execute o programa:

```bash
python mesa_dj.py
```

4. Use o menu:

   * `[1-4]` → Liga/desliga cada faixa.
   * `P` → Para todas as faixas.
   * `Q` → Sai da mesa.

## Estrutura do Código

1. **Bibliotecas:** `threading`, `numpy`, `pygame`, `time`, `os`.
2. **Função `criar_som()`:** cria ondas sonoras programaticamente.
3. **Classe `InstrumentoThread`:** controla cada faixa com métodos para ligar, pausar e parar.
4. **Dicionário `instrumentos`:** armazena todas as threads.
5. **Menu interativo:** exibe status de cada faixa e aceita comandos do usuário.

## Conceitos Abordados

* **Threads:** cada instrumento toca de forma independente.
* **Lock/Sincronização:** evita conflitos ao alterar estado das faixas.
* **Loop principal:** controla interação do usuário em tempo real.
* **Áudio programático:** criação de sons usando NumPy.

## Resumo

Este projeto demonstra como criar um sistema interativo multithreaded, permitindo que o usuário controle diferentes instrumentos de forma simultânea em um console. É uma ótima introdução a conceitos de programação concorrente, controle de áudio e interação em tempo real.

---

📌 **Pronto para entrega e uso como desafio de Mesa de DJ interativa!**


## Equipe e Contato

| Integrante | Perfil |
|------------|--------|
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/ab3d5f4b-1a84-4660-b6ec-bae496e9dc1a" width="80" style="object-fit:cover;"> </div> | **Beatriz Paredes** <br> [LinkedIn](https://www.linkedin.com/in/beatriz-paredes-do-nascimento-91664a182/) |
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/c3b643ec-ebe1-4c73-991f-b7b60d6045bb" width="80" style="object-fit:cover;"> </div> | **Catarina Loureiro** <br> [LinkedIn](https://www.linkedin.com/in/catarina-virginia-lima-loureiro-xavier-439731338/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app) |
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/5c5ebd9a-bd8d-4600-bf45-ae54c9ccd5bc" width="80" style="object-fit:cover;"> </div> | **Cecília Medeiros** <br> [LinkedIn](https://www.linkedin.com/in/medeiroscecilia22) |
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/73402bd7-f077-4679-9cbe-57bcbb939b29" width="80" style="object-fit:cover;"> </div> | **Isabella Batista** <br> [LinkedIn](https://www.linkedin.com/in/isabella-b-a096452b2/) |
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/02960a81-8439-47f8-bf8a-8cac7e296595" width="80" style="object-fit:cover;"> </div> | **Melissa Filgueiras** <br> [LinkedIn](https://www.linkedin.com/in/melissafilgueiras/) |
