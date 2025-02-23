from django.db import models

class ContentItem(models.Model):
    SECTION_CHOICES = [
        ('home', 'Главная страница'),
        ('about', 'О нас'),
        ('archive', 'Архив'),
    ]
    
    section = models.CharField(max_length=20, choices=SECTION_CHOICES, default='home')
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    order = models.IntegerField(default=0)  # Для сортировки

    class Meta:
        ordering = ['order', 'date']

    def __str__(self):
        return f"{self.title} ({self.section})"