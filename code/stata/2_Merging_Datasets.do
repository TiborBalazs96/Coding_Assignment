*Replace with directory containing the datasets
cd C:\Users\Balazs_Tibor\Desktop\Coding_For_Economists_2024_Assignment\Coding_For_Economists_2024_Assignment

use CPIAUCSL

merge 1:1 date using UNEMP, nogenerate

save "C:\Users\Balazs_Tibor\Desktop\Coding_For_Economists_2024_Assignment\Coding_For_Economists_2024_Assignment\merged.dta", replace
