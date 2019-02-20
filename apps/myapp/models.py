from django.db import models

class StudentManager(models.Manager):
    def registerValidator(self, form):
        # print(form)
        errors = {}

        fname = form["fname"]
        lname = form["lname"]

        if len(fname) < 1:
            errors["fname"] = "First name cannot be blank"
        if len(lname) < 1:
            errors["lname"] = "Last name cannot be blank"

        return errors


class Student(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = StudentManager()

    def __repr__(self):
        return f"<Student {self.fname} {self.lname} id: {self.id}>"
