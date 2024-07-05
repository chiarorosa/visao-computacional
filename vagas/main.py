import cv2
import numpy as np

# Definição das regiões de interesse (ROI)
VAGAS = [
    [1, 89, 108, 213],
    [124, 81, 123, 223],
    [282, 86, 127, 215],
    [432, 81, 135, 219],
    [583, 88, 135, 215],
    [727, 87, 141, 212],
    [880, 93, 123, 205],
    [1034, 86, 118, 212]
]

# Constantes
LIMITE_VAGA_LIVRE = 3000
LIMITE_VAGA_OCUPADA = 5000
NUM_VAGAS = len(VAGAS)
DELAY = 50

def processa_frame(img):
    """
    Processa a imagem para destacar as áreas de interesse.
    """
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_threshold = cv2.adaptiveThreshold(img_cinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    img_blur = cv2.medianBlur(img_threshold, 5)
    kernel = np.ones((3, 3), np.int8)
    img_dil = cv2.dilate(img_blur, kernel)
    return [img_dil, img_cinza]

def verifica_vagas(img, img_dil, vagas):
    """
    Verifica o status das vagas de estacionamento e desenha as regiões na imagem.
    """
    qt_vagas_abertas = 0
    for x, y, w, h in vagas:
        recorte = img_dil[y:y+h, x:x+w]
        qt_px_branco = cv2.countNonZero(recorte)

        cv2.rectangle(img, (x, y+h-22), (x+50, y+h-5), (0, 0, 0), -1)
        cv2.putText(img, str(qt_px_branco), (x, y+h-10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

        if qt_px_branco > LIMITE_VAGA_OCUPADA:
            cor = (0, 0, 255)  # Vermelho
        elif LIMITE_VAGA_LIVRE < qt_px_branco <= LIMITE_VAGA_OCUPADA:
            cor = (0, 255, 255)  # Amarelo
        else:
            cor = (0, 255, 0)  # Verde
            qt_vagas_abertas += 1

        cv2.rectangle(img, (x, y), (x + w, y + h), cor, 2)
    
    return qt_vagas_abertas

def exibe_status(img, qt_vagas_abertas, num_vagas):
    """
    Exibe o status das vagas abertas na imagem.
    """
    cv2.rectangle(img, (90, 0), (415, 60), (0, 0, 0), -1)
    cv2.putText(img, 'VAGAS: {}/{}'.format(qt_vagas_abertas, num_vagas), (100, 45), cv2.FONT_HERSHEY_DUPLEX, 1.5, (255, 255, 255), 5)

def main():
    video_path = 'vagas/parkinglot.mp4'
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print(f"Erro ao abrir o vídeo: {video_path}")
        return

    while True:
        check, img = video.read()
        if not check:
            break

        img_dil = processa_frame(img)
        qt_vagas_abertas = verifica_vagas(img, img_dil[0], VAGAS)
        exibe_status(img, qt_vagas_abertas, NUM_VAGAS)

        cv2.imshow('Video', img)
        
        cv2.namedWindow('Processamento', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Processamento', 350, 200)
        cv2.imshow('Processamento', img_dil[0])
        
        cv2.namedWindow('Passo', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Passo', 350, 200)
        cv2.imshow('Passo', img_dil[1])

        if cv2.waitKey(DELAY) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
