from django.db import models

class SmartPhone(models.Model):
    price = models.FloatField()
    img_url = models.CharField(max_length=255)
    color = models.CharField(max_length=30)
    ram = models.IntegerField()
    memory = models.IntegerField()
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def to_dict(self):
        returned = {
            'id': self.id,
            'price': self.price,
            'img_url':self.img_url,
            'color':self.color,
            'ram':self.ram,
            'memory':self.memory,
            'name':self.name,
            'model':self.model,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
        return returned