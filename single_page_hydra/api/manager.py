from single_page_hydra.api.clients import (
    pixapi,
    WikiAPI,
)


class ApiManager:
    def __init__(self):
        self._clients = [
            pixapi(),
            WikiAPI(),
        ]

    def search(self, query):
        results = dict()

        for client in self._clients:
            result = client.search(query)
            results.update(result)

        return results
