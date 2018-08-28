# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AutoConfigInfos(models.Model):
    objects = models.Manager()
    server_num = models.TextField(blank=True, null=True)
    board = models.TextField(blank=True, null=True)
    memory_bank = models.TextField(blank=True, null=True)
    hard_disk = models.TextField(blank=True, null=True)
    raid = models.TextField(blank=True, null=True)
    vga = models.TextField(blank=True, null=True)
    gpu = models.TextField(blank=True, null=True)
    hba = models.TextField(blank=True, null=True)
    net_card = models.TextField(blank=True, null=True)
    fc_card = models.TextField(blank=True, null=True)
    inspect_time = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip_info = models.TextField(blank=True, null=True)
    id = models.AutoField(primary_key=True)  # AutoField?
    state = models.TextField(blank=True, null=True)
    checkstate = models.IntegerField(blank=True, null=True)
    cpu = models.TextField(blank=True, null=True)
    aging_data = models.TextField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'auto_config_infos'
