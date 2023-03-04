mensagem_padrao = """
    Escolha uma opção de cotação (clique no item):
     /USD_BRLT: Dólar - Real Turismo
     /USD_BRL: Dolár - Real
     /EUR_BRL: Euro - Real
     /GBP_BRL: Libra - Real
     /ARS_BRL: Peso Argentino - Real
     /Outros: Acesso a outras conversões
"""

mensagem_nova_solicitacao = (
    "Para solicitar uma nova conversão, envie uma mensagem qualquer"
)

conversoes = [
    "USD_BRL",
    "USD_BRLT",
    "CAD_BRL",
    "EUR_BRL",
    "GBP_BRL",
    "ARS_BRL",
    "BTC_BRL",
    "LTC_BRL",
    "JPY_BRL",
    "CHF_BRL",
    "AUD_BRL",
    "CNY_BRL",
    "ILS_BRL",
    "ETH_BRL",
    "XRP_BRL",
    "EUR_USD",
    "CAD_USD",
    "GBP_USD",
    "ARS_USD",
    "JPY_USD",
    "CHF_USD",
    "AUD_USD",
    "CNY_USD",
    "ILS_USD",
    "BTC_USD",
    "LTC_USD",
    "ETH_USD",
    "XRP_USD",
    "BRL_USD",
    "BRL_EUR",
    "USD_EUR",
    "CAD_EUR",
    "GBP_EUR",
    "ARS_EUR",
    "JPY_EUR",
    "CHF_EUR",
    "AUD_EUR",
    "CNY_EUR",
    "ILS_EUR",
    "BTC_EUR",
    "LTC_EUR",
    "ETH_EUR",
    "XRP_EUR",
    "DOGE_BRL",
    "DOGE_EUR",
    "DOGE_USD",
    "USD_JPY",
    "USD_CHF",
    "USD_CAD",
    "NZD_USD",
    "USD_ZAR",
    "USD_TRY",
    "USD_MXN",
    "USD_PLN",
    "USD_SEK",
    "USD_SGD",
    "USD_DKK",
    "USD_NOK",
    "USD_ILS",
    "USD_HUF",
    "USD_CZK",
    "USD_THB",
    "USD_AED",
    "USD_JOD",
    "USD_KWD",
    "USD_HKD",
    "USD_SAR",
    "USD_INR",
    "USD_KRW",
    "FJD_USD",
    "GHS_USD",
    "KYD_USD",
    "SGD_USD",
    "USD_ALL",
    "USD_AMD",
    "USD_ANG",
    "USD_ARS",
    "USD_AUD",
    "USD_BBD",
    "USD_BDT",
    "USD_BGN",
    "USD_BHD",
    "USD_BIF",
    "USD_BND",
    "USD_BOB",
    "USD_BSD",
    "USD_BWP",
    "USD_BZD",
    "USD_CLP",
    "USD_CNY",
    "USD_COP",
    "USD_CRC",
    "USD_CUP",
    "USD_DJF",
    "USD_DOP",
    "USD_DZD",
    "USD_EGP",
    "USD_ETB",
    "USD_FJD",
    "USD_GBP",
    "USD_GEL",
    "USD_GHS",
    "USD_GMD",
    "USD_GNF",
    "USD_GTQ",
    "USD_HNL",
    "USD_HRK",
    "USD_HTG",
    "USD_IDR",
    "USD_IQD",
    "USD_IRR",
    "USD_ISK",
    "USD_JMD",
    "USD_KES",
    "USD_KHR",
    "USD_KMF",
    "USD_KZT",
    "USD_LAK",
    "USD_LBP",
    "USD_LKR",
    "USD_LSL",
    "USD_LYD",
    "USD_MAD",
    "USD_MDL",
    "USD_MGA",
    "USD_MKD",
    "USD_MMK",
    "USD_MOP",
    "USD_MRO",
    "USD_MUR",
    "USD_MVR",
    "USD_MWK",
    "USD_MYR",
    "USD_NAD",
    "USD_NGN",
    "USD_NIO",
    "USD_NPR",
    "USD_NZD",
    "USD_OMR",
    "USD_PAB",
    "USD_PEN",
    "USD_PGK",
    "USD_PHP",
    "USD_PKR",
    "USD_PYG",
    "USD_QAR",
    "USD_RON",
    "USD_RSD",
    "USD_RWF",
    "USD_SCR",
    "USD_SDG",
    "USD_SOS",
    "USD_STD",
    "USD_SVC",
    "USD_SYP",
    "USD_SZL",
    "USD_TND",
    "USD_TTD",
    "USD_TWD",
    "USD_TZS",
    "USD_UAH",
    "USD_UGX",
    "USD_UYU",
    "USD_UZS",
    "USD_VEF",
    "USD_VND",
    "USD_VUV",
    "USD_XAF",
    "USD_XCD",
    "USD_XOF",
    "USD_XPF",
    "USD_YER",
    "USD_ZMK",
    "AED_USD",
    "DKK_USD",
    "HKD_USD",
    "MXN_USD",
    "NOK_USD",
    "PLN_USD",
    "RUB_USD",
    "SAR_USD",
    "SEK_USD",
    "TRY_USD",
    "TWD_USD",
    "VEF_USD",
    "ZAR_USD",
    "UYU_USD",
    "PYG_USD",
    "CLP_USD",
    "COP_USD",
    "PEN_USD",
    "NIO_USD",
    "BOB_USD",
    "KRW_USD",
    "EGP_USD",
    "USD_BYN",
    "USD_MZN",
    "INR_USD",
    "JOD_USD",
    "KWD_USD",
    "USD_AZN",
    "USD_CNH",
    "USD_KGS",
    "USD_TJS",
    "USD_RUB",
    "MYR_USD",
    "UAH_USD",
    "HUF_USD",
    "IDR_USD",
    "USD_AOA",
    "VND_USD",
    "BYN_USD",
    "XBR_USD",
    "THB_USD",
    "PHP_USD",
    "USD_TMT",
    "XAGG_USD",
    "USD_MNT",
    "USD_AFN",
    "AFN_USD",
    "SYP_USD",
    "IRR_USD",
    "IQD_USD",
    "USD_NGNI",
    "USD_ZWL",
    "BRL_ARS",
    "BRL_AUD",
    "BRL_CAD",
    "BRL_CHF",
    "BRL_CLP",
    "BRL_DKK",
    "BRL_HKD",
    "BRL_JPY",
    "BRL_MXN",
    "BRL_SGD",
    "SGD_BRL",
    "AED_BRL",
    "BRL_AED",
    "BRL_BBD",
    "BRL_BHD",
    "BRL_CNY",
    "BRL_CZK",
    "BRL_EGP",
    "BRL_GBP",
    "BRL_HUF",
    "BRL_IDR",
    "BRL_ILS",
    "BRL_INR",
    "BRL_ISK",
    "BRL_JMD",
    "BRL_JOD",
    "BRL_KES",
    "BRL_KRW",
    "BRL_LBP",
    "BRL_LKR",
    "BRL_MAD",
    "BRL_MYR",
    "BRL_NAD",
    "BRL_NOK",
    "BRL_NPR",
    "BRL_NZD",
    "BRL_OMR",
    "BRL_PAB",
    "BRL_PHP",
    "BRL_PKR",
    "BRL_PLN",
    "BRL_QAR",
    "BRL_RON",
    "BRL_RUB",
    "BRL_SAR",
    "BRL_SEK",
    "BRL_THB",
    "BRL_TRY",
    "BRL_VEF",
    "BRL_XAF",
    "BRL_XCD",
    "BRL_XOF",
    "BRL_ZAR",
    "BRL_TWD",
    "DKK_BRL",
    "HKD_BRL",
    "MXN_BRL",
    "NOK_BRL",
    "NZD_BRL",
    "PLN_BRL",
    "SAR_BRL",
    "SEK_BRL",
    "THB_BRL",
    "TRY_BRL",
    "TWD_BRL",
    "VEF_BRL",
    "ZAR_BRL",
    "BRL_PYG",
    "BRL_UYU",
    "BRL_COP",
    "BRL_PEN",
    "BRL_BOB",
    "CLP_BRL",
    "PYG_BRL",
    "UYU_BRL",
    "COP_BRL",
    "PEN_BRL",
    "BOB_BRL",
    "RUB_BRL",
    "INR_BRL",
    "EUR_GBP",
    "EUR_JPY",
    "EUR_CHF",
    "EUR_AUD",
    "EUR_CAD",
    "EUR_NOK",
    "EUR_DKK",
    "EUR_PLN",
    "EUR_NZD",
    "EUR_SEK",
    "EUR_ILS",
    "EUR_TRY",
    "EUR_THB",
    "EUR_ZAR",
    "EUR_MXN",
    "EUR_SGD",
    "EUR_HUF",
    "EUR_HKD",
    "EUR_CZK",
    "EUR_KRW",
    "BHD_EUR",
    "EUR_AED",
    "EUR_AFN",
    "EUR_ALL",
    "EUR_ANG",
    "EUR_ARS",
    "EUR_BAM",
    "EUR_BBD",
    "EUR_BDT",
    "EUR_BGN",
    "EUR_BHD",
    "EUR_BIF",
    "EUR_BND",
    "EUR_BOB",
    "EUR_BSD",
    "EUR_BWP",
    "EUR_BYN",
    "EUR_BZD",
    "EUR_CLP",
    "EUR_CNY",
    "EUR_COP",
    "EUR_CRC",
    "EUR_CUP",
    "EUR_CVE",
    "EUR_DJF",
    "EUR_DOP",
    "EUR_DZD",
    "EUR_EGP",
    "EUR_ETB",
    "EUR_FJD",
    "EUR_GHS",
    "EUR_GMD",
    "EUR_GNF",
    "EUR_GTQ",
    "EUR_HNL",
    "EUR_HRK",
    "EUR_HTG",
    "EUR_IDR",
    "EUR_INR",
    "EUR_IQD",
    "EUR_IRR",
    "EUR_ISK",
    "EUR_JMD",
    "EUR_JOD",
    "EUR_KES",
    "EUR_KHR",
    "EUR_KWD",
    "EUR_KYD",
    "EUR_KZT",
    "EUR_LAK",
    "EUR_LBP",
    "EUR_LKR",
    "EUR_LSL",
    "EUR_LYD",
    "EUR_MAD",
    "EUR_MDL",
    "EUR_MGA",
    "EUR_MKD",
    "EUR_MMK",
    "EUR_MOP",
    "EUR_MRO",
    "EUR_MUR",
    "EUR_MWK",
    "EUR_MYR",
    "EUR_NAD",
    "EUR_NGN",
    "EUR_NIO",
    "EUR_NPR",
    "EUR_OMR",
    "EUR_PAB",
    "EUR_PEN",
    "EUR_PGK",
    "EUR_PHP",
    "EUR_PKR",
    "EUR_PYG",
    "EUR_QAR",
    "EUR_RON",
    "EUR_RSD",
    "EUR_RWF",
    "EUR_SAR",
    "EUR_SCR",
    "EUR_SDG",
    "EUR_SDR",
    "EUR_SOS",
    "EUR_STD",
    "EUR_SVC",
    "EUR_SYP",
    "EUR_SZL",
    "EUR_TND",
    "EUR_TTD",
    "EUR_TWD",
    "EUR_TZS",
    "EUR_UAH",
    "EUR_UGX",
    "EUR_UYU",
    "EUR_UZS",
    "EUR_VEF",
    "EUR_VND",
    "EUR_XAF",
    "EUR_XOF",
    "EUR_XPF",
    "EUR_ZMK",
    "GHS_EUR",
    "NZD_EUR",
    "SGD_EUR",
    "AED_EUR",
    "DKK_EUR",
    "EUR_XCD",
    "HKD_EUR",
    "MXN_EUR",
    "NOK_EUR",
    "PLN_EUR",
    "RUB_EUR",
    "SAR_EUR",
    "SEK_EUR",
    "TRY_EUR",
    "TWD_EUR",
    "VEF_EUR",
    "ZAR_EUR",
    "MAD_EUR",
    "KRW_EUR",
    "EGP_EUR",
    "EUR_MZN",
    "INR_EUR",
    "JOD_EUR",
    "KWD_EUR",
    "EUR_AZN",
    "EUR_AMD",
    "EUR_TJS",
    "EUR_RUB",
    "HUF_EUR",
    "GEL_EUR",
    "EUR_GEL",
    "IDR_EUR",
    "EUR_AOA",
    "BYN_EUR",
    "XAGG_EUR",
    "PEN_EUR",
]

