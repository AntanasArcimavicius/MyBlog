from django.db import models

# Create your models here.


class Resume(models.Model):
    owner = models.ForeignKey("user.User", on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="mainsite", height_field=None, width_field=None, blank=True)
    role = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return f"{self.owner} CV"


class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    portfolio = models.ForeignKey("mainsite.Resume", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} skill"


class WorkExperience(models.Model):
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    portfolio = models.ForeignKey("mainsite.Resume", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.role} in {self.company}"


class Education(models.Model):
    school = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    portfolio = models.ForeignKey("mainsite.Resume", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.school}, {self.degree}, {self.field_of_study}"
