# SimpleStockApp

### Installing and Running:
As this project is just one python file, simply download and open the file.

To run type `streamlit run .\StockWebApp.py` into the console.

It will run locally and open up the default browser to `http://localhost:8501/` which will be running the SimpleStockApp.

### Description:
Utilizing streamlit and yahoo finance, it is possible to quickly create a simply stock app.
By using streamlit to provide a user interface as well as graphes and by using yahoo finance to provide stock info as well as verify if the stock is valid.

Takes the user's input, validates the stock, and then displays data according to the dates inputted. If the dates are not in range, it will ignore the future dates if possible, otherwise it will not display the data. 
