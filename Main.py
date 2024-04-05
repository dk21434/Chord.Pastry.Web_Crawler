
from Web_Crawler import generate_data  # Εισάγουμε τη συνάρτηση generate_data από το αρχείο Web_Crawler
from Pastry import PastryNode  # Εισάγουμε την κλάση PastryNode από το αρχείο Pastry
from Chord import ChordNode  # Εισάγουμε την κλάση ChordNode από το αρχείο Chord
from Chord import ChordNetwork  # Εισάγουμε την κλάση ChordNetwork από το αρχείο Chord
from statistics import mean  # Εισάγουμε τη συνάρτηση mean από τη βιβλιοθήκη statistics
import time  # Εισάγουμε τη βιβλιοθήκη time


if __name__ == '__main__':
    # Λήψη του αριθμού των γραμμών δεδομένων που θα δημιουργηθούν
    while True:
        dataset_length = input("""Oriste to mikos tou dataset:""")
        if dataset_length.isdigit():
            dataset_length = int(dataset_length)
            break
        else:
            print("Eisagete akeraio arithmo gia to mikos tou dataset.")

    scientists_data = generate_data(dataset_length)

    # Λήψη της λειτουργικής κατάστασης/μεθόδου
    while True:
        system_mode = input("""Epilekste methodo:\n\t0: CHORD\n\t1: PASTRY\n\t""")
        if system_mode.isdigit() and int(system_mode) in [0, 1]:
            system_mode = int(system_mode)
            break
        else:
            print("Eisagete akeraio arithmo(0/1) gia ti methodo.")

    # Λήψη των παραμέτρων ερωτήματος εύρους
    while True:
        # Επώνυμο
        min_surname = input("""Elaxisto eponimo(a-z): """)
        max_surname = input("""Megisto eponimo(a-z): """)
        if min_surname.isalpha() and max_surname.isalpha() and min_surname <= max_surname:
            break
        else:
            print("Eisagete eponima gia to erwtima evrous(a-z).")

    while True:
        # Βραβεία
        min_awards = input("""Elaxistos arithmos vraviwn: """)
        max_awards = input("""Megistos arithmos vraviwn: """)
        if min_awards.isdigit() and max_awards.isdigit() and int(min_awards) <= int(max_awards):
            min_awards = int(min_awards)
            max_awards = int(max_awards)
            break
        else:
            print("Eisagete akeraio arithmo gia to evros vraviwn.")

    education = input("""Panepistimio pros anazitisi: """)


    if system_mode == 0:
        education_data = []
        for scientist in scientists_data:
            education_data.append(scientist.education)


        # Δημιουργία νέου αντικειμένου ChordNode
        node = ChordNode(0, {}, None, scientists_data)

        # Δημιουργία νέου αντικειμένου ChordNetwork
        network = ChordNetwork()

        # Προσθήκη του κόμβου στο δίκτυο
        node.join(network)

        # Εκτέλεση ερωτήματος lookup με τις δοθείσες παραμέτρους
        lookup_results = network.chord_lookup(education_data, education, min_awards, max_awards, min_surname, max_surname)

        # Εξαγωγή των αντικειμένων των επιστημόνων που ταιριάζουν με τη λίστα lookup_results
        lookup_results = [scientist for scientist in scientists_data if scientist.surname in lookup_results]

        # Εκτύπωση των αποτελεσμάτων
        if lookup_results is []:
            print("Distixos den vrethike egkiro apotelesma.")

        print(f'Vrethikan {len(lookup_results)} egkira apotelesmata:')
        for res in lookup_results:
            print(f"""\tEponimo: {res.surname}\n\tVravia: {res.awards}\n\tEkpaidefsi: {res.education}\n\t------""")

    if system_mode == 1:

        node = PastryNode(0, scientists_data)
        # Εκτέλεση ερωτήματος lookup με το min_awards ως threshold
        results = node.lookup(education, min_awards, max_awards, min_surname, max_surname)

        # Εκτύπωση των αποτελεσμάτων
        print(f'Vrethikan {len(results)} egkira apotelesmata:')
        for res in results:
            print(f"""\tEponimo: {res.surname}\n\tVravia: {res.awards}\n\tEkpaidefsi: {res.education}\n\t------""")


def column(matrix, i):
    return [row[i] for row in matrix]

#  πείραμα με προκαθορισμένα δεδομένα
def experiments():
    scale = 1
    query_times = []
    print('\nH didikasia sugkrisis einai upo ektelesi, anamenete gia tin oloklirosi tis.\n')
    for i in range(100):
        new_query_row = []
        exp_scientists_data = generate_data(100)
        min_surname = 'a'
        max_surname = 'n'
        min_awards = 3
        max_awards = 33
        education = 'CEID'

        start = time.time()
        exp_education_data = []
        for scientist in exp_scientists_data:
            education_data.append(scientist.education)


        # Δημιουργία νέου αντικειμένου ChordNode
        node = ChordNode(0, {}, None, scientists_data)

        # Δημιουργία νέου αντικειμένου ChordNetwork
        exp_network = ChordNetwork()


        # Προσθήκη του κόμβου στο δίκτυο

        node.join(network)

        # Εκτέλεση ερωτήματος lookup με τις δοθείσες παραμέτρους
        exp_lookup_results = network.chord_lookup(education_data, education, min_awards, max_awards, min_surname, max_surname)

        # Εξαγωγή των αντικειμένων των επιστημόνων που ταιριάζουν με τη λίστα lookup_results
        exp_lookup_results = [scientist for scientist in scientists_data if scientist.surname in exp_lookup_results]
        end = time.time()
        new_query_row.append(end - start)

        start = time.time()
        # Δημιουργία ενός νέου αντικειμένου PastryNode
        exp_node = PastryNode(0, scientists_data)
        # Εκτέλεση ερωτήματος lookup με το min_awards ως threshold στην Pastry
        exp_results = exp_node.lookup(education, min_awards, max_awards, min_surname, max_surname)
        end = time.time()
        new_query_row.append(end - start)

        query_times.append(new_query_row)

    print('\n\nApotelesmata:')
    print(f'Mesos xronos Chord(ms): {1000 * mean(column(query_times, 0)) / scale}')
    print(f'Mesos xronos Pastry(ms): {1000 * mean(column(query_times, 1)) / scale}')

# Ρωτήστε τον χρήστη αν θέλει να συγκρίνει τις δυο μεθόδους(Chord/Pastry)
exper_answer = input("""\n\nThelete na proxortisete se sugkrisi twn 2 methodwn? Apadiste me 1 an thelete kai me 0 an den thelete.""")

if exper_answer.lower() == '1':
    experiments()

elif exper_answer.lower() == '0':
    print('Me tin ektelesi tis diadikasias sugkrisis boreite na deite stixia gia tin apodosi.')

# Ρωτήστε τον χρήστη αν θέλει να επαναλάβει τη διαδικασία
ans = input("""\n\n\nThelte na arxisei ksana i diadikasia?Apadiste me 1 an thelete kai me 0 an den thelete.  """)
if ans == '1':
    print("\n\nH diadikasia exei oloklirothei, gia na arxisei ek neou epanekiniste to programma.")
    time.sleep(10)
    exit()

elif ans == '0':
    print("\n\nEfxaristoume gia to xrono sas.")
    time.sleep(10)
    exit()
