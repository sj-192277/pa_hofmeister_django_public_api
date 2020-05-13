from django.db import models


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    type1 = models.CharField(max_length=64)
    type2 = models.CharField(max_length=64, blank=True, null=True)
    base_stat_speed = models.IntegerField()
    base_stat_spdef = models.IntegerField()
    base_stat_spatk = models.IntegerField()
    base_stat_atk = models.IntegerField()
    base_stat_def = models.IntegerField()
    sprites_back_default = models.URLField(blank=True, null=True)
    sprites_back_female = models.URLField(blank=True, null=True)
    sprites_back_shiny = models.URLField(blank=True, null=True)
    sprites_back_shiny_female = models.URLField(blank=True, null=True)
    sprites_front_default = models.URLField(blank=True, null=True)
    sprites_front_female = models.URLField(blank=True, null=True)
    sprites_front_shiny = models.URLField(blank=True, null=True)
    sprites_front_shiny_female = models.URLField(blank=True, null=True)

    def __repr__(self):
        return '<Pokemon {}>'.format(self.name)
