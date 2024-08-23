import requests

def dolar_API():
    try:
        response = requests.get('https://backend.selfspaces.com.br/cotacao-dia')
        
        # Print response status code and content for debugging
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")
        
        # Check if the response was successful
        if response.status_code == 200:
            try:
                data = response.json()
                if data and isinstance(data, list) and 'valor_final' in data[0]:
                    dolar = data[0].get('valor_final')
                    return dolar
                else:
                    print("Unexpected JSON structure:", data)
                    return "Unexpected JSON structure"
            except ValueError:
                print("Error: Response is not in JSON format")
                return "Invalid JSON"
        else:
            print(f"Error: Request failed with status code {response.status_code}")
            return f"Error {response.status_code}"
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        return "Request Exception"

# Example usage
print(dolar_API())
