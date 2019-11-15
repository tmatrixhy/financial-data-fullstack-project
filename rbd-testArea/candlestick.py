import plotly.graph_objects as go 
import pandas as pd
from datetime import datetime
import sqlalchemy as db 
import glob

#connect to database
#DATABASEURI = "postgresql://rbd2127:group69db@35.243.220.243/proj1part2"
#engine = create_engine(DATABASEURI)
#metadata = db.MetaData()
#ticker =  db.Table('ticker', metadata, autoload = True, autoload_width = engine)

#get dat file names
path = r'https://github.com/ra2929/w4111-proj1/tree/master/csv_data_for_db'
file_names = glob.glob(path + "/*.csv")

csv_files = []

#loop over csv files
for filename in file_names:
    df = pd.read_csv(filename)
    csv_files.append(df)


#create candlestick chart
graph = go.Figure(data = [go.Candlestick(x=df['Date'], open = df['AAPL.Open'], high=df['AAPL.High'],
                        low = df['AAPL.Low'], close = df['AAPL.Close'])
                        ])

graph.show()