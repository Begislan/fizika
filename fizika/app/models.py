from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class CoreGlav(models.Model):
    name = models.CharField(max_length=255, verbose_name="Основной глава:")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Основной Глава"


class Glav(models.Model):
    core_glav = models.ForeignKey(CoreGlav, on_delete=models.CASCADE, verbose_name="Основной глава: ")
    name = models.CharField(max_length=255, verbose_name="глава: ")

    def __str__(self):
        return f"{self.core_glav} | {self.name}"

    class Meta:
        verbose_name = "Глава"


class Theme(models.Model):
    glav = models.ForeignKey(Glav, on_delete=models.CASCADE, verbose_name="Глава: ")
    title = models.CharField(max_length=255, verbose_name="Тема: ", default="тема")
    full_text = RichTextUploadingField()

    def __str__(self):
        return f"{self.glav} | {self.title}"
