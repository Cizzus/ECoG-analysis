import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.patches as mpatches
from power_calculation import psd_frequency_bands
from data import mice_data, mouse_names

CHANNEL = 'Aux1'
WEEK = 'week_0'
CALC = 'baseline'

ketamine_effect = mice_data[WEEK]["Ketamine"]["after_5_min"]
saline_effect = mice_data[WEEK]["Saline"]["after_5_min"]

# AUX1 DATA

frequency_ket_aux = [psd_frequency_bands(ketamine_effect[x], calc=CALC, channels=[CHANNEL], all_freq=True,
                                         mouse_name=mouse_names[x], experiment_phase='After KET') for x in
                     range(len(ketamine_effect))]
frequency_ket_df = pd.concat(frequency_ket_aux)

frequency_sal_aux = [psd_frequency_bands(saline_effect[x], calc=CALC, channels=[CHANNEL], all_freq=True,
                                         mouse_name=mouse_names[x], experiment_phase='After SAL') for x in
                     range(len(saline_effect))]
frequency_sal_df = pd.concat(frequency_sal_aux)

concat_dfs = pd.concat([frequency_ket_df, frequency_sal_df])
concat_dfs[CHANNEL] = np.log10(concat_dfs[CHANNEL])

concat_dfs.to_csv(f"tables_figures/fig_1_{CHANNEL}_{WEEK}_{CALC}_power.csv")

sns.set(rc={"figure.figsize": (17, 7)})

sns.set_theme(context="poster", style='white', palette=None, font_scale=0.8)
sns.set_theme(context="poster", style='ticks', palette=None, font_scale=0.8)

plt.axvline(x=4, color='#aea9a9')
plt.axvline(x=8, color='#aea9a9')
plt.axvline(x=12, color='#aea9a9')
plt.axvline(x=30, color='#aea9a9')
plt.axvline(x=45, color='#aea9a9')
plt.axvline(x=55, color='#aea9a9')

rect_6 = mpatches.Rectangle((45, -2.5), 10, 8,
                            fill=True,
                            color="black",
                            linewidth=2,
                            alpha=0.3, hatch='x')

plt.gca().add_patch(rect_6)

sign_size = 20
plt.text(2, 3.0, s="$\delta$", color="#000000", size=sign_size)
plt.text(1.7, 2.7, s="ns", color="#000000", size=sign_size)
plt.text(5, 3.0, s=r" $\theta$", color="#000000", size=sign_size)
plt.text(4.65, 2.6, s=r" **", color="#000000", size=sign_size + 1)
plt.text(8.5, 3.0, s=r"  $\alpha$", color="#000000", size=sign_size)
plt.text(8.6, 2.6, s=r"  *", color="#000000", size=sign_size + 1)
plt.text(20, 3.0, s=r"$\beta$", color="#000000", size=sign_size)
plt.text(19, 2.63, s=r"****", color="#000000", size=sign_size + 1)
plt.text(35, 3.0, s="Low $\gamma$", color="#000000", size=sign_size)
plt.text(36, 2.63, s=r"****", color="#000000", size=sign_size + 1)
plt.text(65, 3.0, s="High $\gamma$", color="#000000", size=sign_size)
plt.text(66, 2.63, s=r"****", color="#000000", size=sign_size + 1)
plt.text(48, 2.8, s=" AC\narea", color="black", size=sign_size)

ax = sns.lineplot(x="freq", y=CHANNEL, hue="experiment_phase", errorbar='sd',
                  data=concat_dfs, palette=("#5A96E3", "#A9A9A9"))

plt.legend(title="Experiment phase: ", fontsize=20)
ax.set_xlabel('Frequency, $Hz$', size=30)
ax.set_ylabel(r'Power, $log_{10}(\mu V^2/Hz)$', size=30)
ax.set_yticklabels([x for x in range(-3, 4, 1)], size=25)
ax.set_ylim(-2.5, 3.5)
ax.set_xlim(0.8, 90)
ax.set_xticklabels([x for x in range(0, 100, 10)], size=25)
plt.savefig(f"tables_figures/fig_1_{CHANNEL}_{WEEK}_{CALC}_power.png", dpi=1000, bbox_inches='tight')
plt.show()

################### PFC DATA ###############################

# PFC DATA
#
# frequency_ket_pfc = [psd_frequency_bands(ketamine_effect_week_0[x], calc='baseline', channels=['PFC'], all_freq=True,
#                                          mouse_name=mouse_names[x], experiment_phase='After KET (PFC)') for x in
#                      range(len(ketamine_effect_week_0))]
# frequency_ket_pfc = pd.concat(frequency_ket_pfc)
#
# frequency_sal_pfc = [psd_frequency_bands(saline_effect_week_0[x], calc='baseline', channels=['PFC'], all_freq=True,
#                                          mouse_name=mouse_names[x], experiment_phase='After SAL (PFC)') for x in
#                      range(len(saline_effect_week_0))]
# frequency_sal_df_pfc = pd.concat(frequency_sal_pfc)

# appended_dfs_pfc = frequency_ket_pfc._append(frequency_sal_df_pfc)
# appended_dfs_pfc['PFC'] = np.log10(appended_dfs_pfc['PFC'])

# sns.lineplot(x = "freq", y = "PFC", hue = "experiment_phase",errorbar = 'sd',
#                   data = appended_dfs_pfc, palette=("#F15A59", "#F15A59"), style="experiment_phase")
