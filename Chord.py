
class ChordNode:
    def __init__(self, node_identifier, successor_nodes, predecessor_node, data):
        #  Αρχικοποίηση των μεταβλητών του κόμβου Chord
        self.node_identifier = node_identifier
        self.successor_nodes = successor_nodes
        self.predecessor_node = predecessor_node
        self.data = data

    def find_successor(self, key):
        #  Εύρεση του επόμενου κόμβου (successor_node)
        if key in self.successor_nodes:
            return self.successor_nodes[key]
        else:
            # Εάν το κλειδί δεν βρεθεί στους επόμενους κόμβους
            # επιστρέφεται ο πρώτος κόμβος μεγαλύτερου κλειδιού από το key
            filtered = filter(lambda x: x > key, self.successor_nodes.keys())
            print(list(filtered))  # Εκτύπωση των τιμών της φιλτραρισμένης λίστας
            if not filtered:
                if not self.successor_nodes:
                    print("self.successor_node is empty")
                return self.successor_nodes[min(self.successor_nodes.keys())]
            else:
                return self.successor_nodes[min(filtered)]

    def join(self, network):
        #  Συμμετοχή κόμβου στο δίκτυο
        if not network.nodes:
            network.add_node(self)
            return

        successor = network.nodes[0]
        for node in network.nodes.values():
            if self.node_identifier < node.node_identifier < successor.node_identifier:
                successor = node

        self.successor_nodes[successor.node_identifier] = successor
        self.predecessor_node = successor.predecessor_node
        successor.predecessor_node = self

        network.add_node(self)

    def leave(self, network):
        #  Αποχώρηση κόμβου από το δίκτυο
        for successor in self.successor_nodes.values():
            successor.predecessor_node = self.predecessor_node
        self.predecessor_node.successor_nodes.update(self.successor_nodes)
        network.remove_node(self)

    def lookup(self, education_data, education, min_awards, max_awards, min_surname, max_surname):
        #  Αναζήτηση επιστημόνων σύμφωνα με κριτήρια εκπαίδευσης,
        #  βραβείων και επιθυμητών επιθέτων
        scientists_data = self.data

        surnames = [scientist.surname for scientist in scientists_data if
                    education in scientist.education and scientist.awards > min_awards and scientist.awards < max_awards and max_surname> scientist.surname > min_surname]

        #  Εκτύπωση επιθέτων
        return surnames


class ChordNetwork:
    def __init__(self):
        # Αρχικοποίηση του δικτύου
        self.nodes = {}

    def add_node(self, node):
        #  Προσθήκη κόμβου στο δίκτυο
        self.nodes[node.node_identifier] = node

    def remove_node(self, node):
        #  Αφαίρεση κόμβου από το δίκτυο
        del self.nodes[node.node_identifier]

    def chord_lookup(self, education_data, education, min_awards, max_awards, min_surname, max_surname):
        #  Αναζήτηση στο δίκτυο για επιστήμονες σύμφωνα με συγκεκριμένα κριτήρια
        return self.nodes[0].lookup(education_data, education, min_awards, max_awards, min_surname, max_surname)
        #  Eπιστροφή των αποτελεσμάτων της αναζήτησης
