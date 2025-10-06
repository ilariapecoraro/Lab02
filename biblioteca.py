def carica_da_file(file_path):
    """Carica i libri dal file"""

    try:
        with open(file_path,'r',encoding = 'utf-8') as infile:
            biblioteca = {}
            n = int(readline(infile).strip()) # nella prima riga c'è il numero di sezioni
            from csv import reader
            csv_reader = reader(infile) # restituisce un oggetto su cui si può iterare
            for row in csv_reader: # ogni iterazione restituisce una lista di stringhe
                if len(row) < 5: # in ogni lista ci sono 5 elementi
                    continue
                sezione = row[4].strip()
                sezione = int(sezione )#trasformo la stringa in numero intero
                titolo = row[0].strip()
                autore = row[1].strip()
                anno = row[2].strip()
                num_pagine = row[3].strip()
                libro = {'titolo': titolo, # ogni libro è un dizionario
                        'autore': autore,
                        'anno': anno,
                        'num_pagine': num_pagine}
                if (sezione < 0 ) or (sezione > n):
                    return None # controllo che la sezione esita
                if sezione not in biblioteca: # controlla che la chiave non sia già in biblioteca
                    biblioteca[sezione] = libro # aggiunge una nuova coppia chiave-valore, con una lista come valore
                else:
                    biblioteca[sezione].append(libro) #aggiunge il nuovo libro al valore della chiave sezione
            return biblioteca # restituisce il dizionario biblioteca al termine della lettura del file
    except FileNotFoundError: # eccezione : il file non viene trovato, bisogna risolvere il problema
        print('File non trovato. ')
        return None



    # TODO


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    if sezione not in biblioteca: # se la sezione non è presente : errore
        print('La sezione non è presente. ')
        return None
    for sezione , libri in biblioteca.items(): # ottengo una tupla chiave-valore
        for libro in libri: # itero sui dizionari "libro" presenti nella lista valore
            if libro['titolo'].lower() == titolo.lower(): # il titolo è unico per ogni libro
                return None # non serve aggiungere un libro già presente in biblioteca
    try:
        nuovo_libro = {'titolo': titolo,
                    'autore': autore,
                    'anno': anno,
                    'num_pagine': num_pagine } # definisce il nuovo dizionario "libro" da inserire
        biblioteca[sezione].append((nuovo_libro)) # lo aggiunge alla lista dei valori del dizionario
        with open(file_path,'w',encoding = 'utf-8') as outfile: # apre il file di scrittura
            from csv import writer
            csv_writer = writer(outfile)
            csv_writer.writerow(nuovo_libro) # scrive la riga da aggiungere al file
        return nuovo_libro
    except FileNotFounfError: # controlla che il file esiste
        print('File non trovato. ')
        return None

    """Aggiunge un libro nella biblioteca"""
    # TODO


def cerca_libro(biblioteca, titolo):
    for sezione , libri in biblioteca.items(): # forma le tuple chiave-valore con chiave = sezione, valore = lista di libri
        for libro in libri: # per ogni libro della lista libri
            if libro['titolo'].lower() == titolo.lower(): # controlla che il titolo del libro cercato sia presente in biblioteca
                return (f"{libro['titolo']}', {libro['autore']}, {libro['anno']}, {libro['num_pagine']},{sezione}")
            else:
                print('Il libro non è presente nella biblioteca') # il libro non è presente
                return None
"""Cerca un libro nella biblioteca dato il titolo"""
    # TODO


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    if sezione not in biblioteca: # se la sezione di libri da ordinare non esiste segnala errore
        return None
    elenco_titoli = [] # inizializzo la lista dei titoli
    for libro in biblioteca[sezione]: # per ogni libro nella sezione scelta della biblioteca
        elenco_titoli.append(libro['titolo']) # aggiunge il titolo dei libri nella lista
    return sorted(elenco_titoli,key = str.lower() ) # restituisce l'elenco dei titoli dei libri ordinati senza
                                                    # tenere conto delle maiuscole
"""Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

