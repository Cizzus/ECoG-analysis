import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.patches as mpatches
from power_calculation import psd_frequency_bands
from data import mice_data, mouse_names

CHANNEL = 'Aux1'
WEEK = 'week_0'
CALC = 'baseline'

ketamine_effect_week_0 = mice_data[WEEK]["Ketamine"]["after_5_min"]
saline_effect_week_0 = mice_data[WEEK]["Saline"]["after_5_min"]

# AUX DATA

frequency_ket_aux = [psd_frequency_bands(ketamine_effect_week_0[x], calc=CALC, channels=[CHANNEL], all_freq=True,
                                         mouse_name=mouse_names[x], experiment_phase='After KET') for x in
                     range(len(ketamine_effect_week_0))]
frequency_ket_df = pd.concat(frequency_ket_aux)

frequency_sal_aux = [psd_frequency_bands(saline_effect_week_0[x], calc=CALC, channels=[CHANNEL], all_freq=True,
                                         mouse_name=mouse_names[x], experiment_phase='After SAL') for x in
                     range(len(saline_effect_week_0))]
frequency_sal_df = pd.concat(frequency_sal_aux)

frequency_ket_df[CHANNEL] = frequency_ket_df[CHANNEL] / frequency_sal_df[CHANNEL]  # Calculate ratio

frequency_ket_df.to_csv(f"tables_figures/fig_1_{CHANNEL}_{WEEK}_{CALC}_power_ratio.csv")

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
plt.text(2, 4.2, s="$\delta$", color="#000000", size=sign_size)
plt.text(1.7, 4.0, s="ns", color="#000000", size=sign_size)
plt.text(5, 4.2, s=r" $\theta$", color="#000000", size=sign_size)
plt.text(4.65, 3.9, s=r" **", color="#000000", size=sign_size + 1)
plt.text(8.5, 4.2, s=r"  $\alpha$", color="#000000", size=sign_size)
plt.text(8.6, 3.9, s=r"  *", color="#000000", size=sign_size + 1)
plt.text(20, 4.2, s=r"$\beta$", color="#000000", size=sign_size)
plt.text(19, 3.9, s=r"****", color="#000000", size=sign_size + 1)
plt.text(35, 4.2, s="Low $\gamma$", color="#000000", size=sign_size)
plt.text(36, 3.9, s=r"****", color="#000000", size=sign_size + 1)
plt.text(65, 4.2, s="High $\gamma$", color="#000000", size=sign_size)
plt.text(66, 3.9, s=r"****", color="#000000", size=sign_size + 1)
plt.text(48, 4.0, s=" AC\narea", color="black", size=sign_size)

ax = sns.lineplot(x="freq", y=CHANNEL, hue="experiment_phase", errorbar='sd',
                  data=frequency_ket_df, palette=("#5A96E3", "#F15A59"))

plt.axhline(y=1, color="#030303", ls="dashed", label='Baseline', alpha=0.5)
plt.legend(title="Experiment phase: ", fontsize=20)
ax.set_xlabel('Frequency, $Hz$', size=30)
ax.set_ylabel(r'Power Ratio, $\frac{Ketamine}{Saline}$', size=30)
ax.set_ylim(0, 4.5)
ax.set_xlim(0.8, 90)
ax.set_yticklabels(ax.get_yticks(), size=25)
ax.set_xticklabels([x for x in range(0, 100, 10)], size=25)
plt.savefig(f"tables_figures/fig_1_{CHANNEL}_{WEEK}_{CALC}_power_ratio.png", dpi=1000, bbox_inches='tight')
plt.show()

# PFC DATA

# frequency_ket_pfc = [psd_frequency_bands(ketamine_effect_week_0[x], calc='baseline', channels=['PFC'], all_freq=True,
#                                          mouse_name=mouse_names[x], experiment_phase='After KET (PFC)') for x in
#                      range(len(ketamine_effect_week_0))]
# frequency_ket_pfc = pd.concat(frequency_ket_pfc)
#
# frequency_sal_pfc = [psd_frequency_bands(saline_effect_week_0[x], calc='baseline', channels=['PFC'], all_freq=True,
#                                          mouse_name=mouse_names[x], experiment_phase='After SAL (PFC)') for x in
#                      range(len(saline_effect_week_0))]
# frequency_sal_df_pfc = pd.concat(frequency_sal_pfc)
#
# frequency_ket_pfc['PFC'] = frequency_ket_pfc['PFC']/frequency_sal_df_pfc['PFC']
#
# frequency_ket_pfc.to_csv("figure_1_b_pfc_data.csv")

# plt.figure(figsize=(12, 6))
# plt.axvline(x=4, color='#aea9a9')
# plt.axvline(x=8, color='#aea9a9')
# plt.axvline(x=12, color='#aea9a9')
# plt.axvline(x=30, color='#aea9a9')
# plt.axvline(x=45, color='#aea9a9')
# plt.axvline(x=55, color='#aea9a9')

# sns.lineplot(x="freq", y="PFC", hue="experiment_phase", errorbar='sd',
#              data=frequency_ket_pfc, palette=("#F15A59", "#F15A59"), style="experiment_phase")

# plt.plot(frequency.index, frequency['Aux1']/frequency_sal['Aux1'], label='Ketamine (Aux1)', c="#030303")
#
#
# plt.plot(frequency.index, frequency['PFC']/frequency_sal['PFC'], label='Ketamine (PFC)', c='#817d7d')
#
# plt.axhline(y=1, color="#030303", ls="dashed", label='Baseline')
# plt.xlabel("Time, $s$", size=15)
# plt.ylabel(r"Ratio, $\frac{Power_{Ketamine}}{Power_{Saline}}$", size=18)
# plt.xlim(1, 100)
# plt.legend()
# plt.savefig("figure_1B.png", dpi=400)
# plt.show()
