import cv2
import numpy as np

# Caminhos dos arquivos
ARQUIVO_VIDEO = 'rastreio-pessoas/walking.mp4'
ARQUIVO_MODELO = 'rastreio-pessoas/frozen_inference_graph.pb'
ARQUIVO_CFG = 'rastreio-pessoas/ssd_mobilenet_v2_coco.pbtxt'

def carregar_modelo(ARQUIVO_MODELO, ARQUIVO_CFG):
    try:
        modelo = cv2.dnn.readNetFromTensorflow(ARQUIVO_MODELO, ARQUIVO_CFG)
    except cv2.error as erro:
        print(f"Erro ao carregar o modelo: {erro}")
        exit()
    return modelo

def aplicar_supressao_nao_maxima(caixas, confiancas, limiar_conf, limiar_supr):
    indices = cv2.dnn.NMSBoxes(caixas, confiancas, limiar_conf, limiar_supr)
    return [caixas[i] for i in indices.flatten()] if len(indices) > 0 else []

def main():
    captura = cv2.VideoCapture(ARQUIVO_VIDEO)
    detector_pessoas = carregar_modelo(ARQUIVO_MODELO, ARQUIVO_CFG)
    pausado = False

    while True:
        if not pausado:
            ret, frame = captura.read()
            if not ret:
                break

            blob = cv2.dnn.blobFromImage(frame, size=(300, 300), swapRB=True, crop=False)
            detector_pessoas.setInput(blob)
            deteccoes = detector_pessoas.forward()

            caixas = []
            confiancas = []

            for i in range(deteccoes.shape[2]):
                confianca = deteccoes[0, 0, i, 2]
                if confianca > 0.5:
                    (altura, largura) = frame.shape[:2]
                    caixa = deteccoes[0, 0, i, 3:7] * np.array([largura, altura, largura, altura])
                    (inicioX, inicioY, fimX, fimY) = caixa.astype("int")
                    caixas.append([inicioX, inicioY, fimX - inicioX, fimY - inicioY])
                    confiancas.append(float(confianca))

            caixas_finais = aplicar_supressao_nao_maxima(caixas, confiancas, limiar_conf=0.5, limiar_supr=0.4)
            numero_pessoas = len(caixas_finais)

            for (inicioX, inicioY, largura, altura) in caixas_finais:
                cv2.rectangle(frame, (inicioX, inicioY), (inicioX + largura, inicioY + altura), (0, 255, 0), 2)

            cv2.putText(frame, f"Pessoas: {numero_pessoas}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Rastreio de Pessoas", frame)
        
        tecla = cv2.waitKey(30) & 0xFF
        if tecla == ord('q'):
            break
        elif tecla == ord('p'):
            pausado = not pausado

    captura.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()