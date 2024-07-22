import cv2

def selecionar_roi(video_path, frame_number):
	video = cv2.VideoCapture(video_path)
	video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
	ret, frame = video.read()
	if not ret:
		print('Erro ao ler o frame do vídeo')
		return None

	roi =cv2.selectROI("Selecione a área da fila", frame, fromCenter=False, showCrosshair=True)
	cv2.destroyAllWindows()
	return roi

if _name_ == "__main__":
	video_path = 'C:\\Users\\jenni\\Desktop\\trab-projeto-IA\\visao-computacional\\contador-pessoas-fila\\fila-de-pessoas.mp4'
	frame_number = 0
	roi = selecionar_roi(video_path, frame_number)
	print(f"Região de interesse selecionada: {roi}")
