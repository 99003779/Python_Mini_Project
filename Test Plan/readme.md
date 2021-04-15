##Test Plans

Test_ID|	Description|	Expected Input|	Expected Output|Actual Output|
-------|-------------|----------------|----------------|---------------|
TP_01|	User enters the registration number, name and Email ID of the person being searched|	99673798
Ali Adibi
Ali.adibi@ece.gatech.edu|The data corresponding to the given input will be searched in all the sub-sheets and printed to mastersheet.|The data is printed to mastersheet and summary count has been incremented.|
TP_02| User enters the registration number, name and Email ID of the person being searched. Now it takes multiple input of data by selecting Yes/No in the terminal window.|99673798
Ali Adibi
Ali.adibi@ece.gatech.edu

Continue (y/n) ? y

99673786
Professor Peter Y. K. Cheung
p.cheung@imperial.ac.uk|The data corresponding to the given multiple inputs will be searched in all the sub-sheets and printed to mastersheet.|	The data is printed to mastersheet and summary count has been incremented.|
TP_03|	User enters the registration number, name and Email ID of the person being searched. Now it takes multiple input of data by selecting Yes/No in the terminal window. Now user select no for further data intake.|99673798
Ali Adibi
Ali.adibi@ece.gatech.edu

Continue (y/n) ? y

99673786
Professor Peter Y. K. Cheung
p.cheung@imperial.ac.uk

Continue (y/n) ? n|The data corresponding to the given multiple inputs will be searched in all the sub-sheets and printed to mastersheet.
 
Data has been printed to Mastersheet|The data is printed to mastersheet and summary count has been incremented.|

