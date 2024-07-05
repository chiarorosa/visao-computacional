# Projeto de Visão Computacional

Projeto criado para disciplina Fundamentos de Inteligência Artificial (FIA) - Graduação. Prof. Pablo De Chiaro

Este projeto configura um ambiente virtual Python e instala as bibliotecas necessárias para um projeto de Visão Computacional.

## Configuração do Ambiente Virtual

### Passos para criar e ativar um ambiente virtual:

1. **Criar o ambiente virtual:**

   ```bash
   python -m venv env-visao
   ```

2. **Ativar o ambiente virtual:**

   No macOS e Linux:

   ```bash
   source ./env-visao/bin/activate
   ```

   No Windows:

   ```bash
   .\env-visao\Scripts\activate
   ```

## Instalação de Dependências

Certifique-se de que seu ambiente virtual esteja ativado. Instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Conteúdo do arquivo `requirements.txt`:

```text
numpy==2.0.0
opencv-python==4.10.0.84
```

## Verificação da Instalação

Para verificar se as bibliotecas foram instaladas corretamente, você pode executar o seguinte comando em um terminal Python:

```python
import cv2
import numpy as np

print(f"OpenCV version: {cv2.__version__}")
print(f"NumPy version: {np.__version__}")
```

## Sugestão de Estudos por Diretórios

1. vagas
2. reconhecimento-faces (use primeiro o `verifica_cameras.py`)
3. deteccao-objetos
4. rastreio-pessoas

## Desativação do Ambiente Virtual

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual com o comando:

```bash
deactivate
```

## Referências e Leitura

- (Ref) YoloV3: [yolov3](https://pjreddie.com/darknet/yolo/)
- (Leitura) SSD MobileNet: [SSD MobileNetV2](https://arxiv.org/abs/1512.02325)
- (Leitura) SSD MobileNet: [SSD MobileNetV2 Object Detection](https://medium.com/@techmayank2000/object-detection-using-ssd-mobilenetv2-using-tensorflow-api-can-detect-any-single-class-from-31a31bbd0691)
- (Ref) COCO: [Common Objects in Context](https://cocodataset.org/#overview)
