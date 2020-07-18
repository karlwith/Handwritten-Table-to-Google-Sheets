Overview:
This python script includes methods to request and receive an OCR response using the google vision api, parse the data 
into lists which are then uploaded using the google sheets api. Sample input and local variable output is included in Images.

The design motivation for this script is to save time transposing written tabular data of bikes built, the date, the 
builder and each respective serial number into a digital form as is required for company records. Typically 15 to 20 lines of 
data need to be typed into google sheets per day.

The formatting method included to parse the single string response of the google vision api assumes the written data 
conforms to the style including semi colons and plus characters as detailed in Images/BuildBook01.jpg. A future improvement 
could include creating a printable template to increase the reliability of the OCR formatting and streamline handwriting.

To Do:
Finish upload_to_google_sheet method.
Host on as a web app on google cloud / app engine to facilitate the use of mobile phone to take the picture and run the program.