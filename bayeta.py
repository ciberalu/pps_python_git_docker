import random

def frotar(n_frases: int = 1) -> list:
    try:
        with open("frases.txt", "r") as file:
            frases_disponibles = [line.strip() for line in file if line.strip() != ""]

        # Si n_frases es mayor que la cantidad de frases disponibles, se devuelve toda la lista.
        # Esto evita repetir frases si se solicitan más de las disponibles.
        if n_frases > len(frases_disponibles):
            return frases_disponibles

        frases_elegidas = random.sample(frases_disponibles, k=n_frases)
        return frases_elegidas
    except FileNotFoundError:
        return ["Error: El archivo de frases no fue encontrado."]
