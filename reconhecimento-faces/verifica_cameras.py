import cv2

def verificar_cameras():
    indice = 0
    cameras_disponiveis = []
    
    while True:
        captura = cv2.VideoCapture(indice)
        if not captura.read()[0]:
            break
        else:
            cameras_disponiveis.append(indice)
        captura.release()
        indice += 1
    
    if cameras_disponiveis:
        print(f"{len(cameras_disponiveis)} câmera(s) encontrada(s): {cameras_disponiveis}")
    else:
        print("Nenhuma câmera encontrada.")

if __name__ == "__main__":
    verificar_cameras()
