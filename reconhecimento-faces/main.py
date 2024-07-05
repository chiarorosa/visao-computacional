import cv2

def inicializar_detector_de_faces():
    """
    Inicializa o detector de faces com o modelo pré-treinado do OpenCV.
    """
    classificador_de_faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    if classificador_de_faces.empty():
        raise IOError("Não foi possível carregar o modelo de detecção de faces.")
    return classificador_de_faces

def detectar_faces(quadro, classificador_de_faces):
    """
    Detecta faces no quadro utilizando o modelo carregado.
    """
    cinza = cv2.cvtColor(quadro, cv2.COLOR_BGR2GRAY)
    faces = classificador_de_faces.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    return faces

def desenhar_faces(quadro, faces):
    """
    Desenha um quadrado ao redor das faces detectadas.
    """
    for (x, y, largura, altura) in faces:
        cv2.rectangle(quadro, (x, y), (x + largura, y + altura), (245, 255, 0), 2) # BGR

def main():
    """
    Função principal que realiza o reconhecimento de faces em tempo real.
    """
    classificador_de_faces = inicializar_detector_de_faces()
    captura_de_video = cv2.VideoCapture(1) # 0 para webcam padrão
    
    # Reduzir a resolução do vídeo capturado
    captura_de_video.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    captura_de_video.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    if not captura_de_video.isOpened():
        raise Exception("Não foi possível abrir a webcam.")
    
    print('\033[1;31;43m' + 'Buscando faces...' + '\033[0;39;49m')
    
    try:
        while True:
            ret, quadro = captura_de_video.read()
            if not ret:
                break

            faces = detectar_faces(quadro, classificador_de_faces)
            desenhar_faces(quadro, faces)

            cv2.imshow('Reconhecimento de Faces', quadro)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        captura_de_video.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
