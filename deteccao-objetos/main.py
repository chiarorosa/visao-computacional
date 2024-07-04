import cv2
import numpy as np

# Carregar os nomes das classes
with open("deteccao-objetos/coco.names", "r") as f:
    CLASSES = [line.strip() for line in f.readlines()]

# Gera cores diferentes para cada classe
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# Configurações do modelo YOLOv3
CFG = "deteccao-objetos/yolov3.cfg"
WEIGHTS = "deteccao-objetos/yolov3.weights"

def load_pretrained_model():
    """
    Carrega o modelo YOLOv3 pré-treinado e configurações associadas axso OpenCV.
    """
    model = cv2.dnn.readNetFromDarknet(CFG, WEIGHTS)
    model.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    model.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    if model.empty():
        raise IOError("Não foi possível carregar o modelo de detecção de objetos.")
    return model

def preprocess_frame(frame):
    """
    Pré-processa o frame para detecção: redimensiona e normaliza.
    """
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1/255.0, size=(416, 416), swapRB=True, crop=False)
    return blob

def detect_objects(frame, model):
    """
    Detecta objetos no frame usando o modelo carregado.
    """
    blob = preprocess_frame(frame)
    model.setInput(blob)
    layer_names = model.getLayerNames()
    output_layers = [layer_names[i - 1] for i in model.getUnconnectedOutLayers()]
    outputs = model.forward(output_layers)
    return outputs

def draw_detections(frame, detections, threshold=0.5):
    """
    Desenha retângulos ao redor dos objetos detectados com confiança acima do limiar.
    """
    (h, w) = frame.shape[:2]
    boxes = []
    confidences = []
    class_ids = []

    for output in detections:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > threshold:
                box = detection[0:4] * np.array([w, h, w, h])
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indices = cv2.dnn.NMSBoxes(boxes, confidences, threshold, threshold - 0.1)
    if len(indices) > 0:
        for i in indices.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            color = [int(c) for c in COLORS[class_ids[i]]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            text = f"{CLASSES[class_ids[i]]}: {confidences[i]:.2f}"
            cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

def main():
    """
    Executa a detecção de objetos em tempo real usando a webcam.
    """
    print("Inicializando o detector de objetos...")
    model = load_pretrained_model()
    video_capture = cv2.VideoCapture(0) # 0 para webcam padrão

    if not video_capture.isOpened():
        raise Exception("Não foi possível abrir a webcam.")

    # Reduzir a resolução do vídeo capturado
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    try:
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break
            
            detections = detect_objects(frame, model)
            draw_detections(frame, detections)

            cv2.imshow('Detecta Objetos', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()