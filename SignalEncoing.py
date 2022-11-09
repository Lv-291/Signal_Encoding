from tkinter import * 
import tkinter as tk
from random import randint
import turtle
from turtle import TurtleScreen

# L'importo di tutte le librerie usate


mod = {"NRZI": True, "Manchester": False, "Biopolar-AMI": False, "Pseudoternary": False,
       "Differential Manchester": False, "NRZ-L": False}

# Dizionario che contiene tutte le mod di encoding disponibili, i loro valori servono a far iniziare il programma con il tasto NRZI attivo


def Random():
    # Questa funzione collegata al tasto "Random" genera appunto una serie di 11 bit casuali

    random_bits = []
    # inizializzazione della lista che conterra i bits
    for i in range(11):
        random_bits.append(str(randint(0, 1)))
        # Ogni indirizzo della lista avra il suo bit random (fatto con la funzione randint(0,1), che genera un numero compreso da 0 e 1)

    random_bits = "".join(random_bits)
    # La lista di stringhe viene trasformata in una stringa
    bits.delete(0, "end")
    # Qui viene eliminato il contenuto della casella bits(dove vengono contenuti i bit)
    bits.insert(0, random_bits)
    # Viene inserito nella casella precedentemente cancellata il contenuto di random_bits(la stinga di bit)


def Manchester():
    # Questa funzione è collegato al tasto di "Manchester Encoding"

    for i in mod.keys():
        # Questo "for" serve a "disattivare" tutte le mod tranne una in particolare che invece viene attivata
        if i == "Manchester":
            mod[i] = True
        else:
            mod[i] = False

    nrz_button.config(bg="white")
    diff_manchester_button.config(bg="white")
    nrzl_button.config(bg="white")
    pseudoternary_button.config(bg="white")
    biopolar_button.config(bg="white")
    # i colori di tutti i tasti diventano bianchi
    manchester_button.config(bg="light blue")
    # il colore del tasto da "attivare" diventa verdechiaro


def NRZI():
    # Questa funzione è collegata al tasto di "Nrz-I Encoding", il contenuto viene spiegato nella funzione "Manchester"

    for i in mod.keys():
        if i == "NRZI":
            mod[i] = True
        else:
            mod[i] = False

    manchester_button.config(bg="white")
    diff_manchester_button.config(bg="white")
    nrzl_button.config(bg="white")
    pseudoternary_button.config(bg="white")
    biopolar_button.config(bg="white")

    nrz_button.config(bg="light blue")


def Biopolar_AMI():
    # Questa funzione è collegata al tasto di "Biopolar-AMI Encoding", il contenuto viene spiegato nella funzione "Manchester"

    for i in mod.keys():
        if i == "Biopolar-AMI":
            mod[i] = True
        else:
            mod[i] = False

    manchester_button.config(bg="white")
    nrz_button.config(bg="white")
    diff_manchester_button.config(bg="white")
    nrzl_button.config(bg="white")
    pseudoternary_button.config(bg="white")

    biopolar_button.config(bg="light blue")


def Pseudoternary():
    # Questa funzione è collegata al tasto di "Pseudoternary Encoding", il contenuto viene spiegato nella funzione "Manchester"

    for i in mod.keys():
        if i == "Pseudoternary":
            mod[i] = True
        else:
            mod[i] = False

    manchester_button.config(bg="white")
    nrz_button.config(bg="white")
    diff_manchester_button.config(bg="white")
    nrzl_button.config(bg="white")
    biopolar_button.config(bg="white")

    pseudoternary_button.config(bg="light blue")


def NRZ_L():
    # Questa funzione è collegata al tasto di "NRZ-L Encoding", il contenuto viene spiegato nella funzione "Manchester"

    for i in mod.keys():
        if i == "NRZ-L":
            mod[i] = True
        else:
            mod[i] = False

    manchester_button.config(bg="white")
    nrz_button.config(bg="white")
    diff_manchester_button.config(bg="white")
    pseudoternary_button.config(bg="white")
    biopolar_button.config(bg="white")

    nrzl_button.config(bg="light blue")


