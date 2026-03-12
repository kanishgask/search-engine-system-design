class IndexService:

    def __init__(self):
        self.index = {}

    def index_document(self, doc_id, content):

        words = content.split()

        for word in words:

            if word not in self.index:
                self.index[word] = []

            self.index[word].append(doc_id)

    def get_index(self):

        return self.index
