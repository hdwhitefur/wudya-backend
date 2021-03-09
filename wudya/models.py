from django.db import models


class Option(models.Model):
    prompt = models.CharField(max_length=200)

    def __str__(self):
        return self.prompt


class OptionPair(models.Model):
    desc = models.CharField(max_length=120)
    prompt_a = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='prompt_a')
    prompt_b = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='prompt_b')
    votes_a = models.IntegerField(default=0)
    votes_b = models.IntegerField(default=0)

    def __str__(self):
        return "{} vs. {}".format(self.prompt_a, self.prompt_b)