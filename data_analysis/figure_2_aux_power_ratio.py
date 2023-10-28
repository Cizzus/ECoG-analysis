import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.patches as mpatches
from power_calculation import psd_frequency_bands
from data import mice_data, mouse_names

CHANNEL = 'Aux1'

# KETAMINE TIME EFFECT

ketamine_effect_week_0_after = mice_data["week_0"]["Ketamine"]["after_5_min"]
ketamine_effect_week_0_after_1_h = mice_data["week_0"]["Ketamine"]["after_1_h"]
ketamine_effect_week_0_after_4_h = mice_data["week_0"]["Ketamine"]["after_4_h"]
ketamine_effect_week_0_after_24_h = mice_data["week_0"]["Ketamine"]["after_24_h"]

frequency_ket_after = [
    psd_frequency_bands(ketamine_effect_week_0_after[x], calc='baseline', channels=[CHANNEL], all_freq=True,
                        mouse_name=mouse_names[x], experiment_phase='After 5 min KET ') for x in
    range(len(ketamine_effect_week_0_after))]
frequency_ket_after = pd.concat(frequency_ket_after)

frequency_ket_after_1_h = [
    psd_frequency_bands(ketamine_effect_week_0_after_1_h[x], calc='baseline', channels=[CHANNEL], all_freq=True,
                        mouse_name=mouse_names[x], experiment_phase='After 1 h KET ') for x in
    range(len(ketamine_effect_week_0_after_1_h))]
frequency_ket_after_1_h = pd.concat(frequency_ket_after_1_h)

frequency_ket_after_4_h = [
    psd_frequency_bands(ketamine_effect_week_0_after_4_h[x], calc='baseline', channels=[CHANNEL], all_freq=True,
                        mouse_name=mouse_names[x], experiment_phase='After 4 h KET ') for x in
    range(len(ketamine_effect_week_0_after_4_h))]
frequency_ket_after_4_h = pd.concat(frequency_ket_after_4_h)

frequency_ket_after_24_h = [
    psd_frequency_bands(ketamine_effect_week_0_after_24_h[x], calc='baseline', channels=[CHANNEL], all_freq=True,
                        mouse_name=mouse_names[x], experiment_phase='After 24 h KET ') for x in
    range(len(ketamine_effect_week_0_after_24_h))]
frequency_ket_after_24_h = pd.concat(frequency_ket_after_24_h)

# SALINE TIME EFFECT

saline_effect_week_0_after = mice_data["week_0"]["Saline"]["after_5_min"]
saline_effect_week_0_after_1_h = mice_data["week_0"]["Saline"]["after_1_h"]
saline_effect_week_0_after_4_h = mice_data["week_0"]["Saline"]["after_4_h"]
saline_effect_week_0_after_24_h = mice_data["week_0"]["Saline"]["after_24_h"]

frequency_sal_after = [
    psd_frequency_bands(saline_effect_week_0_after[x], calc='baseline', channels=[CHANNEL], all_freq=True,
                        mouse_name=mouse_names[x], experiment_phase='After 5 min SAL') for x in
    range(len(saline_effect_week_0_after))]

frequency_sal_after = pd.concat(frequency_sal_after)

frequency_sal_after_1_h = [
    psd_frequency_bands(saline_effect_week_0_after_1_h[x], calc='baseline', channels=[CHANNEL], all_freq=True,
                        mouse_name=mouse_names[x], experiment_phase='After 1 h SAL') for x in
    range(len(saline_effect_week_0_after_1_h))]

frequency_sal_after_1_h = pd.concat(frequency_sal_after_1_h)

frequency_sal_after_4_h = [
    psd_frequency_bands(saline_effect_week_0_after_4_h[x], calc='baseline', channels=[CHANNEL], all_freq=True,
                        mouse_name=mouse_names[x], experiment_phase='After 4 h SAL') for x in
    range(len(saline_effect_week_0_after_4_h))]

frequency_sal_after_4_h = pd.concat(frequency_sal_after_4_h)

frequency_sal_after_24_h = [
    psd_frequency_bands(saline_effect_week_0_after_24_h[x], calc='baseline', channels=[CHANNEL], all_freq=True,
                        mouse_name=mouse_names[x], experiment_phase='After 24 h SAL') for x in
    range(len(saline_effect_week_0_after_24_h))]

