
# ------- Importing the useful libraries and modules ------------------
import PySimpleGUI as pg
from bs4 import BeautifulSoup
import requests



# ------------- Creating the GUI ---------------------------

def create_file(url, file_name):

    try:

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title_of_the_articles = []
        links = []

        # Scrapp Title Articles
        article_tags = soup.find_all("article")
        for article in article_tags:
            h3_tag = article.find("h3")
            h3_content = h3_tag.text
            title_of_the_articles.append(h3_content)

        # Scrap Links Articles
        for article in article_tags:
            h3_tag = article.find("h3")

            for a in h3_tag:
                
                a_link = h3_tag.find("a")
                href_value = a_link.get("href")
                href_link = href_value[1:]
                link = "https://news.google.com" + href_link

                links.append(link)
      

        # Make the headlines
        headlines = {
            title: link for title, link in zip(
                title_of_the_articles,
                links)
            }
        
        # Write the txt file with the articles
        with open(file_name, "w") as file:

            for key, value in headlines.items():
                
                file.write(f"Title of Article:\n{key} \nLink of article:\n{value}\n\n")
        
    except Exception as e:
        print(e)

def create_scraping_window():
    # Theme for the GUI
    pg.theme('Purple')

    # Widgets
    layout = [
        [pg.Text("                                  "),
         pg.Text("Enter Correct URL")],
        [pg.Text("URL: "), pg.InputText(key="_INPUT01_")],
        [pg.Text("Name of Save File: "), pg.InputText(key="_INPUT02_")],
        [pg.Button("Scrap!")]
    ]

    # Create the Window
    window = pg.Window('Google News Scraping', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == pg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        
        if event == "Scrap!" and (values["_INPUT01_"] != "" and values["_INPUT02_"] != ""):
            
            url = values["_INPUT01_"]
            file_name = values["_INPUT02_"] + ".txt"
            
            # Function to scrap data
            create_file(url, file_name)
  
            
    # Close Window
    window.close()

    
# Main Program
if __name__ == "__main__":
    create_scraping_window()


