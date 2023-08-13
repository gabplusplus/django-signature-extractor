from rest_framework import serializers
from .models import ExtractSign;

from django.core.validators import FileExtensionValidator
from pdf2image import convert_from_bytes

from django.core.files.uploadedfile import SimpleUploadedFile
from .extractor import signature_detect, perform_image_processing

import io
import os

from datetime import datetime

import cv2
import numpy as np

class ExtractSignSerialzier(serializers.ModelSerializer):
    file = serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpeg', 'jpg'])])

    class Meta:
        model = ExtractSign
        fields = [
            'id',
            'created_at',
            'file',
            'scanned_file'
        ]


    def validate_file(self, value):
        if value.size > 10 * 1024 * 1024:  # Specify your file size limit here (10 MB in this example)
            raise serializers.ValidationError('File size should not exceed 10 MB.')

        return value


    def file_extension(self, file):
        _, extension = os.path.splitext(file)
        return extension
    

    def create(self, validated_data):
        file_obj = validated_data.get('file')
        ext = file_obj.name.split('.')[-1].lower()
        print(ext)

        if ext == 'pdf':
            file_bytes = file_obj.read()
            converted_file = convert_from_bytes(file_bytes, single_file=True)
            print(converted_file[0])
            file_first = converted_file[0]

            buf = io.BytesIO()
            file_first.save(buf, format='PNG')
            image_bytes = buf.getvalue()

            image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
            processed_image = signature_detect(image)
            # processed_image = perform_image_processing(image)
        else:        
            image = cv2.imdecode(np.frombuffer(file_obj.read(), np.uint8), cv2.IMREAD_COLOR)
            # processed_image = perform_image_processing(image)
            processed_image = signature_detect(image)

        # Convert the processed image back to byte data
        _, extracted_image = cv2.imencode('.jpg', processed_image)
        extracted_file = SimpleUploadedFile(f'extracted_{datetime.now()}.jpg', extracted_image.tobytes())

        validated_data['scanned_sign'] = extracted_file

        return super().create(validated_data)