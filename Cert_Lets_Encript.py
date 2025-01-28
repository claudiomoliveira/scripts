import subprocess

def gerar_certificado_letsencrypt(domains, email, output_dir="/etc/letsencrypt/live", dry_run=True):
    """
    Gera um certificado SSL utilizando o Let's Encrypt (Certbot).
    
    :param domains: Lista de domínios para o certificado.
    :param email: Email para notificações de Let's Encrypt.
    :param output_dir: Diretório de saída dos certificados.
    :param dry_run: Simular execução sem gerar certificados reais.
    """
    try:
        command = [
            "certbot", "certonly", "--standalone",
            "--non-interactive", "--agree-tos",
            "--email", email,
            "--config-dir", output_dir,
        ] + [f"-d {domain}" for domain in domains]

        if dry_run:
            command.append("--dry-run")

        subprocess.run(command, check=True)
        print(f"Certificado gerado com sucesso! Verifique em {output_dir}.")
    except FileNotFoundError:
        print("Certbot não encontrado! Certifique-se de que está instalado.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gerar certificado com Certbot: {e}")

# Exemplo de uso:
# gerar_certificado_letsencrypt(["meudominio.com", "www.meudominio.com"], "admin@meudominio.com")
