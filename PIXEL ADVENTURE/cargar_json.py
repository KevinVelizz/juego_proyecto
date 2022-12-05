import pygame
import json
from constantes import *


def cargar_json_data(path:str) -> list:
    '''
    La funcion importa los datos del json.
    Recibe por parametro la URL del json.
    Retorna la lista que contiene.
    '''
    with open(path, "r") as file:
        lista = json.load(file)
    return lista["levels"]

lista_info = cargar_json_data("PIXEL ADVENTURE/levels.json")[0]["level_one"]
