from datetime import datetime
import nselib
from nselib import capital_market
import pandas as pd

# Fetch historical data for Nifty Smallcap 250 directly from NSE
start_date = "01-01-2025"
end_date = datetime.today().strftime("%d-%m-%Y")

try:
  df_smallcap = capital_market.index_data(
      index="Nifty Smallcap 250", from_date=start_date, to_date=end_date
  )
  print("Successfully fetched Nifty Smallcap 250 data:")
  print(df_smallcap.tail())
except Exception as e:
  print(f"Error fetching data: {e}")
