import matplotlib.pyplot as plt
import numpy as np
from power_calculation import calc_itpc_power, import_ecog
from data import mice_data

CHANNEL = 'Aux1'
WEEK = 'week_0'
INJECT = "Ketamine"

ecog_record = mice_data[WEEK][INJECT]["after_1_h"]

power_aux, itc_aux = calc_itpc_power(import_ecog(ecog_record[0]).pick_channels([CHANNEL]))

for num in range(1, len(ecog_record)):
    power_num_aux, itc_num_aux = calc_itpc_power(import_ecog(ecog_record[num]).pick_channels([CHANNEL]))
    power_aux += power_num_aux

average_aux = power_aux / 17

# for num in range(1, len(ecog_record)):
#     power_num_aux, itc_num_aux = calc_itpc_power(import_ecog(ecog_record[num]).pick_channels([CHANNEL]))
#     itc_aux += itc_num_aux
#
# average_aux = itc_aux / 17



average_pow = average_aux.data
average_pow = np.log10(average_pow[0][0:51]) * 10
baseline = average_pow[:, 400:1800].mean(axis=1)
average_pow = average_pow.transpose()
normal_pow = np.array([signal - baseline for signal in average_pow]).transpose()
time = np.linspace(0, 3, 6000)
freq = np.linspace(20, 70, 51)

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.style.use('seaborn-v0_8-paper')

im = plt.pcolormesh(
    time,
    freq,
    normal_pow,
    shading='auto',
    cmap='Blues',
    vmax=10.5
)
cbar = plt.colorbar()
im.figure.axes[1].tick_params(axis='y', labelsize=12)
cbar.set_label(label="Power, $dB$", size=15)

plt.xlabel("Time, $s$", size=15)
plt.xticks(size=12)
plt.ylabel("Frequency, $Hz$", size=15)
plt.yticks(size=12)
plt.title(f"{CHANNEL} 40 Hz ASSR", size=20)

plt.savefig(f"fig_4_{CHANNEL}_{INJECT}_{WEEK}.png", dpi=600, bbox_inches='tight')
plt.show()
