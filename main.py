import os, io, string, gspread
from google.cloud import vision
from oauth2client.service_account import ServiceAccountCredentials


# IMAGE PRE-PROCESSING shouldn't be needed with google vision but otherwise (scale to usable DPI, skew correction, adjust threshold to binarize, remove noise)

def image_to_text_lists():

    # Define google vision api credentials
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'VisionAPIKey.json'
    client = vision.ImageAnnotatorClient()

    # Define the image
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, r'Images\datatable.jpg')
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    # Send the request and receive the response
    input = vision.types.Image(content = content)
    response = client.document_text_detection(image = input)
    return response

def format_for_google_sheet():

    # List recognised word blocks and ascociated confidence
    pages = response.full_text_annotation.pages
    for page in pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    print ('Character Block: {0} (confidence: {1})'.format(word_text, word.confidence))

    # Write output variable to text file
    textOutput = response.full_text_annotation.text
    textFile = open('output.txt', 'w')
    textFile.write(textOutput)
    textFile.close()

    # Remove line breaks and double spacing
    with open('output.txt', 'r') as f:
        text = f.read()
        split = text.split()
        joinedString = " ".join(split)

    # Break into separate lists of date, bikes, serials 
    joinedList = joinedString.split(':')
    date = joinedList[0]
    bikes = joinedList[1]    
    serials = joinedList[2]

    # Parse bike lines
    bikes = bikes.replace('R ', '\nReid ')
    bikes = bikes.replace('M ', '\nMerida ')
    bikes = bikes.replace('N ', '\nNorco ')
    bikes = bikes.strip()
    bikes = bikes.split('\n')
    
    # Parse serial lines
    serials = serials.replace(" ", "")
    serials = serials.split('+')
    
    # Assign date and builder for each line
    date = date.strip()
    dates = [date] * len(bikes)
    builder = 'Karl'
    builder = [builder] * len(bikes)

    return dates, bikes, serials, builder 

def upload_to_google_sheet():

    # Define google sheet api credentials
    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("DriveAPIKey.json", scope)
    client = gspread.authorize(creds)
      
    # Insert new row for each list index
    index = 0
    sheet = client.open("buildtracker").sheet1
    for (i, j, k, z) in zip(dates, bikes, serials, builder):
        data = sheet.get_all_records()
        nextRow = [dates[index], bikes[index], serials[index], builder[index]]
        sheet.insert_row(nextRow, len(data)+2)
        index += 1
    
if __name__ == "__main__":

    # Send image to google and return response
    response = image_to_text_lists()

    # Format response for google sheet
    dates, bikes, serials, builder = format_for_google_sheet()

    # Upload to google sheet
    upload_to_google_sheet()