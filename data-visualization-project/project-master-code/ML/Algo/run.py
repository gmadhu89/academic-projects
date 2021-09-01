#!/usr/bin/python

import sys
import numpy as np
from statsmodels.iolib.smpickle import load_pickle

print("Number of arguments:", len(sys.argv), "arguments.")
print("Argument List:", str(sys.argv))

experiment = sys.argv[1]
new_results = load_pickle(experiment + "_sales_possion_model.pickle")

df_arbitray_value = np.array(
    [float(sys.argv[2]), float(sys.argv[3]), sys.argv[4] == "True"]
)
ypred = new_results.predict(df_arbitray_value)
print(ypred)
