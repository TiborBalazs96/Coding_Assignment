*Replace with directory containing the datasets
cd C:\Users\Balazs_Tibor\Desktop\Coding_For_Economists_2024_Assignment\Coding_For_Economists_2024_Assignment

use merged

drop if missing(cpiaucsl) | missing(unrate)

save "C:\Users\Balazs_Tibor\Desktop\Coding_For_Economists_2024_Assignment\Coding_For_Economists_2024_Assignment\cleaned.dta", replace