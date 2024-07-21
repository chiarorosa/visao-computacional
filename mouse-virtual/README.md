```markdown
# Projeto de Detecção de Gesto para Controle do Mouse

Este projeto utiliza a biblioteca OpenCV para capturar vídeo da webcam em tempo real e exibir em uma janela. O objetivo é desenvolver um sistema de detecção de gestos que permita controlar o mouse ou executar outras ações no computador.

## Pré-requisitos

Para executar este projeto, você precisará ter o Python instalado em seu sistema, além da biblioteca OpenCV. Este projeto foi testado com Python 3.8.

## Configuração do Ambiente

Recomenda-se criar um ambiente virtual para instalar as dependências e executar o projeto. Siga os passos abaixo para configurar seu ambiente:

1. **Criar o ambiente virtual:**

   ```bash
   python -m venv env
   ```

2. **Ativar o ambiente virtual:**

   - No Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - No macOS e Linux:

     ```bash
     source env/bin/activate
     ```

3. **Instalar as dependências:**

   Após ativar o ambiente virtual, instale a biblioteca OpenCV utilizando o pip:

   ```bash
   pip install opencv-python
   ```

## Execução

Para executar o projeto, navegue até o diretório do projeto no terminal e execute o script Python:

```bash
python main.py
```

Uma janela se abrirá mostrando o vídeo capturado pela webcam. Atualmente, o projeto apenas exibe o vídeo capturado, mas pode ser expandido para incluir detecção de gestos e controle do mouse.

## Contribuições

Contribuições para o projeto são bem-vindas. Sinta-se à vontade para clonar o repositório, fazer suas alterações e abrir um pull request.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
```