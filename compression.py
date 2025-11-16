import os
import zipfile

def compress_file(input_path, output_dir="compressed_uploads", target_name=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    file_name = target_name if target_name else os.path.basename(input_path)
    zip_path = os.path.join(output_dir, f"{file_name}.zip")

    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(input_path, arcname=os.path.basename(input_path))

    return zip_path
