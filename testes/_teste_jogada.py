from src.jogada import Jogada
from assertpy import assert_that


def teste_jogada_tem_pedra_papel_tesoura():
    assert_that(Jogada).contains(Jogada.Pedra)
    assert_that(Jogada).contains(Jogada.Papel)
    assert_that(Jogada).contains(Jogada.Tesoura)
