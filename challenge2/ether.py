import requests

def print_transfers(transaction_hash):
    api_key = 'Check my mail for the Key'

    etherscan_url = f'https://api.etherscan.io/api'

    # Define the parameters for the API request
    params = {
        'module': 'logs',
        'action': 'getLogs',
        'apikey': api_key,
        'txhash': transaction_hash,
    }

    try:
        # API request
        response = requests.get(etherscan_url, params=params)
        print(response.text)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == '1':
                # Extract and print the transfer logs
                logs = data.get('result')
                transfers = []

                for log in logs:
                    transfer = {
                        'from': log.get('topics')[1],
                        'to': log.get('topics')[2],
                        'amount': int(log.get('data'), 16),
                    }
                    transfers.append(transfer)

                return transfers
            else:
                return "Transaction not found or API request failed."

        else:
            return "API request failed."

    except Exception as e:
        return str(e)

# Example usage:
transaction_hash = '0x3fbb21da357fdd74a12319ee423b4f30829030ba53b1d8d9e005c0da138e2263'
transfers = print_transfers(transaction_hash)
print(transfers)

