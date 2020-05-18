"""
Samuel Hohenshell

Gets the following from user:
    - Feal message name
    - Fake message name
    - Template name
    - Resulting document name
    - Keyword for Vigenére cipher encription
"""

# Sets up user input for everything
def setup():
    # Gathering user input for everything
    print("Welcome to my encription application.")
    REAL_FILENAME = input("Enter the name of the file, including its "
        "ending in .docx, containing the (unencrypted) \"real\" message you "
        "would like to send. \nSimply clicking enter will default "
        "to \"example_files/realMessage.docx\": ").strip()
    if len(REAL_FILENAME) == 0:
        REAL_FILENAME = "example_files/realMessage.docx"
    
    FAKE_FILENAME = input("Enter the name of the file, including its "
        "ending in .docx, containing the \"fake\" message that will be "
        "visible to anyone. \nSimply clicking enter will default "
        "to \"example_files/fakeMessage.docx\": ").strip()
    if len(FAKE_FILENAME) == 0:
        FAKE_FILENAME = "example_files/fakeMessage.docx"
    
    TEMPLATE = input("Enter the name of the template for the file, including "
        "its ending in .docx. This should contains no text but have all "
        "style, font, margins, etc. set. \nSimply clicking enter will "
        "default to \"example_files/template.docx\": ").strip()
    if len(TEMPLATE) == 0:
        TEMPLATE = "example_files/template.docx"

    RESULTING_DOC_NAME = input("Enter the name of the output document, "
        "including its ending in .docx. This will be where the final result "
        "is stored. \nSimply clicking enter will default "
        "to \"example_files/result.docx\": ").strip()
    if len(RESULTING_DOC_NAME) == 0:
        RESULTING_DOC_NAME = "example_files/result.docx"

    CIPHER_KEY = input("Enter the Vigenere cipher key. Must be all caps. "
        "\nSimply clicking enter will default to "
        "\"DEFAULT\": ").strip().upper()
    if len(CIPHER_KEY) == 0:
        CIPHER_KEY = "DEFAULT"

    return REAL_FILENAME, FAKE_FILENAME, TEMPLATE, \
        RESULTING_DOC_NAME, CIPHER_KEY
