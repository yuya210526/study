from django.db import models


class Plan(models.Model):
    """計画"""
    PALENT = 1
    CHILD = 2
    TARGET_CATEGORY = (
        (PALENT, '親'),
        (CHILD, '子')
    )
    target_category = models.IntegerField('対象区分', choices=TARGET_CATEGORY)
    target_id = models.IntegerField('対象ID')
    target_date = models.DateField('対象日')
    plans = models.TextField('予定')
    results = models.TextField('実績')

    class Meta:
        constraints = [
            # 対象区分,対象ID,対象日で一意に特定
            models.UniqueConstraint(fields=['target_category', 'target_id', 'target_date'], name='unique_plan'),
        ]

    def __str__(self):
        return str(self.target_category) + '_' + str(self.target_id) + '_' + self.target_date.strftime('%Y-%m-%d')
