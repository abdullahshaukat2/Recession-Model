import pandas as pd
import pandas_datareader as pdr
from pandas_datareader.data import DataReader

start = "1970-01-01"
end = None
usrec = DataReader("USREC", "fred", start, end)


