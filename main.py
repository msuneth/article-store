import pandas as pd
#from pdf_code import PDF
from fpdf import FPDF

df = pd.read_csv("articles.csv",dtype={"id": str})


class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.article_name = df.loc[df["id"] == article_id, "name"].squeeze().title()
        self.article_price = df.loc[df["id"] == article_id, "price"].squeeze()
        self.article_stock = df.loc[df["id"] == article_id, "in stock"].squeeze()
        #print(self.article_name,self.article_price,self.article_stock)

    def stock_update(self):
        df.loc[df["id"]== article_Id,"in stock"] = self.article_stock - 1
        df.to_csv("articles.csv",index=False)
        print("stock updated")

    def generate_pdf(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article_name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article_price}", ln=1)
        pdf.output("receipt.pdf")
        print("pdf generated")



print(df)
article_Id = input("Choose an article to buy:")
article = Article(article_Id)
article.generate_pdf()
article.stock_update()