frequency_sal_after_24_h = pd.concat(frequency_sal_after_24_h)

# Ratio calculations

frequency_ket_after[CHANNEL] = frequency_ket_after[CHANNEL] / frequency_sal_after[CHANNEL]
frequency_ket_after_1_h[CHANNEL] = frequency_ket_after_1_h[CHANNEL] / frequency_sal_after_1_h[CHANNEL]
frequency_ket_after_4_h[CHANNEL] = frequency_ket_after_4_h[CHANNEL] / frequency_sal_after_4_h[CHANNEL]
frequency_ket_after_24_h[CHANNEL] = frequency_ket_after_24_h[CHANNEL] / frequency_sal_after_24_h[CHANNEL]

frequency_ket_after.to_csv(f'tables_figures/{CHANNEL}_ratio_5_min_after.csv')
frequency_ket_after_1_h.to_csv(f'tables_figures/{CHANNEL}_ratio_after_1_h.csv')
frequency_ket_after_4_h.to_csv(f'tables_figures/{CHANNEL}_ratio_after_4_h.csv')
frequency_ket_after_24_h.to_csv(f'tables_figures/{CHANNEL}_ratio_after_24_h.csv')

sns.set(rc={"figure.figsize": (20, 9)})
sns.set_theme(context="poster", style='white', palette=None, font_scale=0.8)
sns.set_theme(context="poster", style='ticks', palette=None, font_scale=0.8)

rect_6 = mpatches.Rectangle((45, -2.5), 10, 8,
                            fill=True,
                            color="black",
                            linewidth=2,
                            alpha=0.3, hatch='x')

plt.gca().add_patch(rect_6)

sign_size = 20
plt.text(2, 4.2, s="$\delta$", color="#000000", size=sign_size)
plt.text(5, 4.2, s=r" $\theta$", color="#000000", size=sign_size)
plt.text(8.5, 4.2, s=r"  $\alpha$", color="#000000", size=sign_size)
plt.text(20, 4.2, s=r"$\beta$", color="#000000", size=sign_size)
plt.text(35, 4.2, s="Low $\gamma$", color="#000000", size=sign_size)
plt.text(65, 4.2, s="High $\gamma$", color="#000000", size=sign_size)
plt.text(48, 4.0, s=" AC\narea", color="black", size=sign_size)

sns.set_theme(context="poster", style='white', font_scale=0.8)
sns.set_theme(context="poster", style='ticks', font_scale=0.8)
plt.axvline(x=4, color='#aea9a9')
plt.axvline(x=8, color='#aea9a9')
plt.axvline(x=12, color='#aea9a9')
plt.axvline(x=30, color='#aea9a9')
plt.axvline(x=45, color='#aea9a9')
plt.axvline(x=55, color='#aea9a9')

ax = sns.lineplot(x="freq", y=CHANNEL, hue="experiment_phase", errorbar='sd',
                  data=frequency_ket_after, palette=("#5A96E3", "#00C4FF"))

sns.lineplot(x="freq", y=CHANNEL, hue="experiment_phase", errorbar='sd',
             data=frequency_ket_after_1_h, palette=("#19A7CE", "#5A96E3"))  # For AUX #19A7CE

sns.lineplot(x="freq", y=CHANNEL, hue="experiment_phase", errorbar='sd',
             data=frequency_ket_after_4_h, palette=("#AFD3E2", "#00C4FF"))  # For AUX #AFD3E2
sns.lineplot(x="freq", y=CHANNEL, hue="experiment_phase", errorbar='sd',
             data=frequency_ket_after_24_h, palette=("#F6F1F1", "#577D86"))  # For AUX #F6F1F1

ax.set_xlabel('Frequency, $Hz$', size=30)
ax.set_ylabel(r'Power Ratio, $\frac{Ketamine}{Saline}$', size=30)
ax.set_ylim(0, 4.5)
ax.set_xlim(0.8, 90)
ax.set_yticklabels(ax.get_yticks(), size=25)
ax.set_xticklabels([x for x in range(0, 100, 10)], size=25)
plt.axhline(y=1, color="#030303", ls="dashed", label='Baseline', alpha=0.5)
plt.legend(title="Time effect: ", fontsize=20)
plt.savefig(f"tables_figures/figure_2_{CHANNEL}_power_ratio.png", dpi=1000, bbox_inches='tight')
plt.show()
