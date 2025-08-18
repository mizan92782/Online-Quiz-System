from django.db import models
from Quiz.models import Quiz 
from Student.models import Student

class Submission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission = models.JSONField()  # student's answers
    submission_on = models.DateField(auto_now_add=True)
    submitted = models.BooleanField(default=False)
    marks = models.IntegerField(default=0)

    class Meta:
        unique_together = ("quiz", "student")

    def save(self, *args, **kwargs):
        self.marks = 0

        quiz_questions = self.quiz.question
        student_answers = self.submission

        
        for q, s in zip(quiz_questions, student_answers):
            if q["answer"] == s["answer"]:
                self.marks += q.get("marks", 1)  # add marks for this question
        #submitted 
        self.submitted=True
        super().save(*args, **kwargs)
