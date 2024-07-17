import cv2

# Define o caminho para o vídeo do teclado virtual
video_path = r'visao-computacional-Teclado-Virtual\Teclado\teclado.mp4'

# Inicializa o rastreador (use o algoritmo de sua escolha, por exemplo, CSRT)
rastreador = cv2.TrackerCSRT_create()

# Abre o vídeo
video = cv2.VideoCapture(video_path)

# Verifica se o vídeo foi aberto corretamente
if not video.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Lê o primeiro frame do vídeo
ok, frame = video.read()

# Define manualmente o bounding box para o teclado virtual
bbox = (x, y, w, h)  # Defina as coordenadas do bounding box aqui

# Inicializa o rastreador com o primeiro frame e o bounding box
ok = rastreador.init(frame, bbox)

# Loop para ler e rastrear o teclado virtual no vídeo
while True:
    # Lê o próximo frame do vídeo
    ok, frame = video.read()

    # Verifica se o frame foi lido corretamente
    if not ok:
        break

    # Atualiza o rastreamento com o próximo frame
    ok, bbox = rastreador.update(frame)

    # Se o rastreamento for bem-sucedido, desenha o bounding box
    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, 'Erro no Rastreamento', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Mostra o frame com o rastreamento
    cv2.imshow('Rastreamento do Teclado Virtual', frame)

    # Verifica se a tecla 'ESC' foi pressionada para sair
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Libera os recursos
video.release()
cv2.destroyAllWindows()
