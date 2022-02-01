def load_text(filename):
    """Read file and save it's output in a variable. Return the variable."""
    with open(filename, encoding="UTF-8") as f:
        lines = f.readlines()

        return lines

def get_words(lines):
    """Get all words from the string and store them separately in a list"""
    word = ""
    words = []

    for string in lines:
        for letter in string:
            word += letter

            if letter == " ":
                words.append(word)
                word = ""
            
        # Below command exist only for the last letters (after the last SPACE)        
        words.append(word)
        word = ""
    
    return words

def get_formatted_lines(words):
    """Store each properly formatted line in a list"""
    formatted_line = ""
    formatted_lines = []
    line_limit = 80

    for word in words:
        if '\n' in word:
            if len(formatted_line) + len(word) < line_limit:
                formatted_line += word
                formatted_lines.append(formatted_line)
                formatted_line = ""
            else:
                formatted_line += f"\n{word}"
                formatted_lines.append(formatted_line)
                formatted_line = ""

        # If f_line + word are less than 80 characters, add word in f_line
        elif len(formatted_line) + len(word) < line_limit:
            formatted_line += word
        else:
            # Add newline at the end of f_line string, append f_line in f_lines
            # Then store the unused word to use in new f_line
            formatted_line += '\n'
            formatted_lines.append(formatted_line)
            formatted_line = word
    
    # Below command exist only for the last f_line
    formatted_lines.append(formatted_line)
    return formatted_lines

def get_formatted_text(formatted_lines):
    """Store all formatted lines in a variable as a single string"""
    formatted_text = ""

    for line in formatted_lines:
        formatted_text += line

    return formatted_text

def save_text(filename, text):
    """(Over)Write text in selected file"""
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(text)

def format_text(loading_file, saving_file):
    """Load a file, create a proper text format and save it in selected file"""
    # Load text and store lines in a list
    lines = load_text(loading_file)

    # Format the text properly
    words = get_words(lines)
    formatted_lines = get_formatted_lines(words)
    formatted_text = get_formatted_text(formatted_lines)
    
    # Save formatted text in selected file
    save_text(saving_file, formatted_text)