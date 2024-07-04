import cv2

def initialize_face_detector():
    """
    Inicializa o detector de faces com o modelo pré-treinado do OpenCV.
    """
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    if face_cascade.empty():
        raise IOError("Não foi possível carregar o modelo de detecção de faces.")
    return face_cascade

def detect_faces(frame, face_cascade):
    """
    Detecta faces no frame utilizando o modelo carregado.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    return faces

def draw_faces(frame, faces):
    """
    Desenha um quadrado ao redor das faces detectadas.
    """
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (245, 255, 0), 2) # BGR

def main():
    """
    Função principal que realiza o reconhecimento de faces em tempo real.
    """
    face_cascade = initialize_face_detector()
    video_capture = cv2.VideoCapture(1) # 0 para webcam padrão

    if not video_capture.isOpened():
        raise Exception("Não foi possível abrir a webcam.")
    
    try:
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            faces = detect_faces(frame, face_cascade)
            draw_faces(frame, faces)

            cv2.imshow('Reconhecimento de Faces', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
