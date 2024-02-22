* Change directory
cd "Code\coding_for_economists\"

* Download data
do "0_import_data.do"

* Clean data
do "1_filtering_transforming_data.do"

* Run (simple) analysis
do "2_regression_analysis.do"

* Plot graph
do "3_graph.do"