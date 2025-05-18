import qrcode

def read_user_data(file_path):
  try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                raise ValueError("The file must contain at least two lines: URL and filename.")
            url = lines[0].strip()
            filename = lines[1].strip()
            return url, filename
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

        def generate_qr_code(url, output_filename):
 
    try:
        qr = qrcode.make(url)
        qr.save(output_filename)
        print(f"QR code saved as '{output_filename}'")
    except Exception as e:
        print(f"Failed to generate or save QR code: {e}")

def main():
    file_path = 'userdata.txt'  # Change this if your file is named differently
    url, filename = read_user_data(file_path)
    if url and filename:
        generate_qr_code(url, filename)

if __name__ == "__main__":
    main()