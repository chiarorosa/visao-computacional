import cv2
import numpy as np

# Função para selecionar múltiplas regiões de interesse (ROI)
def selecionar_rois(imagem):
    rois = []
    while True:
        # Crie uma cópia da imagem para não alterar a original
        img = imagem.copy()
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
def capturar_quadro_do_video(caminho_video, numero_quadro):
    # Abra o vídeo
    cap = cv2.VideoCapture(caminho_video)
    # Defina o quadro para capturar
    cap.set(cv2.CAP_PROP_POS_FRAMES, numero_quadro)
    # Capture o quadro
    ret, quadro = cap.read()
    # Libere o vídeo
    cap.release()
    return quadro

# Caminho para o vídeo
caminho_video = 'vagas/parkinglot.mp4'

# Número do quadro a ser capturado
numero_quadro = 100  # Altere para o número do quadro que você deseja capturar

# Capturar o quadro do vídeo
quadro = capturar_quadro_do_video(caminho_video, numero_quadro)

# Selecionar múltiplas regiões de interesse
rois = selecionar_rois(quadro)

# Imprimir as regiões de interesse
for i, roi in enumerate(rois):
    x, y, largura, altura = roi
    print(f"Região de interesse {i+1}: x={x}, y={y}, largura={largura}, altura={altura}")

    # Extrair a região de interesse da imagem
    imagem_roi = quadro[y:y+altura, x:x+largura]

    # Exibir a região de interesse
    cv2.imshow(f'ROI {i+1}', imagem_roi)
    cv2.waitKey(0)
    cv2.destroyWindow(f'ROI {i+1}')
