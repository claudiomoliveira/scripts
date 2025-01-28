import socket

def verificar_portas(ip, portas=[80, 443, 22, 21, 3389, 8080]):
    """Verifica as portas abertas no IP informado."""
    for porta in portas:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            resultado = s.connect_ex((ip, porta))
            if resultado == 0:
                print(f"Porta {porta} aberta no IP {ip}.")
            else:
                print(f"Porta {porta} fechada no IP {ip}.")

# Exemplo de uso:
# verificar_portas("192.168.1.1", [22, 80, 443])
