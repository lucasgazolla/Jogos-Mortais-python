import os

Colaboradores: Lucas Gazolla 1139819, Endrewell Favaretto 1139685


# Conteúdo do README
readme_content = Projeto Jogos Motais

Um jogo de mistério e lógica desenvolvido em Python. O desafio combina cálculos matemáticos, testes de memória e charadas de conversão de dados, tudo narrado por uma voz imersiva via **Edge TTS**.

##  Sobre o Projeto

O projeto utiliza a interface do terminal para criar uma atmosfera de tensão. Através de comandos de cor de sistema e efeitos sonoros, o jogador é guiado por fases onde o erro significa o fim da execução (a "morte" no jogo).

###  Sistema de Voz
O jogo utiliza a biblioteca `edge-tts` com a voz `pt-BR-AntonioNeural` para narrar as perguntas e provocar o jogador, garantindo uma experiência mais profunda do que apenas ler o texto na tela.

---

##  Tecnologias Utilizadas

* **Python 3.x**: Linguagem base.
* **Edge-TTS**: Geração de voz neural da Microsoft (requer conexão com internet).
* **Playsound**: Execução dos arquivos de áudio `.mp3`.
* **Asyncio**: Para gerenciar a criação assíncrona dos áudios.
* **Random/Time/OS**: Para lógica de jogo, temporização e manipulação do terminal.

---

## Instalação e Configuração

Para rodar este projeto, você precisará instalar as dependências de áudio. Siga os passos abaixo:

1. **Clone o repositório ou baixe o arquivo `.py`.**

2. **Instale as bibliotecas necessárias:**
   Abra o seu terminal e execute:
   ```bash
   pip install edge-tts playsound==1.2.2
