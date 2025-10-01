# NetCheck 🔍

NetCheck è un semplice tool sviluppato in Python per verificare se una porta TCP su un host specificato è aperta o chiusa.  
Questo progetto nasce come esercitazione e dimostra competenze base di networking, programmazione Python, uso di librerie standard e gestione della CLI.

---

## Funzionalità principali

- Verifica la raggiungibilità di un host tramite controllo della porta TCP
- Supporto interattivo (input da tastiera) e da riga di comando (CLI) tramite `argparse`
- Messaggi chiari di successo o fallimento della connessione
- Test automatici implementati con `pytest`

---

## Requisiti

- Python 3.x
- Librerie standard `socket` e `argparse`
- Libreria `pytest` (facoltativa, per eseguire i test)

---

## Come usare NetCheck

### Modalità interattiva

Avvia lo script senza argomenti e inserisci host e porta quando richiesti:

```bash
python netcheck.py
```

### Modalità CLI (interfaccia a riga di comando)

Avvia lo script passando i parametri direttamente da terminale:

```bash
python netcheck.py --host google.com --port 443
```

## Struttura del progetto
```
NetCheck/
├── netcheck.py          # Script principale
├── test_netcheck.py     # Test automatici con pytest
├── requirements.txt     # Librerie richieste
├── README.md            # Documentazione progetto
└── .gitignore           # File da ignorare da Git
```
## ♠ Autore
Creato da Vallone Yuri 