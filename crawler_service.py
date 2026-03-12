class CrawlerService:

    def __init__(self):
        self.pages = []

    def crawl(self, url):

        page = {
            "url": url,
            "content": f"Sample content from {url}"
        }

        self.pages.append(page)

        return page
