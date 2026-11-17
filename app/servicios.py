from typing import TypedDict


class Pregunta(TypedDict):
    id: int
    texto: str
    opciones: list[str]


_PREGUNTAS: list[dict[str, object]] = [
    {
        "id": 1,
        "texto": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Marte", "Júpiter", "Saturno", "Venus"],
        "respuesta_correcta": 1,
    },
    {
        "id": 2,
        "texto": "¿Cuál es la capital de Japón?",
        "opciones": ["Kioto", "Osaka", "Tokio", "Nagoya"],
        "respuesta_correcta": 2,
    },
    {
        "id": 3,
        "texto": "¿Quién pintó la Mona Lisa?",
        "opciones": [
            "Vincent van Gogh",
            "Pablo Picasso",
            "Claude Monet",
            "Leonardo da Vinci",
        ],
        "respuesta_correcta": 3,
    },
    {
        "id": 4,
        "texto": "¿Cuál es el océano más extenso de la Tierra?",
        "opciones": [
            "Océano Atlántico",
            "Océano Índico",
            "Océano Pacífico",
            "Océano Ártico",
        ],
        "respuesta_correcta": 2,
    },
    {
        "id": 5,
        "texto": "¿Cuál es el elemento químico cuyo símbolo es Au?",
        "opciones": ["Plata", "Oro", "Cobre", "Aluminio"],
        "respuesta_correcta": 1,
    },
]


def obtener_preguntas(cantidad: int = 5) -> list[Pregunta]:
    return [
        {
            "id": pregunta["id"],
            "texto": pregunta["texto"],
            "opciones": list(pregunta["opciones"]),
        }
        for pregunta in _PREGUNTAS[:cantidad]
    ]


def evaluar_respuesta(id_pregunta: int, opcion: int) -> dict[str, bool | int] | None:
    for pregunta in _PREGUNTAS:
        if pregunta["id"] == id_pregunta:
            respuesta_correcta = pregunta["respuesta_correcta"]
            return {
                "correcta": opcion == respuesta_correcta,
                "respuesta_correcta": respuesta_correcta,
            }
    return None
