import requests

def criar_client_id(base_url, realm, admin_user, admin_password, client_name):
    """Cria um client no Keycloak usando a API."""
    try:
        # Obter token de admin
        token_url = f"{base_url}/realms/master/protocol/openid-connect/token"
        payload = {
            "client_id": "admin-cli",
            "username": admin_user,
            "password": admin_password,
            "grant_type": "password"
        }
        token_response = requests.post(token_url, data=payload)
        token_response.raise_for_status()
        access_token = token_response.json().get("access_token")

        # Criar o client no realm especificado
        client_url = f"{base_url}/admin/realms/{realm}/clients"
        headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
        client_payload = {
            "clientId": client_name,
            "enabled": True,
        }
        client_response = requests.post(client_url, headers=headers, json=client_payload)
        client_response.raise_for_status()

        print(f"Client '{client_name}' criado com sucesso!")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao interagir com o Keycloak: {e}")

# Exemplo de uso:
# criar_client_id("http://localhost:8080", "meu_realm", "admin", "admin123", "meu_client_id")