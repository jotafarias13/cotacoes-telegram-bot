#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""fetch.py: baixa, através da API de economia Awesome API as informações
de moedas e possíveis conversões.

Através dos dados obtidos, é possível encontrar as moedas (em siglas)
disponíveis, as conversões disponíveis e a descrição de cada sigla, isto é,
o nome da moeda por extenso.

"""
__author__ = "João Lucas Correia Barbosa de Farias"
__license__ = "GNU GENERAL PUBLIC LICENSE 3"
__version__ = "1.0.0"
__maintainer__ = "João Lucas Correia Barbosa de Farias"
__email__ = "fariasjota09@gmail.com"
__status__ = "Production"

import requests

url_conversoes = "https://economia.awesomeapi.com.br/json/available"
conteudo_conversoes = requests.get(url_conversoes).json()
conversoes_raw = conteudo_conversoes.keys()
moedas_all = "-".join(conteudo_conversoes.keys()).split("-")
moedas_unicas = list(set(moedas_all))

url_moedas = "https://economia.awesomeapi.com.br/json/available/uniq"
conteudo_moedas = requests.get(url_moedas).json()

moedas_disponiveis = {
    key: value
    for key, value in conteudo_moedas.items()
    if key in moedas_unicas
}

moedas_descricao = [
    "/" + key + ": " + value for key, value in moedas_disponiveis.items()
]

descricao_string = "\n".join(moedas_descricao)

conversoes = [conv.replace("-", "_") for conv in conversoes_raw]
moedas = descricao_string
moedas_sigla = sorted(moedas_unicas)
