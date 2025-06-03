# train_inventory_model.py

import spacy
from spacy.training.example import Example
from training_data_inventory import TRAINING_DATA

nlp = spacy.blank("en")

# Añadir clasificadores
textcat = nlp.add_pipe("textcat", last=True)
textcat.add_label("move_product")
textcat.add_label("check_product")
textcat.add_label("add_product")
textcat.add_label("delete_product")
textcat.add_label("update_stock")

ner = nlp.add_pipe("ner", last=True)

# Registrar entidades
for _, annotations in TRAINING_DATA:
    for start, end, label in annotations["entities"]:
        ner.add_label(label)

# Preparar ejemplos
examples = []
for text, ann in TRAINING_DATA:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, ann)
    examples.append(example)

# Entrenar
nlp.initialize()

for i in range(30):
    losses = {}
    nlp.update(examples, losses=losses)
    print(f"Iteration {i + 1}, Losses: {losses}")

# Guardar
nlp.to_disk("inventory_model")
print("✅ Modelo guardado en inventory_model/")
