import os, io, string
from google.cloud import vision
from google.cloud.vision import types

# IMAGE PRE-PROCESSING shouldn't be needed with google vision but otherwise (scale to usable DPI, skew correction, adjust threshold to binarize, remove noise)

def image_to_text():

    # Login to google vision api
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'VisionAPIKey.json'
    client = vision.ImageAnnotatorClient()

    # Define the image
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, r'Images\BuildBook01.jpg')
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    # Send the request and receive the response
    input = vision.types.Image(content = content)
    response = client.document_text_detection(image = input)
    return response

def format_for_google_sheet(response):

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

    # Break into separate lists of date, bikes, serials with ':'
    joinedList = joinedString.split(':')
    date = joinedList[0]
    bikes = joinedList[1]    
    serials = joinedList[2]

    # Substitute brand names for shorthand and separate bike lines
    bikes = bikes.replace('R ', '\nReid ')
    bikes = bikes.replace('M ', '\nMerida ')
    bikes = bikes.replace('N ', '\nNorco ')
    bikes = bikes.strip()
    bikes = bikes.split('\n')
    
    # Separate serial lines with '+'   
    serials = serials.replace(" ", "")
    serials = serials.split('+')
    
    # Assign date for each line
    date = date.strip()
    dates = [date] * len(bikes)

    # Assign builder for each line
    builder = 'Karl'
    builder = [builder] * len(bikes)

    print(dates)
    print(bikes)
    print(serials)
    print(builder)

def upload_to_google_sheet():

    # Integrate google sheets api and upload lists at next available row in the correct sheet
    placeholder = 1

if __name__ == "__main__":

    # Send image to google and return response
    response = image_to_text()

    # Format response for google sheet
    format_for_google_sheet(response)