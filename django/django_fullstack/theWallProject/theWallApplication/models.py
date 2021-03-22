from django.db import models
import re


# Create your models here.

class UserManager(models.Manager):
    def createValidator(self, postData):
        errors = {}
        if len(postData['firstName']) < 2:
            errors["firstName"] = "First Name must be longer than 1 character."
        if len(postData['lastName']) < 2:
            errors["lastName"] = "Last Name must be longer than 1 character."
        uniqueEmail = User.objects.filter(email=postData['email'])
        if len(uniqueEmail) >= 1:
            errors['duplicateEmail'] = "Email Taken. Use another Email."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Sets up RegEx variable. alphanumeric ". and _ and - and +" + @ + alphanumeric ". and _ and - " + . + alpha
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern
            errors['email'] = "Invalid email address."
        if len(postData['password']) < 8:
            errors["password"] = "Password must at least 7 characters."        
        if postData['password'] != postData['passwordConfirm']:
            errors["passwordConfirm"] = "Passwords do not match."
        return errors

class PostManager(models.Manager):
    def createValidator(self, postData):
        errors = {}        
        if len(postData['content']) < 1:
            errors["content"] = "Post cannot be Empty."
        return errors


class CommentManager(models.Manager):
    def createValidator(self, postData):
        errors = {}        
        if len(postData['content']) < 1:
            errors["content"] = "Comment cannot be Empty."
        return errors

class User(models.Model):
    firstName = models.CharField(max_length=17)
    lastName = models.CharField(max_length=17)
    email = models.CharField(max_length=50)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ONE USER MANY POSTS
    poster = models.ForeignKey(User, related_name="posts", on_delete = models.CASCADE)
    objects = PostManager()

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ONE USER MANY COMMENTS
    commenter = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    postIBelongTo = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    objects = CommentManager()
