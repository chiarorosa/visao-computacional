# Rastreio de Pessoas

Este projeto implementa um sistema de rastreio de pessoas em vídeos utilizando o OpenCV e um modelo pré-treinado de deep learning, SSD MobileNet V2. O código utiliza a API DNN do OpenCV para processar as imagens capturadas de um vídeo, detectando pessoas e desenhando caixas delimitadoras ao redor de cada uma delas.

## Funcionalidades

- Detecção de pessoas em tempo real a partir de um vídeo.
- Aplicação de Supressão Não Máxima para evitar caixas delimitadoras redundantes.
- Contagem e exibição do número de pessoas detectadas no vídeo.

## Modelo Pré-Treinado

O modelo SSD MobileNet V2 usado para a detecção de pessoas pode ser baixado através do seguinte link:

- [Download frozen_inference_graph.pb](https://storage.googleapis.com/download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz)

Extraia o arquivo `frozen_inference_graph.pb` do arquivo tar.gz baixado e coloque-o no diretório `rastreio-pessoas` do projeto.

## Executando o Projeto

Para executar o rastreio de pessoas, simplesmente execute o script `main.py` com Python. Certifique-se de que todos os arquivos necessários estão na mesma pasta que o script.

```bash
python main.py
```

## Controles

Durante a execução do projeto, você pode:

- Pressionar 'p' para pausar/continuar o vídeo.
- Pressionar 'q' para sair do aplicativo.
