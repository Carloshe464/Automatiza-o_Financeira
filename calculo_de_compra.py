from cotacao_spot import obter_cotacao_spot

def compra(total_carteira, cotacao):

    valor_moeda_em_dolar = float(input("Digite o preço da moeda em dolar: "))
    total_de_moedas = float(input("Digite o total de moedas compradas: "))
    preco = valor_moeda_em_dolar 
    posicao = total_de_moedas
    posicao_dolar = posicao * preco
    
    if cotacao is not None:
        total_carteira = posicao_dolar * cotacao
        return total_carteira
    else:
        print(f'Não foi possivel obter a cotacao.')
        return None

total_carteira = 0
    
api_key = 'fc8936dc03264db5b0c9440586d6c5ee'
base_currency = 'USD'
target_currency = 'BRL'

cotacao_spot = obter_cotacao_spot(api_key, base_currency, target_currency)

total_carteira = compra(total_carteira, cotacao_spot)

if total_carteira is not None:
    print(f'Valor convertido para {target_currency}: {total_carteira}')





