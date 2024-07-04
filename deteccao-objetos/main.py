import cv2
import numpy as np

# Carregar os nomes das classes
with open("deteccao-objetos/coco.names", "r") as arquivo:
    CLASSES = [linha.strip() for linha in arquivo.readlines()]

# Gerar cores diferentes para cada classe
CORES = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# Configurações do modelo YOLOv3
ARQUIVO_CFG = "deteccao-objetos/yolov3.cfg"
ARQUIVO_PESOS = "deteccao-objetos/yolov3.weights"

def carregar_modelo_pretreinado():
    """
    Carrega o modelo YOLOv3 pré-treinado e configurações associadas ao OpenCV.
    """
    modelo = cv2.dnn.readNetFromDarknet(ARQUIVO_CFG, ARQUIVO_PESOS)
    modelo.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    modelo.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    if modelo.empty():
        raise IOError("Não foi possível carregar o modelo de detecção de objetos.")
    return modelo

def preprocessar_frame(frame):
    """
    Pré-processa o frame para detecção: redimensiona e normaliza.
    """
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1/255.0, size=(416, 416), swapRB=True, crop=False)
    return blob

def detectar_objetos(frame, modelo):
    """
    Detecta objetos no frame usando o modelo carregado.
    """
    blob = preprocessar_frame(frame)
    modelo.setInput(blob)
    nomes_camadas = modelo.getLayerNames()
    camadas_saida = [nomes_camadas[i - 1] for i in modelo.getUnconnectedOutLayers()]
    saidas = modelo.forward(camadas_saida)
    return saidas

def desenhar_deteccoes(frame, deteccoes, limiar=0.5):
    """
    Desenha retângulos ao redor dos objetos detectados com confiança acima do limiar.
    """
    (altura, largura) = frame.shape[:2]
    caixas = []
    confiancas = []
    ids_classes = []

    for saida in deteccoes:
        for deteccao in saida:
            pontuacoes = deteccao[5:]
            id_classe = np.argmax(pontuacoes)
            confianca = pontuacoes[id_classe]
            if confianca > limiar:
                caixa = deteccao[0:4] * np.array([largura, altura, largura, altura])
                (centroX, centroY, largura_caixa, altura_caixa) = caixa.astype("int")
                x = int(centroX - (largura_caixa / 2))
                y = int(centroY - (altura_caixa / 2))

                caixas.append([x, y, int(largura_caixa), int(altura_caixa)])
                confiancas.append(float(confianca))
                ids_classes.append(id_classe)

    indices = cv2.dnn.NMSBoxes(caixas, confiancas, limiar, limiar - 0.1)
    if len(indices) > 0:
        for i in indices.flatten():
            (x, y) = (caixas[i][0], caixas[i][1])
            (largura_caixa, altura_caixa) = (caixas[i][2], caixas[i][3])
            cor = [int(c) for c in CORES[ids_classes[i]]]
            cv2.rectangle(frame, (x, y), (x + largura_caixa, y + altura_caixa), cor, 2)
            texto = f"{CLASSES[ids_classes[i]]}: {confiancas[i]:.2f}"
            cv2.putText(frame, texto, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, cor, 2)

def main():
    """
    Executa a detecção de objetos em tempo real usando a webcam.
    """
    print("Inicializando o detector de objetos...")
    modelo = carregar_modelo_pretreinado()
    captura_video = cv2.VideoCapture(1) # 0 para webcam padrão

    if not captura_video.isOpened():
        raise Exception("Não foi possível abrir a webcam.")

    # Reduzir a resolução do vídeo capturado
    captura_video.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    captura_video.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    try:
        while True:
            ret, frame = captura_video.read()
            if not ret:
                break
            
            deteccoes = detectar_objetos(frame, modelo)
            desenhar_deteccoes(frame, deteccoes)

            cv2.imshow('Detecta Objetos', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        captura_video.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()