def Diff_Manchester():
    # Questa funzione è collegata al tasto di "Differential Manchester", il contenuto viene spiegato nella funzione "Manchester"

    for i in mod.keys():
        if i == "Differential Manchester":
            mod[i] = True
        else:
            mod[i] = False

    manchester_button.config(bg="white")
    nrz_button.config(bg="white")
    nrzl_button.config(bg="white")
    pseudoternary_button.config(bg="white")
    biopolar_button.config(bg="white")

    diff_manchester_button.config(bg="light blue")


def Fdd(n):
    # Questa funzione serve a creare linee tratteggiate su turtle
    for i in range(5):
        maxwell.fd(n / 10)
        maxwell.up()
        maxwell.fd(n / 10)
        maxwell.down()


def Credits():
    feynman.up()
    feynman.goto(-400, 50)
    feynman.forward(25)
    feynman.down()
    feynman.color("purple")
    for i in "BAIUNCO":
        feynman.write(i, font=("verdana", 40, "normal"))
        feynman.up()
        feynman.fd(100 * x)
        feynman.down()
    feynman.up()
    feynman.goto(-400, -30)
    feynman.forward(25)
    feynman.down()
    for i in "CRISTIAN":
        feynman.write(i, font=("verdana", 40, "normal"))
        feynman.up()
        feynman.fd(100 * x)
        feynman.down()
    feynman.up()
    feynman.goto(-400, 170)
    feynman.forward(25)
    feynman.down()
    feynman.color("black")


