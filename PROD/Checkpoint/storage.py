# myapp/storage.py
import os
from django.core.files.storage import FileSystemStorage

class CustomStaticStorage(FileSystemStorage):
    def __init__(self, location=None, base_url=None):
        if location is None:
            location = '/path/to/staticfiles'  # Update with your desired path
        super().__init__(location=location, base_url=base_url)
    
    def _save(self, name, content):
        # Add custom behavior for saving files
        return super()._save(name, content)