moedas = """
/AED: Dirham dos Emirados
/AFN: Afghani do Afeganistão
/ALL: Lek Albanês
/AMD: Dram Armênio
/ANG: Guilder das Antilhas
/AOA: Kwanza Angolano
/ARS: Peso Argentino
/AUD: Dólar Australiano
/AZN: Manat Azeri
/BAM: Marco Conversível
/BBD: Dólar de Barbados
/BDT: Taka de Bangladesh
/BGN: Lev Búlgaro
/BHD: Dinar do Bahrein
/BIF: Franco Burundinense
/BND: Dólar de Brunei
/BOB: Boliviano
/BRL: Real Brasileiro
/BRLT: Real Brasileiro Turismo
/BSD: Dólar das Bahamas
/BTC: Bitcoin
/BWP: Pula de Botswana
/BYN: Rublo Bielorrusso
/BZD: Dólar de Belize
/CAD: Dólar Canadense
/CHF: Franco Suíço
/CLP: Peso Chileno
/CNH: Yuan chinês offshore
/CNY: Yuan Chinês
/COP: Peso Colombiano
/CRC: Colón Costarriquenho
/CUP: Peso Cubano
/CVE: Escudo cabo-verdiano
/CZK: Coroa Checa
/DJF: Franco do Djubouti
/DKK: Coroa Dinamarquesa
/DOGE: Dogecoin
/DOP: Peso Dominicano
/DZD: Dinar Argelino
/EGP: Libra Egípcia
/ETB: Birr Etíope
/ETH: Ethereum
/EUR: Euro
/FJD: Dólar de Fiji
/GBP: Libra Esterlina
/GEL: Lari Georgiano
/GHS: Cedi Ganês
/GMD: Dalasi da Gâmbia
/GNF: Franco de Guiné
/GTQ: Quetzal Guatemalteco
/HKD: Dólar de Hong Kong
/HNL: Lempira Hondurenha
/HRK: Kuna Croata
/HTG: Gourde Haitiano
/HUF: Florim Húngaro
/IDR: Rupia Indonésia
/ILS: Novo Shekel Israelense
/INR: Rúpia Indiana
/IQD: Dinar Iraquiano
/IRR: Rial Iraniano
/ISK: Coroa Islandesa
/JMD: Dólar Jamaicano
/JOD: Dinar Jordaniano
/JPY: Iene Japonês
/KES: Shilling Queniano
/KGS: Som Quirguistanês
/KHR: Riel Cambojano
/KMF: Franco Comorense
/KRW: Won Sul-Coreano
/KWD: Dinar Kuwaitiano
/KYD: Dólar das Ilhas Cayman
/KZT: Tengue Cazaquistanês
/LAK: Kip Laosiano
/LBP: Libra Libanesa
/LKR: Rúpia de Sri Lanka
/LSL: Loti do Lesoto
/LTC: Litecoin
/LYD: Dinar Líbio
/MAD: Dirham Marroquino
/MDL: Leu Moldavo
/MGA: Ariary Madagascarense
/MKD: Denar Macedônio
/MMK: Kyat de Mianmar
/MNT: Mongolian Tugrik
/MOP: Pataca de Macau
/MRO: Ouguiya Mauritana
/MUR: Rúpia Mauriciana
/MVR: Rufiyaa Maldiva
/MWK: Kwacha Malauiana
/MXN: Peso Mexicano
/MYR: Ringgit Malaio
/MZN: Metical de Moçambique
/NAD: Dólar Namíbio
/NGN: Naira Nigeriana
/NIO: Córdoba Nicaraguense
/NOK: Coroa Norueguesa
/NPR: Rúpia Nepalesa
/NZD: Dólar Neozelandês
/OMR: Rial Omanense
/PAB: Balboa Panamenho
/PEN: Sol do Peru
/PGK: Kina Papua-Nova Guiné
/PHP: Peso Filipino
/PKR: Rúpia Paquistanesa
/PLN: Zlóti Polonês
/PYG: Guarani Paraguaio
/QAR: Rial Catarense
/RON: Leu Romeno
/RSD: Dinar Sérvio
/RUB: Rublo Russo
/RWF: Franco Ruandês
/SAR: Riyal Saudita
/SCR: Rúpias de Seicheles
/SDG: Libra Sudanesa
/SDR: DSE
/SEK: Coroa Sueca
/SGD: Dólar de Cingapura
/SOS: Shilling Somaliano
/STD: Dobra São Tomé/Príncipe
/SVC: Colon de El Salvador
/SYP: Libra Síria
/SZL: Lilangeni Suazilandês
/THB: Baht Tailandês
/TJS: Somoni do Tajiquistão
/TMT: TMT
/TND: Dinar Tunisiano
/TRY: Nova Lira Turca
/TTD: Dólar de Trinidad
/TWD: Dólar Taiuanês
/TZS: Shilling Tanzaniano
/UAH: Hryvinia Ucraniana
/UGX: Shilling Ugandês
/USD: Dólar Americano
/UYU: Peso Uruguaio
/UZS: Som Uzbequistanês
/VEF: Bolívar Venezuelano
/VND: Dong Vietnamita
/VUV: Vatu de Vanuatu
/XAF: Franco CFA Central
/XAGG: XPrata
/XBR: Brent Spot
/XCD: Dólar do Caribe Oriental
/XOF: Franco CFA Ocidental
/XPF: Franco CFP
/XRP: XRP
/YER: Riyal Iemenita
/ZAR: Rand Sul-Africano
/ZMK: Kwacha Zambiana
/ZWL: Dólar Zimbabuense
"""

