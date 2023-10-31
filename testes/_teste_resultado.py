from src.resultado import Resultado
from assertpy import assert_that

def teste_resultado_do_jogo_possui_empate_jogador1vence_jogador2vence():
    assert_that(Resultado).contains(Resultado.Empate)
    assert_that(Resultado).contains(Resultado.Jogador1_Vence)
    assert_that(Resultado).contains(Resultado.Jogador2_Vence)
