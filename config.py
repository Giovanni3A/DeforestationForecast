import os
import pandas as pd

# data folder
DATA_PATH = r"C:\Users\GiovanniAmorim\Pessoal\Mestrado\DL2CV\data"

# data layers
RAW_DATA_PATH = os.path.join(DATA_PATH, "raw")
TRUSTED_DATA_PATH = os.path.join(DATA_PATH, "trusted")

# raw data
AMAZON_FRONTIER_DATA = os.path.join(RAW_DATA_PATH, "brazilian_legal_amazon")
INITIAL_DEFORESTATION = os.path.join(RAW_DATA_PATH, "accumulated_deforestation_2007")
DETER_DATA = os.path.join(RAW_DATA_PATH, "deter-amz-public-2023set08")
PRODES_DATA = os.path.join(RAW_DATA_PATH, "yearly_deforestation")
COUNTIES_DATA = os.path.join(RAW_DATA_PATH, "municipios")
RAIN_DATA = os.path.join(RAW_DATA_PATH, "precipitations")

# trusted data
TR_DEFORESTATION = os.path.join(TRUSTED_DATA_PATH, "deforestation.csv")
TR_FRAMES = os.path.join(TRUSTED_DATA_PATH, "frames_detail")
TR_FRAMES_IDX = os.path.join(TRUSTED_DATA_PATH, "frames_idx.csv")
TR_COUNTIES = os.path.join(TRUSTED_DATA_PATH, "counties.csv")
TR_COUNTIES_DEFOR = os.path.join(TRUSTED_DATA_PATH, "counties_defor.csv")
TR_RAIN_AVG = os.path.join(TRUSTED_DATA_PATH, "avg_precipitation.csv")

# temporal limits
DT_INIT = "2016-07-01"
DT_FIM = "2023-06-30"
TIME_STEPS = pd.date_range(
    DT_INIT,
    DT_FIM,
    freq="QS",
)

# spatial and input size parameters
BOX_SIDE = 0.01 * 3
INPUT_BOXES_SIZE = 64