moedas_sigla = [
    "AED",
    "AFN",
    "ALL",
    "AMD",
    "ANG",
    "AOA",
    "ARS",
    "AUD",
    "AZN",
    "BAM",
    "BBD",
    "BDT",
    "BGN",
    "BHD",
    "BIF",
    "BND",
    "BOB",
    "BRL",
    "BRL",
    "BSD",
    "BTC",
    "BWP",
    "BYN",
    "BZD",
    "CAD",
    "CHF",
    "CLP",
    "CNH",
    "CNY",
    "COP",
    "CRC",
    "CUP",
    "CVE",
    "CZK",
    "DJF",
    "DKK",
    "DOG",
    "DOP",
    "DZD",
    "EGP",
    "ETB",
    "ETH",
    "EUR",
    "FJD",
    "GBP",
    "GEL",
    "GHS",
    "GMD",
    "GNF",
    "GTQ",
    "HKD",
    "HNL",
    "HRK",
    "HTG",
    "HUF",
    "IDR",
    "ILS",
    "INR",
    "IQD",
    "IRR",
    "ISK",
    "JMD",
    "JOD",
    "JPY",
    "KES",
    "KGS",
    "KHR",
    "KMF",
    "KRW",
    "KWD",
    "KYD",
    "KZT",
    "LAK",
    "LBP",
    "LKR",
    "LSL",
    "LTC",
    "LYD",
    "MAD",
    "MDL",
    "MGA",
    "MKD",
    "MMK",
    "MNT",
    "MOP",
    "MRO",
    "MUR",
    "MVR",
    "MWK",
    "MXN",
    "MYR",
    "MZN",
    "NAD",
    "NGN",
    "NIO",
    "NOK",
    "NPR",
    "NZD",
    "OMR",
    "PAB",
    "PEN",
    "PGK",
    "PHP",
    "PKR",
    "PLN",
    "PYG",
    "QAR",
    "RON",
    "RSD",
    "RUB",
    "RWF",
    "SAR",
    "SCR",
    "SDG",
    "SDR",
    "SEK",
    "SGD",
    "SOS",
    "STD",
    "SVC",
    "SYP",
    "SZL",
    "THB",
    "TJS",
    "TMT",
    "TND",
    "TRY",
    "TTD",
    "TWD",
    "TZS",
    "UAH",
    "UGX",
    "USD",
    "UYU",
    "UZS",
    "VEF",
    "VND",
    "VUV",
    "XAF",
    "XAGG",
    "XBR",
    "XCD",
    "XOF",
    "XPF",
    "XRP",
    "YER",
    "ZAR",
    "ZMK",
    "ZWL",
]