def Genera():
    # Questa è la funzione collegata al tasto genera

    feynman.clear()
    # Ogni volta che si preme il tasto genera, tutto quello costruito dalla turtle "feynman" viene cancellato. (feynman viene utilizzato per disegnare il segnale metre maxwell per il menu)

    feynman.up()
    feynman.goto(-400, 170)
    feynman.forward(25)
    feynman.down()
    # dopo aver disattivato la penna viene messa nella posizione di "origine"

    feynman.color("black")
    # vien cambiato il colore della penna perche poi diventera rosso

    bit = bits.get()
    # La funzione .get() permette di prendere la stinga contenuta nella cella bit

    if bit == "credits":
        Credits()
    # fa una funzione speciale

    for i in range(len(bit)):
        feynman.write(bit[i], font=("arial", 30, "normal"))
        feynman.up()
        feynman.fd(100 * x)
        feynman.down()
    # Questo "for" permette di scrivere i bit

    feynman.up()
    feynman.goto(-400, 170)
    feynman.down()
    feynman.color("red")
    feynman.pensize(2)
    # La penna viene riposizionata, cambiata di colore e aumentata in dimensioni per rendere il segnale piu visibie

    selezione = 0
    for key, value in mod.items():
        # questo for trova l unica mod attivata e la salva dentro la variabile selezione
        if value is True:
            selezione = key

    if selezione == "NRZI":
        # se il tasto nrzi è attivo...
        segno = True
        # questa variabile serve per capire se la penna si trova in alto nel segnale (True) o in basso (False)

        for i in range(len(bit)):
            # questo for disegna il segnale
            if bit[i] == "0":
                # se è 0 vai avanti
                feynman.forward(100 * x)
            elif bit[i] == "1":
                # se è 1 guarda se è in basso o in alto
                if segno is True:
                    # se è in alto cambia direzione verso il basso e vai avanti
                    feynman.right(90)
                    feynman.forward(200 * x)
                    feynman.left(90)
                    feynman.forward(100 * x)
                    segno = False
                elif segno is False:
                    # se è in basso cambia direzione verso l alto e vai avanti
                    feynman.left(90)
                    feynman.forward(200 * x)
                    feynman.right(90)
                    feynman.forward(100 * x)
                    segno = True

    elif selezione == "Manchester":
        # se il tasto machester è attivo...
        for i in range(len(bit)):
            # questo for disegna il segnale
            if bit[i] == "0":
                # se è 0 fai questa forma
                feynman.forward(50 * x)
                feynman.right(90)
                feynman.forward(200 * x)
                feynman.left(90)
                feynman.forward(50 * x)
                feynman.up()
                feynman.left(90)
                feynman.forward(200 * x)
                feynman.right(90)
                feynman.down()
            elif bit[i] == "1":
                # se è 1 fai quest altra forma
                feynman.right(90)
                feynman.up()
                feynman.forward(200 * x)
                feynman.left(90)
                feynman.down()
                feynman.forward(50 * x)
                feynman.left(90)
                feynman.forward(200 * x)
                feynman.right(90)
                feynman.forward(50 * x)

            if i != len(bit) - 1 and bit[i] == bit[i + 1]:
                feynman.right(90)
                feynman.forward(200 * x)
                feynman.left(180)
                feynman.forward(200 * x)
                feynman.right(90)
            # questo if disegna il "collegamento" del segnale quando 2 bit uguali sono vicini

    elif selezione == "Biopolar-AMI":
        # se il tasto biopolar è attivo...
        last_1 = False
        feynman.up()
        feynman.right(90)
        feynman.forward(100 * x)
        feynman.left(90)
        feynman.down()
        for i in range(len(bit)):
            # questo for disegna il segnale
            if bit[i] == "0":
                # se è 0 fai...
                feynman.forward(100 * x)
            elif bit[i] == "1":

                if last_1 is False:
                    feynman.left(90)
                    feynman.forward(100 * x)
                    feynman.right(90)
                    feynman.forward(100 * x)
                    feynman.right(90)
                    feynman.forward(100 * x)
                    feynman.left(90)
                    last_1 = True
                elif last_1 is True:
                    feynman.right(90)
                    feynman.forward(100 * x)
                    feynman.left(90)
                    feynman.forward(100 * x)
                    feynman.left(90)
                    feynman.forward(100 * x)
                    feynman.right(90)
                    last_1 = False

    elif selezione == "Pseudoternary":
        last_1 = False
        feynman.up()
        feynman.right(90)
        feynman.forward(100 * x)
        feynman.left(90)
        feynman.down()
        for i in range(len(bit)):

            if bit[i] == "1":

                feynman.forward(100 * x)
            elif bit[i] == "0":

                if last_1 is False:
                    feynman.left(90)
                    feynman.forward(100 * x)
                    feynman.right(90)
                    feynman.forward(100 * x)
                    feynman.right(90)
                    feynman.forward(100 * x)
                    feynman.left(90)
                    last_1 = True
                elif last_1 is True:
                    feynman.right(90)
                    feynman.forward(100 * x)
                    feynman.left(90)
                    feynman.forward(100 * x)
                    feynman.left(90)
                    feynman.forward(100 * x)
                    feynman.right(90)
                    last_1 = False

    elif selezione == "Differential Manchester":
        # se il tasto machester è attivo...
        for i in range(len(bit)):

            if bit[i] == "1":

                feynman.forward(50 * x)
                feynman.right(90)
                feynman.forward(200 * x)
                feynman.left(90)
                feynman.forward(50 * x)
                feynman.up()
                feynman.left(90)
                feynman.forward(200 * x)
                feynman.right(90)
                feynman.down()
            elif bit[i] == "0":

                feynman.right(90)
                feynman.up()
                feynman.forward(200 * x)
                feynman.left(90)
                feynman.down()
                feynman.forward(50 * x)
                feynman.left(90)
                feynman.forward(200 * x)
                feynman.right(90)
                feynman.forward(50 * x)

            if i != len(bit) - 1 and bit[i] == bit[i + 1]:
                feynman.right(90)
                feynman.forward(200 * x)
                feynman.left(180)
                feynman.forward(200 * x)
                feynman.right(90)

    elif selezione == "NRZ-L":
        segno = False
        for i in range(len(bit)):
            if bit[i] == "0":
                if segno is True:
                    feynman.left(90)
                    feynman.forward(200 * x)
                    feynman.right(90)
                    feynman.forward(100 * x)
                    segno = False
                else:
                    feynman.forward(100 * x)

            elif bit[i] == "1":
                if segno is False:
                    feynman.right(90)
                    feynman.forward(200 * x)
                    feynman.left(90)
                    feynman.forward(100 * x)
                    segno = True
                else:
                    feynman.forward(100 * x)

    screen.update()
    # Aggiorna lo schermo



