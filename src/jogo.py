from src.jogada import Jogada
from src.resultado import Resultado
import random


def checagem(jogador1_jogada: Jogada, jogador2_jogada: Jogada) -> Resultado:
    _result_map = {Jogada.Pedra: Jogada.Tesoura, Jogada.Tesoura: Jogada.Papel}

    if jogador1_jogada == jogador2_jogada:
        return Resultado.Empate

    if _result_map[jogador1_jogada] == jogador2_jogada:
        return Resultado.Jogador1_Vence

    return Resultado.Jogador2_Vence


def jogada_aleatoria() -> Jogada:
    jogada_aleatorizada = random.randint(0, 2)
    return Jogada(jogada_aleatorizada)
