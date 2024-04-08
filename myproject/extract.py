import xml.etree.ElementTree as ET

def extract_keywords_from_libdoc(doc_file):
    try:
        # Parse the Libdoc XML file and get the root element
        tree = ET.parse(doc_file)
        root = tree.getroot()

        keywords = []

        # Traverse the XML tree and extract keywords
        for lib in root.findall('keywords'):
            for kw in lib.findall('kw'):
                keyword = kw.get('name')
                keywords.append(keyword)

        return keywords
    except Exception as e:
        print(f"Error occurred while parsing {doc_file}: {e}")
        return None

# Example usage:
doc_file = 'lib.xml'
keywords = extract_keywords_from_libdoc(doc_file)
if keywords is not None:
    print(keywords)
else:
    print("Failed to extract keywords. Check the error message for details.")
