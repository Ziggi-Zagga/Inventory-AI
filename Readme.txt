He instalado python desde la siguiente url:
https://www.python.org/downloads/windows/

crear main.py
crear requirements.txt

Instalar las dependencias (Desde el cmd)
pip install -r requirements.txt
python -m spacy download es_core_news_sm

Lanzar el servidor
uvicorn main:app --reload

para configurar FastAPI abrir
http://localhost:8000/docs

para entrenar el modelo
python train_intent_model.py

