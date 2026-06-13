from django.db import models

from django.contrib.auth.models import User




class Profile(models.Model):


    user = models.OneToOneField(

        User,

        on_delete=models.CASCADE

    )




    image = models.ImageField(

        upload_to="profiles",

        default="profiles/default.png"

    )




    phone = models.CharField(

        max_length=15,

        blank=True

    )




    address = models.TextField(

        blank=True

    )




    city = models.CharField(

        max_length=100,

        blank=True

    )





    def __str__(self):


        return self.user.username