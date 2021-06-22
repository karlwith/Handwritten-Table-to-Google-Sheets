# Google API Framework:

This python script includes methods to request and receive an OCR response using the Google Vision API, parse the data into lists which are then uploaded to the next available row using the Google Sheets API. Example input, local variable output and google sheet output is included in \Images.

The design motivation for this script is to save time transposing written tabular data (in this example being bikes built, date, the builder and each respective serial number) into a digital form as is required for databases. In the context of this example typically 15 to 20 lines of data need to be typed into Google Sheets per day.

The formatting method included to parse the single string response of the Google Vision API assumes the written data conforms to the style including semi colons and plus characters as detailed in Images/datatable.jpg. A future improvement could include creating a printable template to increase the reliability of the OCR formatting and streamline handwriting.

## Example input:
![datatable](https://user-images.githubusercontent.com/65951397/122892701-f5ee9a00-d388-11eb-8b7d-e25aa330405f.jpg)

## Example output:
![sheetoutput](https://user-images.githubusercontent.com/65951397/122892742-00a92f00-d389-11eb-9596-2ad2361ad4fc.jpg)


## To Do:
Host as a web app on Google Cloud / app engine to facilitate the use of mobile phone to take the picture and run the program.
