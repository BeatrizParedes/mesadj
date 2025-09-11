
<img width="851" height="315" alt="capamesadj" src="https://github.com/user-attachments/assets/f1fa43ba-f9b6-483b-8bc2-67ae9cf21fc9" />

# ConsoleGroove

Bem-vindo ao **DJ Console Simulator**, um projeto que transforma o seu console em uma verdadeira mesa de DJ! Aqui, diferentes faixas musicais (representadas por instrumentos) tocam simultaneamente, e você é o DJ no controle de cada uma delas.  

---

## 📝 Descrição do Projeto

O desafio é criar uma aplicação de console que simule uma **mesa de DJ**, onde cada instrumento toca de forma independente.  

- Cada faixa (Bateria, Baixo, Synth, etc.) é executada em sua própria **thread**, garantindo que todas funcionem simultaneamente.  
- Você pode **pausar, retomar ou encerrar** qualquer instrumento sem interferir nas demais faixas.  
- O projeto explora conceitos de **concorrência e sincronização**, permitindo controlar o estado de cada thread de forma segura.  

---

## 🎯 Conceitos Chave

- **Threads Independentes**: Cada instrumento é um thread rodando em loop contínuo.  
- **Controle de Estado**: Os estados possíveis de cada instrumento incluem:
  - `Tocando`  
  - `Pausado`  
  - `Parado`  
- **Sincronização**: Garantir que apenas um thread altere o estado de um instrumento por vez. Dependendo da linguagem, usamos mecanismos como:
  - `lock` (C#)  
  - `synchronized` (Java)  
  - `Mutex` (Python, C++)  

- **Interação com o Usuário**: Comandos de texto permitem ao DJ:
  - Pausar/retomar faixas  
  - Adicionar novos instrumentos  
  - Visualizar status ao vivo  

---

## 🚀 Funcionalidades Extras

Para quem quiser ir além:

1. **Volume e BPM**: Alterar o `Thread.Sleep()` no loop do instrumento para simular batidas mais rápidas ou lentas.  
2. **Painel ao Vivo**: Mostrar o status de todas as faixas a cada 2 segundos, com o console sendo atualizado dinamicamente.  
3. **Adicionar Instrumentos em Tempo Real**: O usuário pode adicionar uma nova faixa enquanto a música toca, mantendo a experiência interativa.  

---

## 🛠 Tecnologias

- Linguagens suportadas: C#, Java, Python, C++  
- Conceitos aplicados:
  - Threads  
  - Locks / Mutex  
  - Controle de estado de objetos  
  - Interação via console  

## Equipe e Contato

| Integrante | Perfil |
|------------|--------|
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/ab3d5f4b-1a84-4660-b6ec-bae496e9dc1a" width="80" style="object-fit:cover;"> </div> | **Beatriz Paredes** <br> [LinkedIn](https://www.linkedin.com/in/beatriz-paredes-do-nascimento-91664a182/) |
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/c3b643ec-ebe1-4c73-991f-b7b60d6045bb" width="80" style="object-fit:cover;"> </div> | **Catarina Loureiro** <br> [LinkedIn](https://www.linkedin.com/in/catarina-virginia-lima-loureiro-xavier-439731338/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app) |
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/5c5ebd9a-bd8d-4600-bf45-ae54c9ccd5bc" width="80" style="object-fit:cover;"> </div> | **Cecília Medeiros** <br> [LinkedIn](https://www.linkedin.com/in/medeiroscecilia22) |
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/73402bd7-f077-4679-9cbe-57bcbb939b29" width="80" style="object-fit:cover;"> </div> | **Isabella Batista** <br> [LinkedIn](https://www.linkedin.com/in/isabella-b-a096452b2/) |
| <div style="width:80px; height:80px; overflow:hidden; border-radius:8px;"> <img src="https://github.com/user-attachments/assets/02960a81-8439-47f8-bf8a-8cac7e296595" width="80" style="object-fit:cover;"> </div> | **Melissa Filgueiras** <br> [LinkedIn](https://www.linkedin.com/in/melissafilgueiras/) |



---

## 💡 Como Jogar com o DJ

1. Execute a aplicação no console.  
2. Use comandos para controlar cada instrumento, como:
