#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""utils.py: funções e constantes usadas para auxiliar o funcionamento do bot.

As constantes e função aqui definidas são utilizadas exibir mensagens padrões
e se comunicar com a API de economia do Awesome API para obter as informações
atuais sobre cotações.

"""
__author__ = "João Lucas Correia Barbosa de Farias"
__license__ = "GNU GENERAL PUBLIC LICENSE 3"
__version__ = "1.0.0"
__maintainer__ = "João Lucas Correia Barbosa de Farias"
__email__ = "fariasjota09@gmail.com"
__status__ = "Production"


import datetime

import requests

mensagem_padrao = """
    Escolha uma opção de cotação (clique no item):
     /USD_BRLT: Dólar - Real Turismo
     /USD_BRL: Dolár - Real
     /EUR_BRL: Euro - Real
     /GBP_BRL: Libra - Real
     /BRL_ARS: Real - Peso Argentino
     /Outros: Acesso a outras conversões
"""

mensagem_nova_solicitacao = (
    "Para solicitar uma nova conversão, envie uma mensagem qualquer"
)


def ver_cotacao(cot: str):
    url = "https://economia.awesomeapi.com.br/last/" + cot

    conteudo = requests.get(url).json()
    lista_conteudo = list(conteudo)

    resposta = ""

    for cont in lista_conteudo:
        cotacao = conteudo[cont]
        cotacao_nome = cotacao["name"]
        cotacao_nome = cotacao_nome.replace("/", " - ").upper()
        cotacao_compra = float(cotacao["ask"])
        cotacao_venda = float(cotacao["bid"])
        cotacao_alta = float(cotacao["high"])
        cotacao_baixa = float(cotacao["low"])
        cotacao_variacao_pct = float(cotacao["pctChange"])
        cotacao_data_horario = datetime.datetime.strptime(
            cotacao["create_date"], "%Y-%m-%d %H:%M:%S"
        )
        cotacao_data_horario = cotacao_data_horario.strftime(
            "%d/%m/%y %H:%M:%S"
        )

        resposta += f"{cotacao_nome}\n\n"
        resposta += f"*Compra*: {cotacao_compra:.4f}\n"
        resposta += f"*Venda*: {cotacao_venda:.4f}\n\n"
        resposta += f"*Alta*: {cotacao_alta:.4f}\n"
        resposta += f"*Baixa*: {cotacao_baixa:.4f}\n\n"
        resposta += f"*Variação*: {cotacao_variacao_pct:.2f}%\n"
        resposta += f"*Data/Hora*: {cotacao_data_horario}\n\n"

    return resposta
