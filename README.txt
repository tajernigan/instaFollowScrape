# Instagram Followers Scraper

This project allows you to scrape Instagram followers and following, store the data in a JSON file, and then parse this data for further analysis.

### Installation

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/tajernigan/instaFollowScrape.git
   cd instaFollowScrape

2. **Install Requirements**

   ```bash
   pip install -r requirements.txt

3. **scrape followers**
    ```bash
    python scrapeFollowers.py 

This will create a json file "USERNAME.json"

4. **Alter followers and following data**
    ```bash
    python parseJson.py {USERNAME}.json