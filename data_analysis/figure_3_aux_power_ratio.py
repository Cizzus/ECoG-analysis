import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.patches as mpatches
from power_calculation import psd_frequency_bands
from data import mice_data, mouse_names

CHANNEL = 'Aux1'

ketamine_effect_week_0_after = mice_data["week_0"]["Ketamine"]["after_5_min"]
ketamine_effect_week_2_after = mice_data["week_2"]["Ketamine"]["after_5_min"]

saline_effect_week_0_after = mice_data["week_0"]["Saline"]["after_5_min"]
saline_effect_week_2_after = mice_data["week_2"]["Saline"]["after_5_min"]

# Aux1 DATA Ketamine

table_ketamine_week_0 = [psd_frequency_bands(ketamine_effect_week_0_after[x], calc='baseline', channels=[CHANNEL],
                                             all_freq=True, mouse_name=mouse_names[x],
                                             experiment_phase='After KET (Acute)') for x in
                         range(len(ketamine_effect_week_0_after))]
table_ketamine_week_0 = pd.concat(table_ketamine_week_0)

table_ketamine_week_2 = [psd_frequency_bands(ketamine_effect_week_2_after[x], calc='baseline', channels=[CHANNEL],
                                             all_freq=True, mouse_name=mouse_names[x],
                                             experiment_phase='After KET (Chronic)') for x in
                         range(len(ketamine_effect_week_2_after))]
table_ketamine_week_2 = pd.concat(table_ketamine_week_2)

# Aux1 DATA Saline

table_saline_week_0 = [psd_frequency_bands(saline_effect_week_0_after[x], calc='baseline', channels=[CHANNEL],
                                           all_freq=True, mouse_name=mouse_names[x],
                                           experiment_phase='After SAL (Week 0)') for x in
                       range(len(saline_effect_week_0_after))]
table_saline_week_0 = pd.concat(table_saline_week_0)

table_saline_week_2 = [psd_frequency_bands(saline_effect_week_2_after[x], calc='baseline', channels=[CHANNEL],
                                           all_freq=True, mouse_name=mouse_names[x],
                                           experiment_phase='After SAL (Week 2)') for x in
                       range(len(saline_effect_week_2_after))]
table_saline_week_2 = pd.concat(table_saline_week_2)

# CALCULATE RATIO
table_ketamine_week_0[CHANNEL] = table_ketamine_week_0[CHANNEL] / table_saline_week_0[CHANNEL]
table_ketamine_week_2[CHANNEL] = table_ketamine_week_2[CHANNEL] / table_saline_week_2[CHANNEL]

table_ketamine_week_0.to_csv(f"tables_figures/fig_3_{CHANNEL}_acute_ket_effect.csv")
table_ketamine_week_2.to_csv(f"tables_figures/fig_3_{CHANNEL}_chronic_ket_effect.csv")

# FIGURE AESTHETICS

sns.set(rc={"figure.figsize": (17, 7)})
sns.set_theme(context="poster", style='white', font_scale=1.4)
sns.set_theme(context="poster", style='ticks', font_scale=1.4)

rect_6 = mpatches.Rectangle((45, -2.5), 10, 8,
                            fill=True,
                            color="black",
                            linewidth=2,
                            alpha=0.3, hatch='x')

plt.gca().add_patch(rect_6)

sign_size = 20
plt.text(2, 5, s="$\delta$", color="#000000", size=sign_size)
plt.text(1.5, 4.7, s="ns", color="#000000", size=sign_size)
plt.text(5, 5, s=r" $\theta$", color="#000000", size=sign_size)
plt.text(5, 4.7, s="ns", color="#000000", size=sign_size)
plt.text(8.5, 5, s=r"  $\alpha$", color="#000000", size=sign_size)
plt.text(8.9, 4.7, s="ns", color="#000000", size=sign_size)
plt.text(20, 5, s=r"$\beta$", color="#000000", size=sign_size)
plt.text(19.5, 4.7, s="ns", color="#000000", size=sign_size)
plt.text(35, 5, s="Low $\gamma$", color="#000000", size=sign_size)
plt.text(37, 4.7, s="ns", color="#000000", size=sign_size)
plt.text(60, 5, s="High $\gamma$", color="#000000", size=sign_size)
plt.text(62, 4.7, s="ns", color="#000000", size=sign_size)
plt.text(48, 4.8, s=" AC\narea", color="black", size=sign_size)

plt.axvline(x=4, color='#aea9a9')
plt.axvline(x=8, color='#aea9a9')
plt.axvline(x=12, color='#aea9a9')
plt.axvline(x=30, color='#aea9a9')
plt.axvline(x=45, color='#aea9a9')
plt.axvline(x=55, color='#aea9a9')

ax = sns.lineplot(x="freq", y=CHANNEL, hue="experiment_phase", errorbar='sd',
                  data=table_ketamine_week_0,
                  palette=("#5A96E3", "#119A7CE"))  # For AUX ("#5A96E3", "#119A7CE", "#AFD3E2", "#F6F1F1")

sns.lineplot(x="freq", y=CHANNEL, hue="experiment_phase", errorbar='sd',
             data=table_ketamine_week_2, palette=("#AFD3E2", "#AFD3E2"))  # For AUX ("#F6F1F1", "#AFD3E2")
ax.set_xlabel('Frequency, $Hz$', size=30)
ax.set_ylabel(r'Power Ratio, $\frac{Ketamine}{Saline}$', size=30)
ax.set_ylim(-0.5, 5.5)
ax.set_xlim(0.8, 90)
# plt.axhline(y=1, color="#030303", ls="dashed", label='Baseline', alpha=0.5)
plt.legend(title="Time effect: ", fontsize=15)
plt.savefig(f"tables_figures/fig_3_{CHANNEL}.png", dpi=1000, bbox_inches='tight')
plt.show()
