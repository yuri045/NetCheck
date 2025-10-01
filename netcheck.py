import socket
import argparse

# vediamo se l'host ha delle porte aperte tipo la 443
def is_port_open(host, port, timeout=2):
    try:
        with socket.create_connection((host, port), timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False
if __name__ == "__main__":    

    # parser degli argomenti da terminale

    parser = argparse.ArgumentParser(description="Controlla se una porta TCP è aperta ")
    parser.add_argument("--host", required=True, help="Host/IP da controllare")
    parser.add_argument("--port", type=int, required=True, help="Porta TCP da controllare")
    args = parser.parse_args()

 # nel caso non venissero passati da terminale, chiede direttamente all'utente 
    if not args.host:
        args.host = input("Inserisci un domio o indirizzo ip: ") # input dominio o indirizzo ip
    if not args.port:
        args.port = int(input("inserisci la porta da controllare: ")) # input porta { tipo numero intero}

    risultato = is_port_open(args.host, args.port)

    if risultato:
        print(f"✅ la porta {args.port} su host {args.host} è open.")
    else:
        print(f"❗ la porta  {args.port} su {args.host} è chiusa o non raggiungibile.")

