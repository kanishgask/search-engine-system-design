class SearchService:

    def __init__(self, index_service):
        self.index_service = index_service

    def search(self, query):

        index = self.index_service.get_index()

        return index.get(query, [])
