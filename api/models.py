from django.db import models


# Create your models here.

class Manufacturer(models.Model):
    manufacturer_id = models.UUIDField(primary_key=True, editable=False)
    manufacturer_name = models.TextField()
    manufacturer_address = models.DateField()
    manufacturer_telephone = models.TextField()

    def __str__(self):
        return self.manufacturer_name[0:50]

    class Meta:
        db_table = 'manufacturer'


class MedicineInfo(models.Model):
    medicine_id = models.UUIDField(primary_key=True, editable=False)
    manufacturer_id = models.UUIDField(editable=False)
    medicine_title = models.TextField()
    medicine_description = models.TextField()
    expiration_date = models.DateTimeField()
    medicine_dosage = models.TextField()
    medicine_count = models.IntegerField()
    medicine_release_info = models.TextField()

    def __str__(self):
        return self.medicine_title[0:50]

    class Meta:
        db_table = 'medicine_info'


class MedicineInstruction(models.Model):
    medicine_id = models.UUIDField(primary_key=True)
    registration_number = models.IntegerField()
    medicine_trade_name = models.TextField()
    medicine_form = models.TextField()
    medicine_composition = models.TextField()
    medicine_description = models.TextField()
    indications_for_use = models.TextField()
    method_of_use = models.TextField()
    medicine_side_effect = models.TextField()
    medicine_release_form = models.TextField()
    medicine_storage_conditions = models.TextField()

    class Meta:
        db_table = 'medicine_instruction'


class MedicineJournal(models.Model):
    medicine_id = models.UUIDField(primary_key=True)

    class Meta:
        db_table = 'medicine_instruction'
