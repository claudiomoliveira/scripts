from acme import client, messages, crypto_util
from acme.client import ClientV2
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography import x509
from cryptography.x509.oid import NameOID
import OpenSSL

def gerar_certificado_acme(server_url, email, domain):
    """
    Gera um certificado SSL utilizando o protocolo ACME.
    
    :param server_url: URL do servidor ACME (ex.: Let's Encrypt ou outro).
    :param email: Email do administrador.
    :param domain: Domínio para o certificado.
    """
    try:
        # Criação da chave privada
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        private_key_pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        # Geração do CSR (Certificate Signing Request)
        csr = crypto_util.make_csr(private_key=key, domains=[domain])

        # Configuração do cliente ACME
        directory = client.Directory.from_json(server_url)
        net = client.ClientNetwork(key)
        client_acme = ClientV2(directory, net)
        registration = client_acme.new_account(messages.NewRegistration.from_data(email=email))

        # Solicitação do certificado
        order = client_acme.new_order(csr)
        print(f"Certificado solicitado para {domain}.")
        print("Desafios e validações precisam ser implementados aqui dependendo da ACME.")

        # Simples retorno da chave privada e CSR
        return private_key_pem, csr

    except Exception as e:
        print(f"Erro ao gerar certificado com ACME: {e}")

# Exemplo de uso:
# gerar_certificado_acme("https://acme-v02.api.letsencrypt.org/directory", "admin@meudominio.com", "meudominio.com")
