from django.db import models


class PostDetail(models.Model):

    firstname = models.CharField(db_column='First Name',max_length=100,blank=True,null=True)
    lastname = models.CharField(db_column='Last Name',max_length=100,blank=True,null=True)
    city = models.CharField(db_column='city',max_length=100,blank=True,null=True)
    mobile = models.CharField(db_column='Mobile',max_length=20,blank=True,null=True)
    address = models.TextField(db_column='Address',max_length=250,blank=True,null=True)

    class Meta:
        db_table = 'Post Detail'

    def __str__(self):
        return str(self.firstname)


    


