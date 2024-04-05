
import csv  # Εισάγουμε το πακέτο csv για τη διαχείριση αρχείων CSV
import random  # Εισάγουμε το πακέτο random για τη δημιουργία τυχαίων αριθμών
import names  # Εισάγουμε το πακέτο names

# Λίστα με τα πανεπιστήμια στην επιστήμη των υπολογιστών
cs_universities = [
    "MIT",
    "CEID",
    "Stanford University",
    "Carnegie Mellon University",
    "UC Berkeley",
    "Princeton University",
    "Harvard University",
    "Caltech",
    "Cornell University",
    "University of Chicago",
    "Columbia University",
    "New York University",
    "Rice University",
    "University of Texas - Austin",
    "University of Illinois - Urbana-Champaign",
    "University of Maryland - College Park",
    "University of Pennsylvania",
    "Yale University",
    "Cambridge",
    "Berkley",
    "Oxford University",
    "Johns Hopkins University",
    "University of College London",
    "Tsinghua University",
    "Ohio State University",
    "University of Tokyo",
    "National University of Singapore",
    "University of Pittsburgh",
    "McGill University",
    "Nanyang Technological University",
    "University of Melbourne",
    "Catholic University of Leuven",
    "University of Sydney",
    "Shanghai Jiao Tong University",
    "University of California--Irvine"

]


class Scientist(object):
    def __init__(self, s, a, d, e):
        self.surname = s  # Επώνυμο
        self.awards = a  # Βραβεία
        self.description = d  # Περιγραφή
        self.education = e  # Εκπαίδευση


def generate_data(dataset_length):
    # Ορισμός του ονόματος του αρχείου CSV
    file_id = "WikiScientists_short.csv"

    # Άνοιγμα του αρχείου CSV με κωδικοποίηση UTF-8
    with open(file_id, encoding="UTF-8") as file:
        # Μετατροπή κεφαλαίων γραμμάτων σε πεζά
        data = file.read().lower()

        # Δημιουργία αντικειμένου αναγνώστη CSV
        reader = csv.reader(data.splitlines())

        # Εξαγωγή δεδομένων από το αρχείο CSV
        scientists = []
        row_count = 0  # Αρχικοποίηση μετρητή
        for row in reader:
            try:
                name, description = row[0].split(" - ")
            except ValueError:
                continue
            surname = name.split()[-1]
            awards = random.randint(0, 30)
            education = random.sample(cs_universities, 5)
            # Δημιουργία νέου αντικειμένου Scientist
            scientists.append(Scientist(surname, awards, description, education))
            row_count += 1  # Αύξηση μετρητή


        # Προσθήκη τυχαία δημιουργημένων επιστημόνων αν είναι απαραίτητο
        if dataset_length > row_count:
            # Δημιουργία λίστας με τα υπάρχοντα επώνυμα
            used_surnames = [scientist.surname for scientist in scientists]
            for x in range(dataset_length - row_count):
                surname = names.get_last_name().lower()
                while surname in used_surnames:
                    surname = names.get_last_name().lower()
                used_surnames.append(surname)
                awards = random.randint(0, 30)
                education = random.sample(cs_universities, 5)
                # Ορισμός της περιγραφής ως κενό string
                scientist = Scientist(surname, awards, "", education)
                scientists.append(scientist)

        # Επιστροφή των επιστημόνων
        data = scientists
        return data
