*Replace with directory containing the datasets
cd C:\Users\Balazs_Tibor\Desktop\Coding_For_Economists_2024_Assignment\Coding_For_Economists_2024_Assignment

*Importing and saving datasets to different dataframes

frame create cpi
frame change cpi

import delimited using "C:\Users\Balazs_Tibor\Desktop\Coding_For_Economists_2024_Assignment\Coding_For_Economists_2024_Assignment\CPIAUCSL.csv"

save "C:\Users\Balazs_Tibor\Desktop\Coding_For_Economists_2024_Assignment\Coding_For_Economists_2024_Assignment\CPIAUCSL.dta", replace

frame create unemp
frame change unemp

import delimited using "C:\Users\Balazs_Tibor\Desktop\Coding_For_Economists_2024_Assignment\Coding_For_Economists_2024_Assignment\UNRATE.csv"

save "C:\Users\Balazs_Tibor\Desktop\Coding_For_Economists_2024_Assignment\Coding_For_Economists_2024_Assignment\UNEMP.dta", replace

frame change default

