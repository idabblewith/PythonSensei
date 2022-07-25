

def prac():
    response = requests.get("https://news.ycombinator.com/")
    contents = response.text
    # print(contents)
    soup = BeautifulSoup(contents, 'html.parser')
    
    articles = soup.find_all(name='a', class_="storylink")

    art_texts = []
    art_links = []
    for article_tag in articles:

        text = article_tag.getText()
        art_texts.append(text)

        link = article_tag.get("href")
        art_links.append(link)

    article_votes = [int(upvotes.getText().split()[0]) for upvotes in soup.find_all(name="span", class_="score")]

    # print(votes)
    highest_vote = max(article_votes)
    hv_index = article_votes.index(highest_vote)
    

    print(f'\nARTICLE: {art_texts[hv_index]},\nLINK: {art_links[hv_index]},\nVOTES: {article_votes[hv_index]}\n')

    # print(art_texts)
    # print(art_links)
    # print(article_votes)






    # PRACTICE
    # with open("./complete/Day_045/website.html", encoding="utf-8") as file:
    #     contents = file.read()
    #     # print(contents)

    # soup = BeautifulSoup(contents, 'html.parser')
    # company_url = soup.select_one(selector="p a").get('href')
    # # company_url = soup.select_one(selector=".heading").get('href')
    # print(company_url)
    # print(soup.title.string)
    # all_anchor_tags = soup.find_all(name="a")
    # all_paragraph_tags = soup.find_all(name="p")
    # for tag in all_anchor_tags:
        # print(tag.getText())
        # print(tag.get("href"))

    # heading = soup.find(name="h1", id="name")
    # heading = soup.find(name="h3", class_="heading")
    # print(heading.getText())