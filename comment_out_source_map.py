import os

def comment_out_source_map(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Open the file in write mode to update the content
    with open(file_path, 'w') as file:
        for line in lines:
            if 'sourceMappingURL=bootstrap.bundle.min.js.map' in line:
                # Comment out the line
                file.write('/* ' + line.strip() + ' */\n')
            else:
                file.write(line)

if __name__ == "__main__":
    # Define the path to the bootstrap.bundle.min.js file
    js_file_path = 'assets/js/vendor/bootstrap.bundle.min.js'
    # Check if the file exists
    if os.path.exists(js_file_path):
        comment_out_source_map(js_file_path)
        print(f"Updated {js_file_path} successfully.")
    else:
        print(f"File {js_file_path} does not exist.")
