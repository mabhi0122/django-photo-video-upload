from django.core.exceptions import ValidationError
import os

def validate_file_size(file):
    max_size_kb = 5000  # for example: max size of 5MB
    if file.size > max_size_kb * 1024: #file sizes are often measured in bytes(file.size is in bytes).
        raise ValidationError(f'File size should be less than {max_size_kb}KB')
    

def validate_file_extensions(file):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.mp4']
    ext = os.path.splitext(file.name)[1] # split the extension from the path name
    if not ext.lower() in valid_extensions:
        raise ValidationError(f'Unsupported file extension. Supported extensions are: {", ".join(valid_extensions)}')