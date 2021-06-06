from django.db import models
import ujson

class Flexi(models.Model):
    key = models.CharField(max_length=512, null=False)
    _value = models.TextField(blank=True)
    
    @property
    def value(self):
        return ujson.loads(self._value)

    @value.setter
    def value(self, input_value):
        if type(input_value) is dict:
            self._value = ujson.dumps(input_value)
        else:
            self._value = input_value

