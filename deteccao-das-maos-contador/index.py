import mediapipe as mp
import cv2
import os

# Inicializações do MediaPipe e OpenCV
drawing_hand = mp.solutions.drawing_utils
hand_node = mp.solutions.hands

# Cria o diretório para salvar as imagens, se não existir
output_dir = 'Output_Images'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Inicia a captura de vídeo
cap = cv2.VideoCapture(0)

with hand_node.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Converte a imagem de BGR para RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Inverte horizontalmente a imagem
        image = cv2.flip(image, 1)
        
        # Define a imagem como não gravável para otimizar o desempenho
        image.flags.writeable = False
        
        # Processa a imagem para detectar as mãos
        results = hands.process(image)
        
        # Define a imagem como gravável
        image.flags.writeable = True
        
        # Converte a imagem de volta de RGB para BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Desenha as detecções na imagem
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                drawing_hand.draw_landmarks(
                    image, hand_landmarks, hand_node.HAND_CONNECTIONS,
                    drawing_hand.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                    drawing_hand.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2)
                )
        

        
        # Exibe a imagem com o rastreamento das mãos
        cv2.imshow('Hand Tracking', image)
        
        # Sai do loop se a tecla 'q' for pressionada
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Libera o objeto de captura de vídeo e fecha todas as janelas
cap.release()
cv2.destroyAllWindows()
