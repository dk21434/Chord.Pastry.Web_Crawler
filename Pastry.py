
class PastryNode(object):
    def __init__(self, node_identifier, scientists):
        # Αρχικοποίηση των μεταβλητών του κόμβου Pastry
        self.node_identifier = node_identifier
        self.routing_table = {}
        self.leaf_table = []
        self.neighborhood_table = []
        self.scientists = scientists

    def join(self, pastry_network):
        # Συμμετοχή κόμβου στο δίκτυο
        pass

    def leave(self, pastry_network):
        # Αφαίρεση κόμβου από το δίκτυο
        pass

    def lookup(self, lookup_key, threshold, max_awards, min_surname, max_surname):
        # Λειτουργία αναζήτησης επιστημόνων σύμφωνα με συγκεκριμένα κριτήρια
        results = []
        for scientist in self.scientists:
            if lookup_key in scientist.education and threshold < scientist.awards:
                if scientist.awards < max_awards:
                    if min_surname < scientist.surname < max_surname:
                        results.append(scientist)
                        return results


class PastryNetwork(object):
    def __init__(self):
        # Αρχικοποίηση του δικτύου
        self.nodes = {}

    def add_node(self, node):
        # Προσθήκη κόμβου στο δίκτυο
        self.nodes[node.node_identifier] = node

    def remove_node(self, node):
        # Αφαίρεση κόμβου από το δίκτυο Pastry
        del self.nodes[node.node_identifier]

    def lookup(self, lookup_key, threshold, max_awards, min_surname, max_surname):
        # Λειτουργία αναζήτησης στο δίκτυο Pastry σύμφωνα με συγκεκριμένα κριτήρια
        results = []
        for node in self.nodes.values():
            # Κάθε κόμβος εκτελεί τη μέθοδο lookup για την αναζήτηση επιστημόνων
            # Τα αποτελέσματα προστίθενται στη λίστα results
            results += node.lookup(lookup_key, threshold, max_awards, min_surname, max_surname)
            # Επιστροφή της λίστας με τα αποτελέσματα της αναζήτησης
        return results
