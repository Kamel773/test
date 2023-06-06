def convert_xml_to_json(xml_string):
    """
    Converts XML string to JSON.

    :param xml_string: The XML string to convert.
    :return: The JSON representation of the XML.
    """
    try:
        json_data = json.dumps(xmltodict.parse(xml_string), indent=4)
        return json_data
    except xmltodict.expat.ExpatError as e:
        print(f"Error parsing XML: {str(e)}")
        return None
    except Exception as e:
        print(f"Error converting XML to JSON: {str(e)}")
        return None
