import datetime

import requests
import telebot

from keys import TOKEN


def ver_cotacao(cot: str):
    url = "https://economia.awesomeapi.com.br/last/" + cot

    conteudo = requests.get(url).json()
    lista_conteudo = list(conteudo)

    resposta = ""

    for cont in lista_conteudo:
        cotacao = conteudo[cont]
        cotacao_nome = cotacao["name"]
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

        resposta += f"{cotacao_nome}\n"
        resposta += f"Compra: {cotacao_compra:.4f}\n"
        resposta += f"Venda: {cotacao_venda:.4f}\n"
        resposta += f"Alta: {cotacao_alta:.4f}\n"
        resposta += f"Baixa: {cotacao_baixa:.4f}\n"
        resposta += f"Variação: {cotacao_variacao_pct:.2f}%\n"
        resposta += f"Data/Hora: {cotacao_data_horario}\n\n"

    return resposta


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["USD_BRL"])
def USD_BRL(mensagem):
    resposta = ver_cotacao("USD-BRL")
    bot.reply_to(mensagem, resposta)


@bot.message_handler(commands=["USD_BRLT"])
def USD_BRLT(mensagem):
    resposta = ver_cotacao("USD-BRLT")
    bot.reply_to(mensagem, resposta)


@bot.message_handler(commands=["EUR_BRL"])
def EUR_BRL(mensagem):
    resposta = ver_cotacao("EUR-BRL")
    bot.reply_to(mensagem, resposta)


@bot.message_handler(func=lambda x: True)
def mensagem_padrao(mensagem):
    msg = """
    Escolha uma opção de cotação (clique no item):
     /USD_BRL
     /USD_BRLT
     /EUR_BRL
    Responder qualquer outra opção não vai funcionar, clique em uma das opções!
    """
    bot.send_message(mensagem.chat.id, msg)


if __name__ == "__main__":
    bot.polling()
