from src.jogo import checagem, jogada_aleatoria
from src.jogada import Jogada
from assertpy import assert_that
from src.resultado import Resultado
from unittest.mock import patch


def teste_empate_pedra():
    jogador1_jogada = Jogada.Pedra
    jogador2_jogada = Jogada.Pedra

    resultado = checagem(jogador1_jogada, jogador2_jogada)
    assert_that(resultado).is_equal_to(Resultado.Empate)


def teste_pedra_x_tesoura():
    jogador1_jogada = Jogada.Pedra
    jogador2_jogada = Jogada.Tesoura

    resultado = checagem(jogador1_jogada, jogador2_jogada)

    assert_that(resultado).is_equal_to(Resultado.Jogador1_Vence)


def teste_pedra_x_papel():
    jogador1_jogada = Jogada.Pedra
    jogador2_jogada = Jogada.Papel

    resultado = checagem(jogador1_jogada, jogador2_jogada)

    assert_that(resultado).is_equal_to(Resultado.Jogador2_Vence)


def teste_tesoura_x_papel():
    jogador1_jogada = Jogada.Tesoura
    jogador2_jogada = Jogada.Papel

    resultado = checagem(jogador1_jogada, jogador2_jogada)

    assert_that(resultado).is_equal_to(Resultado.Jogador1_Vence)


def teste_tesoura_x_pedra():
    jogador1_jogada = Jogada.Tesoura
    jogador2_jogada = Jogada.Pedra

    resultado = checagem(jogador1_jogada, jogador2_jogada)

    assert_that(resultado).is_equal_to(Resultado.Jogador2_Vence)


def teste_empate_tesoura():
    jogador1_jogada = Jogada.Tesoura
    jogador2_jogada = Jogada.Tesoura

    resultado = checagem(jogador1_jogada, jogador2_jogada)

    assert_that(resultado).is_equal_to(Resultado.Empate)


@patch("random.randint")
def teste_jogada_aleatoria_pedra_no_0(random_mock):
    random_mock.return_value = 0

    resultado = jogada_aleatoria()

    assert_that(resultado).is_equal_to(Jogada.Pedra)


@patch("random.randint")
def teste_jogada_aleatoria_papel_no_1(random_mock):
    random_mock.return_value = 1

    resultado = jogada_aleatoria()

    assert_that(resultado).is_equal_to(Jogada.Papel)


@patch("random.randint")
def teste_jogada_aleatoria_tesoura_no_2(random_mock):
    random_mock.return_value = 2

    resultado = jogada_aleatoria()

    assert_that(resultado).is_equal_to(Jogada.Tesoura)
