from django.db import models
from users.models import User
from staf.models import Staf
from django.utils.timezone import now





class Job(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    staf=models.ForeignKey(Staf, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    location=models.CharField(max_length=150)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    requirements=models.TextField()
    ideal_candidate=models.TextField()
    skills_required = models.TextField(null=True, blank=True)
    is_available=models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=now)
    

    def __str__(self):
        return self.title
    
    
class Apply(models.Model):
        status_choices=(
            ('Accepted','Accepted'),
            ('Rejected','Rejected'),
            ('Pending','Pending'),
        )
        
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        job=models.ForeignKey(Job,on_delete=models.CASCADE)
        timestamp=models.DateTimeField(auto_now_add=True)
        status=models.CharField(max_length=30,choices=status_choices,default='Pending')
    
        def __str__(self):
          return f"{self.user.username} - {self.job.title} ({self.status})"



class CoverLetter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    content = models.TextField()  # Contenu généré de la lettre
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cover Letter for {self.job.title} by {self.user.username}'
        