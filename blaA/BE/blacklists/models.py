from django.db import models

# Create your models here.
class Blacklist(models.Model) :
    blacklist_pk = models.AutoField(primary_key=True)
    user_pk = models.ForeignKey('accounts.User',on_delete=models.CASCADE, related_name='from_user_pk')
    user_pk = models.ForeignKey('accounts.User',on_delete=models.CASCADE, related_name='to_user_pk')
    black_content = models.CharField(max_length=50)
    black_reason = models.CharField(max_length=20)
    