import random
from app.database import SessionLocal, engine, Base
from app.models.resource import Resource
from app.services.resource_service import _get_or_create_tag

Base.metadata.create_all(bind=engine)

# titulos e tags geradas por i.a

TITLES = [
    "Introdução ao Python",
    "Cálculo Diferencial e Integral",
    "História do Brasil",
    "Fundamentos de Física",
    "Álgebra Linear",
    "Programação Orientada a Objetos",
    "Estatística Básica",
    "Química Orgânica",
    "Biologia Celular",
    "Filosofia Moderna",
    "Estruturas de Dados",
    "Redes de Computadores",
    "Banco de Dados Relacional",
    "Machine Learning com Python",
    "Desenvolvimento Web com React",
    "Sistemas Operacionais",
    "Arquitetura de Computadores",
    "Cálculo Numérico",
    "Probabilidade e Estatística",
    "Inteligência Artificial",
]

TYPES = ["video", "pdf", "link"]

TAG_POOL = [
    "python",
    "matematica",
    "historia",
    "fisica",
    "algebra",
    "programacao",
    "estatistica",
    "quimica",
    "biologia",
    "filosofia",
    "estruturas-de-dados",
    "redes",
    "banco-de-dados",
    "machine-learning",
    "react",
    "sistemas-operacionais",
    "arquitetura",
    "calculo",
    "probabilidade",
    "ia",
    "educacao",
    "ensino-medio",
    "graduacao",
    "exercicios",
    "teoria",
    "pratica",
    "video-aula",
    "apostila",
]

AMOUNT = 100


def seed():
    db = SessionLocal()
    try:
        for i in range(AMOUNT):
            title = f"{random.choice(TITLES)} — {i + 1}"
            resource_type = random.choice(TYPES)
            tag_names = random.sample(TAG_POOL, k=random.randint(2, 5))
            tags = [_get_or_create_tag(db, name) for name in tag_names]
            resource = Resource(
                title=title,
                description=f"Material de estudo sobre {title.lower()}.",
                type=resource_type,
                url=f"https://exemplo.com/recurso-{i + 1}",
                tags=tags,
            )
            db.add(resource)

        db.commit()
        print(f"Seed terminado: {AMOUNT} recursos criados")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
