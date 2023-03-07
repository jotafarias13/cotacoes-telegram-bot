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
