Overview:
This python script includes methods to request and receive an OCR response using the google vision api, parse the data 
into lists which are then uploaded to the next available row using the google sheets api. Example input, local variable output and google sheet output is included in Images.

The design motivation for this script is to save time transposing written tabular data (in this example being bikes built, date, the 
builder and each respective serial number) into a digital form as is required for databases. In the context of this example typically 15 to 20 lines of 
data need to be typed into google sheets per day.

The formatting method included to parse the single string response of the google vision api assumes the written data 
conforms to the style including semi colons and plus characters as detailed in Images/datatable.jpg. A future improvement 
could include creating a printable template to increase the reliability of the OCR formatting and streamline handwriting.

To Do:
Host on as a web app on google cloud / app engine to facilitate the use of mobile phone to take the picture and run the program.