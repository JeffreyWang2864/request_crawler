from bs4 import BeautifulSoup

class parse:
    def startParse(self, old_url, html_out):
        soup = BeautifulSoup(html_out, 'html.parser', from_encoding='utf-8')
        comments = soup.find_all('div', class_='review-content')
        sentences = list()
        stars = list()
        for comment in comments:
            sentence = comment.p.get_text().strip()
            sentences.append(sentence.replace("\xa0", ""))
            stars.append(int(comment.div.div.div.img['alt'][0]))
        next_link = soup.find('a', class_='u-decoration-none next pagination-links_anchor')
        if next_link is None:
            next_url = None
        else: next_url = next_link['href']
        data = {a : b for a, b in zip(sentences, stars)}
        return next_url, data