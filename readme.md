Colaboradores: Lucas Gazolla 1139819, Endrewell V. Favaretto 1139685

#  Jogos Mortais Terminal (The Game)

Este é um jogo de aventura textual e lógica desenvolvido em Python, focado em desafios de tomada de decisão, matemática e memória. O jogo utiliza comandos de sistema para criar uma experiência imersiva diretamente no terminal.

## Descrição

Você assume o papel de um participante em um jogo de vida ou morte comandado por uma inteligência artificial. O objetivo é superar cinco desafios consecutivos. Um único erro encerra o programa imediatamente.

### Desafios incluídos:
1.  **Sorte Pura:** Tente adivinhar o número entre 1 e 3.
2.  **Cálculo de Potência:** Resolva uma operação exponencial gerada aleatoriamente.
3.  **Fórmula Combinatória:** Utilize resultados de fases anteriores para resolver uma equação.
4.  **Teste de Memória:** Memorize uma sequência de 5 números exibida por apenas 2 segundos.
5.  **Enigma de Arquitetura:** Converta bits para Megabytes (MB).

## Como Executar

1.  Certifique-se de ter o **Python 3** instalado.
2.  O jogo foi projetado para o terminal do **Windows** (CMD ou PowerShell), pois utiliza comandos `os.system` para cores e limpeza de tela.
3.  Abra o VS Code na pasta do projeto.
4.  No terminal, execute:
    ```bash
    python nome_do_seu_arquivo.py
    ```

##  Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Bibliotecas nativas:**
    * `os`: Controle de interface (cores e `cls`).
    * `time`: Gerenciamento de tempo e pausas dramáticas.
    * `random`: Geração de números aleatórios para os desafios.
    * `sys`: Manipulação do sistema e encerramento do processo.

##  Interface Visual

O jogo utiliza códigos de cores do Windows para indicar o estado do jogador:
*  **Verde (`0a`):** Sucesso / Sobrevivência.
*  **Vermelho (`04` / `0c`):** Perigo / Morte.
*  **Branco (`07`):** Texto padrão e perguntas.
