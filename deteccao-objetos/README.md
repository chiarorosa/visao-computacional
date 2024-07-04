### YOLOv3 com OpenCV em Python

Este repositório contém um exemplo de uso do modelo YOLOv3 para detecção de objetos em tempo real utilizando OpenCV e Python. O código inclui o carregamento do modelo pré-treinado YOLOv3, a configuração do OpenCV DNN, e a realização da detecção de objetos em tempo real a partir de uma captura de vídeo (por exemplo, webcam).

### Links para Download de Modelos YOLO

#### YOLOv3:

- Arquivo de configuração: [yolov3.cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
- Arquivo de pesos: [yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)
- Arquivo de nomes das classes: [coco.names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

#### YOLOv3-tiny:

- Arquivo de configuração: [yolov3-tiny.cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3-tiny.cfg)
- Arquivo de pesos: [yolov3-tiny.weights](https://pjreddie.com/media/files/yolov3-tiny.weights)
- Arquivo de nomes das classes: [coco.names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

### Descrição do Código

Este código faz o seguinte:

1. **Carrega o modelo YOLOv3 pré-treinado**:
   Utiliza a função `cv2.dnn.readNetFromDarknet` para carregar a configuração (`.cfg`) e os pesos (`.weights`) do modelo YOLOv3.

2. **Pré-processa os frames de vídeo**:
   Redimensiona e normaliza os frames capturados para que possam ser usados como entrada para o modelo YOLOv3.

3. **Detecta objetos nos frames**:
   Utiliza o modelo carregado para detectar objetos nos frames pré-processados.

4. **Desenha as detecções nos frames**:
   Desenha caixas delimitadoras ao redor dos objetos detectados, juntamente com a classe e a confiança da detecção.

### COCO

Common Objects in Context: https://cocodataset.org/#overview

### DNN (Deep Neural Network) no OpenCV

A DNN (Deep Neural Network) é uma biblioteca no OpenCV que permite o uso de redes neurais profundas para diversas tarefas de visão computacional, como classificação de imagens, detecção de objetos, e segmentação semântica. A API DNN do OpenCV oferece uma interface para carregar e executar modelos treinados em diferentes frameworks de deep learning, como Caffe, TensorFlow, PyTorch e Darknet. Ela suporta tanto a CPU quanto a GPU, tornando-a flexível e eficiente para aplicações em tempo real.

### Darknet

Darknet é uma estrutura de rede neural de código aberto escrita em C e CUDA. Ela é utilizada principalmente para a detecção de objetos em tempo real. YOLO (You Only Look Once) é uma das implementações mais conhecidas que utilizam Darknet. YOLO é altamente eficiente e capaz de detectar objetos em uma única passagem pela rede neural, ao contrário de métodos tradicionais que requerem múltiplas passagens. Darknet é conhecido por seu desempenho rápido e capacidade de ser executado em tempo real em GPUs.
