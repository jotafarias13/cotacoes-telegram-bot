import telebot

from keys import TOKEN, verificar_cotacao
from utils import (
    conversoes,
    mensagem_nova_solicitacao,
    mensagem_padrao,
    moedas,
    moedas_sigla,
    ver_cotacao,
)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=conversoes)
def converter(mensagem):
    conversao = mensagem.text.replace("/", "").replace("_", "-")
    resposta = ver_cotacao(conversao)
    verificar_cotacao(mensagem.json)
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
    msg = "Agora clique na moeda a ser convertida"
    bot.send_message(mensagem.chat.id, msg)
    lista_conversao = [conv for conv in conversoes if conv.startswith(opcao)]

    convertido = [c.split("_")[1] for c in lista_conversao]
    moedas_lista = moedas.split("\n")
    descricao = []
    for conv in convertido:
        for ml in moedas_lista:
            if ml.startswith("/" + conv + ":"):
                descricao.append(ml.split(":")[1].strip())
                break

    opcao_moeda = ""
    for ml in moedas_lista:
        if ml.startswith("/" + opcao + ":"):
            opcao_moeda = ml.split(":")[1].strip()

    resposta = opcao_moeda + "\n\n"
    for conv, desc in zip(lista_conversao, descricao):
        resposta += "/" + conv + ": " + desc + "\n"

    bot.send_message(mensagem.chat.id, resposta)
    bot.send_message(mensagem.chat.id, msg)


@bot.message_handler(func=lambda x: True)
def padrao(mensagem):
    bot.send_message(mensagem.chat.id, mensagem_padrao)


if __name__ == "__main__":
    bot.polling()
