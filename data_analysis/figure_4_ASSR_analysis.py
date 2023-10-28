from power_calculation import *
from data import mice_data, mouse_names
import pandas as pd
import numpy as np

CHANNEL = 'Aux1'
INJECT = 'Ketamine'
WEEK = 'week_0'

ecog_records = mice_data[WEEK][INJECT]["after_5_min"]

time = np.linspace(0, 3, 6000)
freq = np.linspace(20, 70, 51)

baseline_list = []
response_list = []
ratio_list = []
plf_list = []

for num in range(len(ecog_records)):
    # For every ecog record calculating power and itc parameters
    power, itc = calc_itpc_power(import_ecog(ecog_records[num]).pick_channels([CHANNEL]))
    # From power param which takes freq values from 20 to 90 Hz (power_calculation.py function) we extract values from
    # 20 to 70 Hz
    data_power = np.array(power.data[0][0:51])
    data_power_df = pd.DataFrame(data_power, index=freq, columns=time)
    data_itc = np.array(itc.data[0][0:51])
    data_itc_df = pd.DataFrame(data_itc, index=freq, columns=time)
    # For 40 Hz ASSR response we only take [39:41] Hz frequency values
    assr_power_freq = data_power_df[(data_power_df.index >= 39) & (data_power_df.index <= 41)].transpose()
    assr_itc_freq = data_itc_df[(data_itc_df.index >= 39) & (data_itc_df.index <= 41)].transpose()
    # To extract 40 Hz baseline parameter we choose epoch time interval from 0.2 s to 0.9 s
    baseline = assr_power_freq[(assr_power_freq.index >= 0.2) & (assr_power_freq.index <= 0.9)]
    # To extract 40 Hz ASSR response parameter we choose epoch time interval from 1.2 s to 1.9 s
    response = assr_power_freq[(assr_power_freq.index >= 1.2) & (assr_power_freq.index <= 1.9)]
    response_itc = assr_itc_freq[(assr_itc_freq.index >= 1.2) & (assr_itc_freq.index <= 1.9)]
    # Calculate mean for every 40 Hz param
    baseline_mean = baseline.mean().mean()
    response_mean = response.mean().mean()
    response_itc_mean = response_itc.mean().mean()
    # Calculate 40 Hz ASSR power ratio
    ratio = response_mean / baseline_mean
    baseline_list.append(baseline_mean)
    response_list.append(response_mean)
    ratio_list.append(ratio)
    plf_list.append(response_itc_mean)

df_dict = {
    "mouse_name": mouse_names,
    "baseline_mean": baseline_list,
    "response_mean": response_list,
    "ratio": ratio_list,
    "plf": plf_list
}

new_df = pd.DataFrame(df_dict)
new_df["Injection"] = INJECT
new_df.to_csv(f"tables_figures/fig_4_{INJECT}_40_ASSR_{CHANNEL}_{WEEK}.csv")
