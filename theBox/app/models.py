#=======================================================================================
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Data(models.Model):
    sid = models.IntegerField(primary_key=True)
    cid = models.IntegerField()
    data_payload = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data'
        unique_together = (('sid', 'cid'),)


class Detail(models.Model):
    detail_type = models.IntegerField(primary_key=True)
    detail_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'detail'


class Encoding(models.Model):
    encoding_type = models.IntegerField(primary_key=True)
    encoding_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'encoding'


class Event(models.Model):
    sid = models.IntegerField(primary_key=True)
    cid = models.IntegerField()
    signature = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'event'
        unique_together = (('sid', 'cid'),)


class Icmphdr(models.Model):
    sid = models.IntegerField(primary_key=True)
    cid = models.IntegerField()
    icmp_type = models.IntegerField()
    icmp_code = models.IntegerField()
    icmp_csum = models.SmallIntegerField(blank=True, null=True)
    icmp_id = models.SmallIntegerField(blank=True, null=True)
    icmp_seq = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icmphdr'
        unique_together = (('sid', 'cid'),)


class Iphdr(models.Model):
    sid = models.IntegerField(primary_key=True)
    cid = models.IntegerField()
    ip_src = models.IntegerField()
    ip_dst = models.IntegerField()
    ip_ver = models.IntegerField(blank=True, null=True)
    ip_hlen = models.IntegerField(blank=True, null=True)
    ip_tos = models.IntegerField(blank=True, null=True)
    ip_len = models.SmallIntegerField(blank=True, null=True)
    ip_id = models.SmallIntegerField(blank=True, null=True)
    ip_flags = models.IntegerField(blank=True, null=True)
    ip_off = models.SmallIntegerField(blank=True, null=True)
    ip_ttl = models.IntegerField(blank=True, null=True)
    ip_proto = models.IntegerField()
    ip_csum = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iphdr'
        unique_together = (('sid', 'cid'),)


class Opt(models.Model):
    sid = models.IntegerField(primary_key=True)
    cid = models.IntegerField()
    optid = models.IntegerField()
    opt_proto = models.IntegerField()
    opt_code = models.IntegerField()
    opt_len = models.SmallIntegerField(blank=True, null=True)
    opt_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opt'
        unique_together = (('sid', 'cid', 'optid'),)


class Reference(models.Model):
    ref_id = models.AutoField(primary_key=True)
    ref_system_id = models.IntegerField()
    ref_tag = models.TextField()

    class Meta:
        managed = False
        db_table = 'reference'


class ReferenceSystem(models.Model):
    ref_system_id = models.AutoField(primary_key=True)
    ref_system_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reference_system'


class Schema(models.Model):
    vseq = models.IntegerField(primary_key=True)
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'schema'


class Sensor(models.Model):
    sid = models.AutoField(primary_key=True)
    hostname = models.TextField(blank=True, null=True)
    interface = models.TextField(blank=True, null=True)
    filter = models.TextField(blank=True, null=True)
    detail = models.IntegerField(blank=True, null=True)
    encoding = models.IntegerField(blank=True, null=True)
    last_cid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sensor'


class SigClass(models.Model):
    sig_class_id = models.AutoField(primary_key=True)
    sig_class_name = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'sig_class'


class SigReference(models.Model):
    sig_id = models.IntegerField(primary_key=True)
    ref_seq = models.IntegerField()
    ref_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sig_reference'
        unique_together = (('sig_id', 'ref_seq'),)


class Signature(models.Model):
    sig_id = models.AutoField(primary_key=True)
    sig_name = models.CharField(max_length=255)
    sig_class_id = models.IntegerField()
    sig_priority = models.IntegerField(blank=True, null=True)
    sig_rev = models.IntegerField(blank=True, null=True)
    sig_sid = models.IntegerField(blank=True, null=True)
    sig_gid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'signature'


class Tcphdr(models.Model):
    sid = models.IntegerField(primary_key=True)
    cid = models.IntegerField()
    tcp_sport = models.SmallIntegerField()
    tcp_dport = models.SmallIntegerField()
    tcp_seq = models.IntegerField(blank=True, null=True)
    tcp_ack = models.IntegerField(blank=True, null=True)
    tcp_off = models.IntegerField(blank=True, null=True)
    tcp_res = models.IntegerField(blank=True, null=True)
    tcp_flags = models.IntegerField()
    tcp_win = models.SmallIntegerField(blank=True, null=True)
    tcp_csum = models.SmallIntegerField(blank=True, null=True)
    tcp_urp = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tcphdr'
        unique_together = (('sid', 'cid'),)


class Udphdr(models.Model):
    sid = models.IntegerField(primary_key=True)
    cid = models.IntegerField()
    udp_sport = models.SmallIntegerField()
    udp_dport = models.SmallIntegerField()
    udp_len = models.SmallIntegerField(blank=True, null=True)
    udp_csum = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'udphdr'
        unique_together = (('sid', 'cid'),)
