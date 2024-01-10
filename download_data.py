import os
from dotenv import load_dotenv
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

load_dotenv()

ZINDI_AUTH_TOKEN = os.getenv('ZINDI_AUTH_TOKEN')

train_url=f'https://api.zindi.africa/v1/competitions/zindiweekendz-learning-urban-air-pollution-challenge/files/Train.csv?auth_token={ZINDI_AUTH_TOKEN}'
test_url=f'https://api.zindi.africa/v1/competitions/zindiweekendz-learning-urban-air-pollution-challenge/files/Test.csv?auth_token={ZINDI_AUTH_TOKEN}'

train_data=pd.read_csv(train_url)
test_data=pd.read_csv(test_url)

train_data.to_csv('data/Train.csv')
test_data.to_csv('data/Test.csv')
