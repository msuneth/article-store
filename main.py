import pandas as pd
import pdf_code

df = pd.read_csv("articles.csv",dtype={"id": str})


class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.article_name = df.loc[df["id"] == article_id, "name"].squeeze()
        self.article_price = df.loc[df["id"] == article_id, "price"].squeeze()
        self.article_stock = df.loc[df["id"] == article_id, "in stock"].squeeze()
        #print(self.article_name,self.article_price,self.article_stock)

    def generate_pdf(self):
        pass

    def stock_update(self):
        pass


print(df)
article_Id = input("Choose an article to buy:")
article = Article(article_Id)
