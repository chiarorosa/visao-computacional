# Bot Piano Game

## Objetivo
Este projeto implementa um sistema que joga um jogo de piano automaticamente utilizando OpenCV e um modelo de deep learning. O código utiliza a API DNN do OpenCV para processar as imagens capturadas do jogo, detectando as teclas do piano e simulando os toques.

## Funcionalidades
- Detecção de teclas do piano em tempo real a partir de um vídeo.
- Simulação automática dos toques no piano conforme as teclas são detectadas.
- Contagem e exibição do número de acertos no jogo.

## Modelo Pré-Treinado
O modelo de deep learning utilizado para a detecção das teclas do piano pode ser baixado através do seguinte link:

[Download frozen_inference_graph.pb](URL_DO_MODELO)

Extraia o arquivo `frozen_inference_graph.pb` do arquivo tar.gz baixado e coloque-o no diretório `bot-piano-game` do projeto.

## Executando o Projeto
Para executar o bot de piano, simplesmente execute o script `main.py` com Python. Certifique-se de que todos os arquivos necessários estão na mesma pasta que o script.

```bash
python main.py
