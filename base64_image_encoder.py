import base64
from pathlib import Path
from PIL import Image
import io

def encode_image_to_base64(image_path):
    with Image.open(image_path) as image:
        buffered = io.BytesIO()
        image.save(buffered, format=image.format)
        return base64.b64encode(buffered.getvalue()).decode()

def generate_html_with_base64_images(image_folder):
    html_content = '<script>\nconst base64ImageMap = new Map();\n'
    for image_path in Path(image_folder).glob('*.png'):  # Adjust the glob pattern for different image types (e.g., '*.png')
        base64_image = encode_image_to_base64(image_path)
        image = image_path.name
        html_content += f'base64ImageMap.set("{image}", `data:image/png;base64,{base64_image}`);\n'  # Adjust 'image/jpeg' as needed
    html_content += '\n</script>'

    with open('images_base64.html', 'w') as html_file:
        html_file.write(html_content)

# Usage
generate_html_with_base64_images('./images')
