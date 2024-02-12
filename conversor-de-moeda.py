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
