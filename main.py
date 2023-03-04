import datetime

import requests
import telebot

from keys import TOKEN
from utils import (
    conversoes,
    enviar_dados,
    mensagem_nova_solicitacao,
    mensagem_padrao,
    moedas,
    moedas_sigla,
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


bot = telebot.TeleBot(TOKEN)


comando_duplo = []


@bot.message_handler(commands=conversoes)
def converter(mensagem):
    conversao = mensagem.text.replace("/", "").replace("_", "-")
    resposta = ver_cotacao(conversao)
    enviar_dados(mensagem.json)
    bot.reply_to(mensagem, resposta, parse_mode="Markdown")
    bot.send_message(mensagem.chat.id, mensagem_nova_solicitacao)


@bot.message_handler(commands=["Outros"])
def outros(mensagem):
    msg = "Clique na moeda que quer converter"
    bot.send_message(mensagem.chat.id, msg)
    bot.send_message(mensagem.chat.id, moedas)
    bot.send_message(mensagem.chat.id, msg)


@bot.message_handler(commands=moedas_sigla)
def escolher_conversao(mensagem):
    opcao = mensagem.text.replace("/", "")
    global comando_duplo
    if not comando_duplo:
        comando_duplo.append(opcao)
        msg = "Agora clique na moeda a ser convertida"
        bot.send_message(mensagem.chat.id, msg)
        bot.send_message(mensagem.chat.id, moedas)
        bot.send_message(mensagem.chat.id, msg)
    elif len(comando_duplo) == 1:
        comando_duplo.append(opcao)
        comando = "-".join(comando_duplo)
        comando_verificar = comando.replace("-", "_")
        if comando_verificar not in conversoes:
            msg = f"Não existe conversão {comando}!"
            bot.send_message(mensagem.chat.id, msg)
            bot.send_message(mensagem.chat.id, mensagem_nova_solicitacao)
            comando_duplo = []
            return
        comando_duplo = []
        resposta = ver_cotacao(comando)
        enviar_dados(mensagem.json)
        bot.send_message(mensagem.chat.id, resposta, parse_mode="Markdown")
        bot.send_message(mensagem.chat.id, mensagem_nova_solicitacao)


@bot.message_handler(commands=["Resetar", "resetar", "Reset", "reset"])
def resetar(mensagem):
    global comando_duplo
    comando_duplo = []


@bot.message_handler(func=lambda x: True)
def padrao(mensagem):
    bot.send_message(mensagem.chat.id, mensagem_padrao)


if __name__ == "__main__":
    bot.polling()
