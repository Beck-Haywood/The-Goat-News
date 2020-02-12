
# from django.db import models
# from django.urls import reverse
# from django.utils.text import slugify


# class Article(models.Model):
#     title = models.CharField(max_length=150, null=True)
#     author = models.CharField(max_length=150, null=True)
#     description = models.CharField(max_length=300, null=True)
#     content = models.CharField(max_length=300, null=True)
#     source = models.CharField(max_length=100, null=True)
#     link = models.CharField(max_length=100, null=True)
#     image = models.ImageField(upload_to="", verbose_name="Image", null=True)
#     slug = models.CharField(max_length=20, blank=True, editable=False, null=True)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         """ Returns a fully-qualified path for an article. """
#         path_components = {"slug": self.slug}
#         return reverse("", kwargs=path_components)

#     def save(self, *args, **kwargs):
#         """ Creates a URL safe slug automatically when a new an article is created. """
#         if not self.pk:
#             self.slug = slugify(self.title, allow_unicode=True)

#         # Call save on the superclass.
#         return super(Article, self).save(*args, **kwargs)