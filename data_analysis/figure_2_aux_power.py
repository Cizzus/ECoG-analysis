import pandas as pd
from power_calculation import table_of_frequency_bands, filter_table
from data import mice_data, mouse_names

CALC = 'baseline'
WEEK = 'week_0'

# KETAMINE DATA

ketamine_effect_week_0_after = mice_data[WEEK]["Ketamine"]["after_5_min"]
ketamine_effect_week_0_after_1_h = mice_data[WEEK]["Ketamine"]["after_1_h"]
ketamine_effect_week_0_after_4_h = mice_data[WEEK]["Ketamine"]["after_4_h"]
ketamine_effect_week_0_after_24_h = mice_data[WEEK]["Ketamine"]["after_24_h"]

# SALINE DATA

saline_effect_week_0_after = mice_data[WEEK]["Saline"]["after_5_min"]
saline_effect_week_0_after_1_h = mice_data[WEEK]["Saline"]["after_1_h"]
saline_effect_week_0_after_4_h = mice_data[WEEK]["Saline"]["after_4_h"]
saline_effect_week_0_after_24_h = mice_data[WEEK]["Saline"]["after_24_h"]

# KETAMINE EFFECT ON FREQUENCY BANDS

table_ketamine_after = table_of_frequency_bands(ketamine_effect_week_0_after, channels=['Aux1', 'PFC'],
                                                mice_names=mouse_names, experiment_phase="after_5_min_ket",
                                                calc=CALC, freq_40=False)

table_ketamine_after_1_h = table_of_frequency_bands(ketamine_effect_week_0_after_1_h, channels=['Aux1', 'PFC'],
                                                    mice_names=mouse_names, experiment_phase="after_1_h_ket",
                                                    calc=CALC, freq_40=False)

table_ketamine_after_4_h = table_of_frequency_bands(ketamine_effect_week_0_after_4_h, channels=['Aux1', 'PFC'],
                                                    mice_names=mouse_names, experiment_phase="after_4_h_ket",
                                                    calc=CALC, freq_40=False)

table_ketamine_after_24_h = table_of_frequency_bands(ketamine_effect_week_0_after_24_h, channels=['Aux1', 'PFC'],
                                                     mice_names=mouse_names, experiment_phase="after_24_h_ket",
                                                     calc=CALC, freq_40=False)

# SALINE EFFECT ON FREQUENCY BANDS

table_saline_after = table_of_frequency_bands(saline_effect_week_0_after, channels=['Aux1', 'PFC'],
                                              mice_names=mouse_names, experiment_phase="after_5_min_sal",
                                              calc=CALC, freq_40=False)

table_saline_after_1_h = table_of_frequency_bands(saline_effect_week_0_after_1_h, channels=['Aux1', 'PFC'],
                                                  mice_names=mouse_names, experiment_phase="after_1_h_sal",
                                                  calc=CALC, freq_40=False)

table_saline_after_4_h = table_of_frequency_bands(saline_effect_week_0_after_4_h, channels=['Aux1', 'PFC'],
                                                  mice_names=mouse_names, experiment_phase="after_4_h_sal",
                                                  calc=CALC, freq_40=False)

table_saline_after_24_h = table_of_frequency_bands(saline_effect_week_0_after_24_h, channels=['Aux1', 'PFC'],
                                                   mice_names=mouse_names, experiment_phase="after_24_h_sal",
                                                   calc=CALC, freq_40=False)

# CREATING FILES WHERE EFFECT IS ON PARTICULAR FREQUENCY BAND

BAND = "high gamma"
AREA = 'Aux1'

ket_after = filter_table(table_ketamine_after, band=BAND, brain_area=AREA)
sal_after = filter_table(table_saline_after, band=BAND, brain_area=AREA)

ket_after_1_h = filter_table(table_ketamine_after_1_h, band=BAND, brain_area=AREA)
sal_after_1_h = filter_table(table_saline_after_1_h, band=BAND, brain_area=AREA)

ket_after_4_h = filter_table(table_ketamine_after_4_h, band=BAND, brain_area=AREA)
sal_after_4_h = filter_table(table_saline_after_4_h, band=BAND, brain_area=AREA)

ket_after_24_h = filter_table(table_ketamine_after_24_h, band=BAND, brain_area=AREA)
sal_after_24_h = filter_table(table_saline_after_24_h, band=BAND, brain_area=AREA)

ket_after = pd.concat([sal_after, ket_after])
ket_after_1_h = pd.concat([sal_after_1_h, ket_after_1_h])
ket_after_4_h = pd.concat([sal_after_4_h, ket_after_4_h])
ket_after_24_h = pd.concat([sal_after_24_h, ket_after_24_h])

ket_after.to_csv(f"tables_figures/fig_2_{BAND}_after_5_min_{AREA}_{WEEK}_{CALC}_power.csv")
ket_after_1_h.to_csv(f"tables_figures/fig_2_{BAND}_after_1_h_{AREA}_{WEEK}_{CALC}_power.csv")
ket_after_4_h.to_csv(f"tables_figures/fig_2_{BAND}_after_4_h_{AREA}_{WEEK}_{CALC}_power.csv")
ket_after_24_h.to_csv(f"tables_figures/fig_2_{BAND}_after_24_h_{AREA}_{WEEK}_{CALC}_power.csv")
