import qrcode

def read_user_data(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().strip().splitlines()
            if len(lines) < 2:
                raise ValueError("File must contain exactly two lines: a URL and a filename.")
            url = lines[0].strip()
            filename = lines[1].strip()
            return url, filename
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find file: {file_path}")