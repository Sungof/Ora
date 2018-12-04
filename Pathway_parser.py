from Bio.KEGG.KGML.KGML_parser import read
import Bio.KEGG.KGML.KGML_pathway


class Node:
    def __init__(self, names):
        self.gene = names
        self.weight = 0


class Parser:

    def __init__(self):
        self.path = {}

    def get_path(self):
        return self.path

    def parse(self, file):

        def _set_gene(way, path):
            gene_name = [e.name for e in way.entries.values() if e.type == 'gene']
            ent_id = [e.id for e in way.entries.values() if e.type == 'gene']
            name = _parse_name(gene_name)
            for i in range(len(name)):
                path[ent_id[i]] = Node(name[i])

        def _parse_name(nodes):
            names = []
            for node in nodes:
                names.append(node.split())
            return names

        def _set_weight(way, path):

            for relation in way.relations:

                if relation.entry1.type == 'gene' and relation.entry2.type == 'gene':
                    path[relation.entry1.id].weight += 1
                    path[relation.entry2.id].weight += 1

        pathway = read(open(file), 'r')
        _set_gene(pathway, self.path)
        _set_weight(pathway, self.path)


p = Parser()
p.parse('hsa04150.xml')
d = p.get_path()
#path = read(open('hsa04150.xml'), 'r')

#ent = path.entries.copy()
#print([e.name for e in path.entries.values() if e.type == 'gene'])

#print([e.name for e in path.entries.values() if e.type == 'compound'])

#print("\n".join([e.name for e in path.entries.values() if e.type == 'gene']))
#arr = [e.type for e in path.entries.values()]