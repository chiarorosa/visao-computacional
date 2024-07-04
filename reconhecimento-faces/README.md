# Reconhecimento de Faces com OpenCV

Este projeto é um exemplo simples de aplicação de reconhecimento facial em tempo real usando Python e a biblioteca OpenCV. O script acessa a webcam do dispositivo, detecta faces em tempo real e desenha uma área quadrada verde ao redor de cada rosto detectado.

## Funcionalidades

- Acesso à webcam do dispositivo para captura de vídeo em tempo real.
- Detecção de faces utilizando o modelo Haar Cascade fornecido pelo OpenCV.
- Desenho de retângulos ao redor das faces detectadas.

## Estrutura do Código

O script é dividido em várias funções para modularidade e clareza:

- `initialize_face_detector()`: Carrega o modelo de detecção de faces Haar Cascade. Retorna um objeto `CascadeClassifier`.

- `detect_faces(frame, face_cascade)`: Recebe um frame e o objeto `face_cascade`, convertendo o frame para escala de cinza e aplicando a detecção de faces. Retorna as coordenadas das faces detectadas.

- `draw_faces(frame, faces)`: Recebe o frame original e as coordenadas das faces, desenhando retângulos verdes ao redor das faces.

- `main()`: Orquestra a execução do programa, gerenciando a captura de vídeo, a detecção de faces, a atualização dos gráficos na janela e o encerramento do programa.

## IMPORTANTE

- Certifique-se de que a webcam não está sendo usada por outro aplicativo.
- O índice da câmera (`video_capture = cv2.VideoCapture(1)`) pode precisar ser ajustado dependendo do dispositivo e da configuração do sistema. O índice '0' geralmente se refere à webcam integrada em laptops.

## CURIOSIDADE

O haarcascade_frontalface_default.xml é um arquivo que contém um modelo pré-treinado de classificador Haar Cascade para detectar faces frontais em imagens. Este arquivo é parte da biblioteca OpenCV e baseia-se na técnica de Haar Cascades, desenvolvida por Paul Viola e Michael Jones, que foi publicada em seu artigo pioneiro “Rapid Object Detection using a Boosted Cascade of Simple Features” em 2001.
