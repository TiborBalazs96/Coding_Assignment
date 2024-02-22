*Replace with directory containing the datasets
cd C:\Users\Balazs_Tibor\Desktop\Coding_For_Economists_2024_Assignment\Coding_For_Economists_2024_Assignment

use cleaned

gen date_variable = date(date, "YMD")

*Filtering and transforming the variables
keep if unrate > 5
*Creating the inflation rate from the CPI

gen ln_cpi = ln(cpiaucsl)

save "C:\Users\Balazs_Tibor\Desktop\Coding_For_Economists_2024_Assignment\Coding_For_Economists_2024_Assignment\filtered_transformed.dta", replace