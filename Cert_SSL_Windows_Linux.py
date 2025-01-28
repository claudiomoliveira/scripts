import subprocess

def gerar_certificado(cert_name, output_dir="."):
    """Gera um certificado autoassinado."""
    command = [
        "openssl", "req", "-x509", "-nodes", "-days", "365",
        "-newkey", "rsa:2048",
        "-keyout", f"{output_dir}/{cert_name}.key",
        "-out", f"{output_dir}/{cert_name}.crt",
        "-subj", f"/CN={cert_name}"
    ]
    try:
        subprocess.run(command, check=True)
        print(f"Certificado e chave gerados em {output_dir}")
    except FileNotFoundError:
        print("OpenSSL não encontrado! Certifique-se de que está instalado e no PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gerar certificado: {e}")

# Exemplo de uso:
# gerar_certificado("meu_certificado", "/tmp")
