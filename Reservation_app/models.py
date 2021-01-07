from django.db import models

# Create your models here.
class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255)
    capacity= models.PositiveBigIntegerField()
    projector_availability =models.BooleanField("is_projector", default=False)
    def __str__(self):
        return f"Nazwa sali:{self.name} Ilosc miejsc:{self.capacity} Projektor:{self.projector_availability}"

    def get_detail_url(self):
        return f'/room/{self.id}'