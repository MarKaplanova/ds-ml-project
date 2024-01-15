import joblib
import pandas as pd
import numpy as np
import sys
import argparse

from mace.util import (
    interpolate_by,
    drop_columns,
    sort_by
)

parser=argparse.ArgumentParser(description="""
Read a joblib 'model' and csv 'data', outputing .predict(data) as 'target'
""")
parser.add_argument("model", nargs='?', default="models/model.joblib")
parser.add_argument("data", nargs='?', default="data/test.csv")
parser.add_argument("--target", nargs='?', default="target.csv")
args=parser.parse_args()

model_path = args.model
data_path = args.data
target_path= args.target

model = joblib.load(model_path)
features = model.feature_names_in_
data = pd.read_csv(data_path)[features]
pred = model.predict(data)

target = pd.DataFrame(pred, columns=['target'])
output = pd.concat([data['Place_ID X Date'], target], axis=1)

output.to_csv(target_path, index=False)

