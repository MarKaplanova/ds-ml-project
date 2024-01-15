# Urban Air Pollution

Zindi Challenge regarding [Air Pollution](https://zindi.africa/competitions/urban-air-pollution-challenge) in African cities by using RMSE as evaluation metric.

## Description

 Using collected weather data and daily observations from the Sentinel 5P satellite tracking various pollutants in the atmosphere to predict PM2.5 particulate matter concentration (a common measure of air quality that normally requires ground-based sensors to measure) every day for each city. The data covers January to March of 2020, spanning hundreds of cities across the globe.

## Data

Main sources of the data:
- **Ground-based air quality sensors** : Target (daily mean PM2.5 Concentration), minimum and maximum readings on that day, the variance of the readings and the total number (count) of sensor readings used to compute the target value. This data is only provided for the train set - **we must predict the target variable for the test set.**
- **The Global Forecast System (GFS)** : Humidity, temperature and wind speed.
- **The Sentinel 5P satellite** : Monitors various pollutants in the atmosphere.(read more about the individual products [here](https://developers.google.com/earth-engine/datasets/catalog/sentinel-5p)


Download data for this project: 
1. Train.csv, Test.csv, SampleSubmission.csv [from](https://zindi.africa/competitions/zindiweekendz-learning-urban-air-pollution-challenge/data)

2. Run `download_data.py` in terminal.
 - Windows:
    ```sh
    python .\download_data.py
    ```
- Linux or macOS:
    ```sh
    python ./download_data.py
    ```

Note that your auth_token from your Zindi competition page must be placed in the .env file for download_data.py to work.

## Set up the Environment

This repo contains a requirements.txt file with a list of all the packages and dependecies you will need.

### **`macOS`** type the following commands : 
 Install the virtual environment and the required packages by following commands:
  There are two ways to create and activate a new virtual environment for this repo. You can either use the [requirements](requirements.txt) file and run the following commands.

```BASH
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
  
  *Note: If there are errors during environment setup, try removing the versions from the failing packages in the requirements file.*

### **`WindowsOS`** type the following commands :

 Install the virtual environment and the required packages by following commands:

For `PowerShell` CLI :

```PowerShell
pyenv local 3.11.3
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

For `Git-Bash` CLI :
  
```BASH
pyenv local 3.11.3
python -m venv .venv
source .venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
```

 **`Note:`**
    If you encounter an error when trying to run `pip install --upgrade pip`, try using the following command:

   ```Bash
   python.exe -m pip install --upgrade pip
   ```

## Executing program

In order to train the model and store test data in the data folder and the model in models run:

**`Note`**: Make sure your environment is activated.

```bash
python ./predict.py  
```

In order to test that predict works on a test set you created run:

```bash
python ./predict.py models/gs_final.joblib data/Test.csv
```

## Presentation 

Feel free to check on our presentation for Stakeholder : 
https://prezi.com/view/DVSQefHYd564gALRreMF/