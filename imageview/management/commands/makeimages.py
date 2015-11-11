from django.core.management.base import BaseCommand, CommandError
from imageview.models import Image
from django.core.exceptions import ValidationError
from django.db import IntegrityError
import os
# django.db.utils.IntegrityError
class Command(BaseCommand):
    help = 'Creates a list of all '

    def handle(self, *args, **options):
        # print(Image.objects.all())
        root_dir = 'media/images'
        for _, _, files in os.walk(root_dir):
            for f in files:
                full_path = "images/%s" % f
                print("\n%s" % full_path.ljust(50),end='')
                
                i = Image(image_file=full_path,title=f,description="")
                print(" ... ",end='')

                try:
                    print('creating md5 ',end='')
                    i.clean()
                    print('unique ',end='')
                except ValidationError:
                    print("Image already exists",end='')
                else:
                    try:
                        i.save()
                        print("Saved",end='')
                    except IntegrityError:
                        print("Key already exists",end='')
        print('\n')
        
