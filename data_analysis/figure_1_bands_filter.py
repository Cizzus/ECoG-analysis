import pandas as pd
from power_calculation import table_of_frequency_bands, psd_calc, filter_table
from data import mice_data, mouse_names

AREA = 'Aux1'
CALC = "baseline"
WEEK = 'week_0'

ketamine_effect_week_0 = mice_data[WEEK]["Ketamine"]["after_5_min"]
saline_effect_week_0 = mice_data[WEEK]["Saline"]["after_5_min"]

frequency_ket = psd_calc(ketamine_effect_week_0, calc=CALC, channels=['Aux1', 'PFC'])
frequency_sal = psd_calc(saline_effect_week_0, calc=CALC, channels=['Aux1', 'PFC'])

table_ketamine = table_of_frequency_bands(ketamine_effect_week_0, channels=['Aux1', 'PFC'], mice_names=mouse_names,
                                          experiment_phase="after_5_min_ket", calc=CALC, freq_40=False)
table_saline = table_of_frequency_bands(saline_effect_week_0, channels=['Aux1', 'PFC'], mice_names=mouse_names,
                                        experiment_phase="after_5_min_sal", calc=CALC, freq_40=False)

delta_ketamine = filter_table(table_ketamine, 'delta', AREA)
theta_ketamine = filter_table(table_ketamine, 'theta', AREA)
alpha_ketamine = filter_table(table_ketamine, 'alpha', AREA)
beta_ketamine = filter_table(table_ketamine, 'beta', AREA)
low_gamma_ketamine = filter_table(table_ketamine, 'low gamma', AREA)
high_gamma_ketamine = filter_table(table_ketamine, 'high gamma', AREA)

delta_saline = filter_table(table_saline, 'delta', AREA)
theta_saline = filter_table(table_saline, 'theta', AREA)
alpha_saline = filter_table(table_saline, 'alpha', AREA)
beta_saline = filter_table(table_saline, 'beta', AREA)
low_gamma_saline = filter_table(table_saline, 'low gamma', AREA)
high_gamma_saline = filter_table(table_saline, 'high gamma', AREA)

delta = pd.concat([delta_saline, delta_ketamine])
theta = pd.concat([theta_saline, theta_ketamine])
alpha = pd.concat([alpha_saline, alpha_ketamine])
beta = pd.concat([beta_saline, beta_ketamine])
low_gamma = pd.concat([low_gamma_saline, low_gamma_ketamine])
high_gamma = pd.concat([high_gamma_saline, high_gamma_ketamine])

delta.to_csv(f"tables_figures/fig_1_delta_{AREA}_{WEEK}_{CALC}_power.csv")
theta.to_csv(f"tables_figures/fig_1_theta_{AREA}_{WEEK}_{CALC}_power.csv")
alpha.to_csv(f"tables_figures/fig_1_alpha_{AREA}_{WEEK}_{CALC}_power.csv")
beta.to_csv(f"tables_figures/fig_1_beta_{AREA}_{WEEK}_{CALC}_power.csv")
low_gamma.to_csv(f"tables_figures/fig_1_low_gamma_{AREA}_{WEEK}_{CALC}_power.csv")
high_gamma.to_csv(f"tables_figures/fig_1_high_gamma_{AREA}_{WEEK}_{CALC}_power.csv")
