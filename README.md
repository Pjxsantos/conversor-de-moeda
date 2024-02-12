# Conversor-de-moeda

Vamos criar um **conversor de moeda** em Python que converte dólares americanos (USD) para reais brasileiros (BRL). Existem várias maneiras de fazer isso, mas vou mostrar um exemplo simples usando a taxa de câmbio atual.

1. **Usando uma API de conversão de moeda:**
Vamos usar a API **ExchangeRate-API** para obter as taxas de câmbio em tempo real.
Primeiro, instale a biblioteca requests usando o seguinte comando:
```yaml
pip install requests
```
Agora, crie um arquivo chamado currency_converter.py e adicione o seguinte código:
```yaml
import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"].get(target_currency)

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

if __name__ == "__main__":
    base_currency = "USD"
    target_currency = "BRL"
    amount_usd = float(input("Digite o valor em dólares (USD): "))
    
    exchange_rate_brl = get_exchange_rate(base_currency, target_currency)
    if exchange_rate_brl:
        amount_brl = convert_currency(amount_usd, exchange_rate_brl)
        print(f"{amount_usd:.2f} USD = {amount_brl:.2f} BRL")
    else:
        print("Não foi possível obter a taxa de câmbio. Verifique sua conexão com a internet.")
```
2. **Executando o código:**

Execute o script acima no terminal.
Digite o valor em dólares (USD) que deseja converter para reais (BRL).
O programa buscará a taxa de câmbio atual e exibirá o valor equivalente em reais.

3. **Observações:**

Certifique-se de estar conectado à internet para obter as taxas de câmbio em tempo real.
Você pode personalizar o código para adicionar mais moedas ou melhorar a interface do usuário.

**Lembre-se de que este é apenas um exemplo básico. Você pode expandir o conversor de moeda adicionando mais recursos, como histórico de taxas, gráficos ou uma interface gráfica com Tkinter. Divirta-se criando seu próprio conversor de moeda! 💰🌎**
