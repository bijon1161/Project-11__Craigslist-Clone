from django.db import models


class Search(models.Model):
    query = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.query

    class Meta:
        # pass
        verbose_name_plural = 'Searches'
