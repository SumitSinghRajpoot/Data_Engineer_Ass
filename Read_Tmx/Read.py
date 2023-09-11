
import xml.etree.ElementTree as ET
import glob

# Specify the path to the TMX file
# tmx_file_path = 'C:\\Users\\SUMIT SINGH RAJPOOT\\OneDrive\\Documents\\ar-en.tmx\\ar-en.tmx'
var=glob.glob("C:\\Users\\SUMIT SINGH RAJPOOT\\OneDrive\\Documents\\ar-en.tmx\\*.tmx")
# print(var)

# Define the XML namespace for the 'xml' prefix
xml_namespace = {'xml': 'http://www.w3.org/XML/1998/namespace'}

# Parse the TMX file with the namespace definition
for i in var:
    tree = ET.parse(i)
    root = tree.getroot()

    # Initialize a list for translation pairs
    translation_pairs = []

    # Extract translation pairs (English and Arabic)
    for tu in root.findall('.//body/tu'):
        english_text = tu.find(".//tuv[@xml:lang='en']/seg", namespaces=xml_namespace).text
        arabic_text = tu.find(".//tuv[@xml:lang='ar']/seg", namespaces=xml_namespace).text
        translation_pairs.append((english_text, arabic_text))

    # Specify the output file path
    output_file_path = 'translation_pairs.txt'

    # Open the file for writing
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Write each translation pair to the file
        for pair in translation_pairs:
            english_text, arabic_text = pair
            output_file.write(f"English: {english_text}\nArabic: {arabic_text}\n\n")

    print(f"Translation pairs have been written to {output_file_path}")
