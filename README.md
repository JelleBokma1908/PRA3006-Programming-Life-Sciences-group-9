# Instructions setting Project up
## Converting .csv into .ttl file

* The excel file [TPM_human_and_mouse_dataset_excel.csv](TPM_human_and_mouse_dataset_excel.csv) contains the data required for this project
* For convenience, all spaces have been removed in the 'Brain region' column
* Running the [csv_ttl_converter.py](csv_ttl_converter.py) file on this csv will create the attached [TPM_human_and_mouse_dataset_turtle.ttl](TPM_human_and_mouse_dataset_turtle.ttl) file.

## Setting up Blazegraph 

* In a command prompt, set the directory to the one the bigdata.jar (https://github.com/blazegraph/database/releases/download/BLAZEGRAPH_2_1_6_RC/bigdata.jar) file is located in
* Run the following command: java -jar bigdata.jar
* Go to localhost:9999 ; (http://localhost:9999)
* Under the 'Update' tab, browse for the [TPM_human_and_mouse_dataset_turtle.ttl](TPM_human_and_mouse_dataset_turtle.ttl) file, and upload

## Disabling chrome security

* Run a separate command prompt as administrator
* Run the following command, replacing YOUR_USERNAME with your device username:  

"C:\Program Files\Google\Chrome\Application\chrome.exe" --disable-web-security --user-data-dir=C:\User\YOUR_USERNAME  

* This should open a new chrome application, in which the html page can be loaded

## Running HTML code

* The final product is named Gene_and_Neurotransmitter_Viewer_htmlcode.html [Gene_and_Neurotransmitter_Viewer_htmlcode.html]
  (Gene_and_Neurotransmitter_Viewer_htmlcode.html)
* Upon running, make sure it is set up on a different port as the Blazegraph is, eg 5500
* It can only work successfully in the Chrome tab where security is disabled. In browsers without the cross-origin request will be blocked. 
