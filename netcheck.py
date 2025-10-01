import socket

# vediamo se l'host ha delle porte aperte tipo la 443
def is_port_open(host, port, timeout=2):
    try:
        with socket.create_connection((host, port), timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False
if __name__ == "__main__":    
    host = input("Inserisci un domio o indirizzo ip: ") # input dominio o indirizzo ip
    port = int(input("inserisci la porta da controllare: ")) # input porta { tipo numero intero}

    risultato = is_port_open(host, port)

    if risultato:
        print(f"✅ la porta {port} su host {host} è open.")
    else:
        print(f"❗ la porta  {port} su {host} è chiusa o non raggiungibile.")