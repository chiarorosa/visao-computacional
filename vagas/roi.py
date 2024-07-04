import cv2
import numpy as np

# Função para selecionar múltiplas regiões de interesse (ROI)
def select_rois(image):
    rois = []
    while True:
        # Crie uma cópia da imagem para não alterar a original
        img = image.copy()
        # Crie uma janela para exibir a imagem
        cv2.namedWindow('ROI', cv2.WINDOW_NORMAL)
        # Exiba a imagem na janela
        cv2.imshow('ROI', img)
        # Selecione a região de interesse
        roi = cv2.selectROI('ROI', img, fromCenter=False, showCrosshair=True)
        # Verifique se a seleção é válida (não nula)
        if roi == (0, 0, 0, 0):
            break
        rois.append(roi)
        # Feche a janela
        cv2.destroyWindow('ROI')
        # Pergunte ao usuário se deseja selecionar mais ROIs
        print("Pressione 'q' para sair ou qualquer outra tecla para selecionar outra região.")
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    return rois

# Função para capturar um quadro do vídeo
def capture_frame_from_video(video_path, frame_number):
    # Abra o vídeo
    cap = cv2.VideoCapture(video_path)
    # Defina o quadro para capturar
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    # Capture o quadro
    ret, frame = cap.read()
    # Libere o vídeo
    cap.release()
    return frame

# Caminho para o vídeo
video_path = 'vagas/parkinglot.mp4'

# Número do quadro a ser capturado
frame_number = 100  # Altere para o número do quadro que você deseja capturar

# Capturar o quadro do vídeo
frame = capture_frame_from_video(video_path, frame_number)

# Selecionar múltiplas regiões de interesse
rois = select_rois(frame)

# Imprimir as regiões de interesse
for i, roi in enumerate(rois):
    x, y, w, h = roi
    print(f"Região de interesse {i+1}: x={x}, y={y}, w={w}, h={h}")

    # Extrair a região de interesse da imagem
    roi_image = frame[y:y+h, x:x+w]

    # Exibir a região de interesse
    cv2.imshow(f'ROI {i+1}', roi_image)
    cv2.waitKey(0)
    cv2.destroyWindow(f'ROI {i+1}')
