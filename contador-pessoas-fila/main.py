import cv2
import numpy as np

#carrega o detector de pessoas HOG
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#define a regiao da fila
AREA_FILA = [100, 100, 500, 300]

def processa_frame(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def verifica_pessoas(img, area_fila):
	x, y, w, h = area_fila
	roi = img[y:y+h, x:x+w]
	pessoas, _= hog.detectMultiScale(roi)
	return len(pessoas)

def exibe_status(img, num_pessoas):
	cv2.putText(img, f'Pessoas na fila: {num_pessoas}',(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0),2)

def main():
	video = cv2.VideoCapture('C:\Users\jenni\Desktop\trab-projeto-IA\visao-computacional\contador-pessoas-fila\fila-de-pessoas.mp4')

	while True:
		ret, frame = video.read()
		if not ret:
			break

		img_processada = processa_frame(frame)
		num_pessoas = verifica_pessoas(img_processada, AREA_FILA)
		exibe_status(frame, num_pessoas)

		cv2.rectangle(frame, (AREA_FILA[0], AREA_FILA[1]), (AREA_FILA[0]+AREA_FILA[2], AREA_FILA[1]+AREA_FILA[3]), (0, 255, 0), 2)
		cv2.imshow('Contador de Pessoas', frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	video.release()
	cv2.destroyAllwindows()

if __name__ == '__main__':
	main()