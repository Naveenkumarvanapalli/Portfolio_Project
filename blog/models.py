from django.db import models

# Create your models.
    # Title
    # Publication date
    # content Body
    # Image
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:101]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
# Add to Blog app to the Settings
# Create a migration
# Migrate
# Add to the admin