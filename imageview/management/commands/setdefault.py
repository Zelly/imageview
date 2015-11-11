from django.core.management.base import BaseCommand, CommandError
from imageview.models import Image
from django.core.exceptions import ValidationError
from django.db import IntegrityError
import os


class Command(BaseCommand):
    help = 'Makes sure all image models have description'

    def handle(self, *args, **options):
        for img in Image.objects.all():
            if not img.description:
                img.description = "No description"
                img.save()
                print("Updated description")
        
