def parse_letter(path: str) -> dict:
    """
    Function that parses the letters. Returns a dictionary: {version_id: {line_id: text}}
    """
    
    versions = {1: {}, 2: {}, 3: {}}

    with open(path, "r") as letter:
        for line in letter:
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                full_id = parts[0]
                text = parts[1]

                version = int(full_id[0])
                line_id = full_id[1:]

                version[version][line_id] = text
    
    return versions 
