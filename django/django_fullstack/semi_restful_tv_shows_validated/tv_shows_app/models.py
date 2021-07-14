from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # postData == request.POST
        if len(postData['title']) < 2:
            errors["title"] = "Title must be at least 2 characters long."
        if len(postData['network']) < 3:
            errors["network"] = "Network must be at least 3 characters long."
        if len(postData['description']) < 10:
            errors["description"] = "Description must be at least 10 characters long."

        #Release Date must be 13 years in the past or older
        print(postData['release_date'])
        #splits the data from request.POST on the - into a list
        nums = postData['release_date'].split("-")

        print(nums[0])
        # #adding 13 to the year so we can compare to present date
        add_thirteen = int(nums[0])+13
        # #typecasting year back to str and saving to split list
        nums[0] = str(add_thirteen)
        # #joining the split list into a whole list to turn back to date
        new_date = "-".join(nums)
            
        print(new_date)
        # #changing date str into datetime object
        date_plus_thirteen = datetime.strptime(new_date, '%Y-%m-%d')
        
        print(date_plus_thirteen    )
        print(datetime.now())
        # #if datetime has 13 years more and it's older 13 years haven't passed since bday -- birthday year should be younger than datetime.now()
        if date_plus_thirteen > datetime.now():
            errors["birthday"] = "You must be at least 13 years or older."
        return errors
        

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
