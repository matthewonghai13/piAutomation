import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.nordstrom.com/s/canada-goose-langford-slim-fit-down-parka-with-genuine-coyote-fur-trim/3218760?origin=coordinating-3218760-0-1-PDP_1-recbot-also_viewed_graph&recs_placement=PDP_1&recs_strategy=also_viewed_graph&recs_source=recbot&recs_page_type=product&recs_seed=4509445&color=NAVY&size=xx-large")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