root = Tk()
# questo è lo schermo di tkinter
root.title('Trasposizione da bit a segnali')
root.geometry('900x440')
root.resizable(False, False)
# viene definito il titolo della finestra, le sue dimensioni e se puo essere ridimensionato (no)

root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=2)
root.columnconfigure(3, weight=1)
# servono per "ridimensionare" le celle di tiker(tiker usa uno schema di posizionamento a griglia)

bits = tk.Entry(root, font=("Helvetica 44 bold", 15))
bits.grid(row=0, column=0, sticky=EW, padx=20, pady=10)
# la casella dove inserire i bits che si vuole trasformare in segnale

random = tk.Button(text="Random", command=Random, bg="white", width=15, height=2)
random.grid(row=1, column=0, sticky=W, padx=20, pady=10)
# tasto "random"

nrz_button = tk.Button(text="NRZ-I Encoding", command=NRZI, bg="light blue")
nrz_button.grid(row=0, column=1, sticky=E)
# tasto NRZ-I Encoding

nrzl_button = tk.Button(text="NRZ-L Encoding", command=NRZ_L, bg="white")
nrzl_button.grid(row=1, column=1, sticky=E)
# tasto NRZ-L Encoding

manchester_button = tk.Button(text="Manchester Encoding", command=Manchester, bg="white")
manchester_button.grid(row=0, column=2, sticky=W, padx=20, pady=10)
# tasto Manchester Encoding

diff_manchester_button = tk.Button(text="Differential Manchester", command=Diff_Manchester, bg="white")
diff_manchester_button.grid(row=1, column=2, sticky=W, padx=20, pady=10)
# tasto Differential Manchester


biopolar_button = tk.Button(text="Biopolar-AMI Encoding", command=Biopolar_AMI, bg="white")
biopolar_button.grid(row=0, column=2, sticky=E, padx=20, pady=10)
# tasto Biopolar-AMI (Encoding)

pseudoternary_button = tk.Button(text="Pseudoternary Encoding", command=Pseudoternary, bg="white")
pseudoternary_button.grid(row=1, column=2, sticky=E, padx=20, pady=10)
# tasto Pseudoternary Encoding

generate = tk.Button(text="Genera", command=Genera, bg="light green", width=25, height=2)
generate.grid(row=1, column=0, padx=20, sticky=E, pady=10)
# Tasto genera

canvas = Canvas(root, width=900, height=510, )
canvas.grid(row=3, columnspan=3, pady=10)
# qui viene generato lo porzione di schermo di tkinter con modificabile con  turtule

screen = TurtleScreen(canvas)
# viene trasformato in uno schemo interamente turtle

screen.tracer(False)
# le animazioni sono bloccate

maxwell = turtle.RawTurtle(screen)
maxwell.hideturtle()
# crea una penna e viene nascosta la sua freccia

feynman = turtle.RawTurtle(screen)
feynman.hideturtle()
# crea una penna e viene nascosta la sua freccia

x = 0.7
# il moltiplicatore serve a ridimensionare le proporzioni del disegno

maxwell.up()
maxwell.goto(-400, 170)
maxwell.down()
# la penna viene posizionata nell "origine"

# il codice sottostante disegna il sistema di griglia
for i in range(11):
    Fdd(100 * x)

for j in range(2):
    maxwell.up()
    maxwell.right(180)
    for i in range(11):
        maxwell.fd(100 * x)

    maxwell.left(90)
    maxwell.fd(100 * x)
    maxwell.left(90)

    maxwell.down()
    for i in range(11):
        Fdd(100 * x)

maxwell.up()
maxwell.right(90)
maxwell.fd(100 * x)
maxwell.right(180)
maxwell.down()

for j in range(11):
    for i in range(4):
        Fdd(100 * x)
    maxwell.up()
    maxwell.left(90)
    maxwell.fd(100 * x)
    maxwell.left(90)

    for i in range(4):
        maxwell.fd(100 * x)
    maxwell.left(180)
for i in range(4):
    Fdd(100 * x)

screen.update()
# lo schermo viene aggiornato

root.mainloop()
# d ora in poi il programma sara in un loop infinito
