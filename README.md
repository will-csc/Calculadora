# Calculadora Tkinter com Histórico

Este é um projeto de calculadora desenvolvido em Python utilizando a biblioteca Tkinter para criação da interface gráfica. O programa permite realizar operações matemáticas básicas e exibe um histórico dos últimos cinco cálculos realizados.

![image](https://github.com/user-attachments/assets/4f43f327-a6ca-487b-8af7-e24a3680ef0e)

<hr>

## Funcionalidades
- Interface gráfica intuitiva.
- Operações matemáticas básicas (+, -, *, /).
- Exibição do resultado na tela.
- Botão "Limpar" para resetar a equação.
- Botão "Histórico" que exibe os últimos cinco cálculos realizados.

<hr>

## Requisitos
- Python 3.x
- Biblioteca Tkinter (já incluída na maioria das instalações do Python)

<hr>

## Como executar
1. Certifique-se de que o Python esteja instalado na sua máquina.
2. Baixe ou clone este repositório.
3. Execute o seguinte comando no terminal:
   ```sh
   python calculadora.py
   ```
   
<hr>

## Estrutura do Código
- `button_press(num)`: Adiciona um número ou operador à expressão.
- `equals()`: Calcula o resultado da expressão e salva no histórico.
- `clear()`: Limpa a expressão atual.
- `show_history()`: Exibe os últimos cinco cálculos realizados.
- Configuração da interface com botões para operações matemáticas e controle do histórico.
