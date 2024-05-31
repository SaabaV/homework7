from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    NEW = 'New'
    IN_PROGRESS = 'In progress'
    PENDING = 'Pending'
    BLOCKED = 'Blocked'
    DONE = 'Done'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In progress'),
        (PENDING, 'Pending'),
        (BLOCKED, 'Blocked'),
        (DONE, 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('title', 'created_at')

    def __str__(self):
        return self.title


class SubTask(models.Model):
    NEW = 'New'
    IN_PROGRESS = 'In progress'
    PENDING = 'Pending'
    BLOCKED = 'Blocked'
    DONE = 'Done'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In progress'),
        (PENDING, 'Pending'),
        (BLOCKED, 'Blocked'),
        (DONE, 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
