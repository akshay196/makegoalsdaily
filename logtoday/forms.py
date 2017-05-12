
from django import forms
from logtoday.models import GoalsCategory, ShortTermGoals, DailyActivity


class GoalsCreateForm(forms.ModelForm):

    goal_category = forms.ChoiceField(widget=forms.Select(attrs={'class': 'btn btn-default'}))

    def __init__(self, *args, **kwargs):
        categories = tuple([(category.category_value, category.category_name) for category in
                            GoalsCategory.objects.only('category_value', 'category_name').all() or []])
        if not categories:
            categories = (
                ('Certification', 'Education - Certification'),
                ('Diploma', 'Education - Diploma'),
                ('Degree', 'Education - Degree'),
                ('Language', 'Programming - Language'),
                ('Tool', 'Software - Tool'),
                ('Project', 'OpenSource - Project'),
                ('Event', 'OpenSource - Event'),
                ('Celebration', 'Family - Occasion'),
                ('Excursion', 'Travel - Plan'),
                ('Extra-Curricular', 'Extracurricular - Activities'),
                ('Miscellaneous', 'Miscellaneous - Activities'),
            )
        super(GoalsCreateForm, self).__init__(*args, **kwargs)
        self.fields['goal_category'].choices = categories

    class Meta:
        model = ShortTermGoals
        fields = ['goal_slug', 'goal_desc', 'goal_target', 'goal_category']
        widgets = {
            'goal_target': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }


class ActivityCreateForm(forms.ModelForm):

    activity_goal_map = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        goals = tuple([(goal, goal) for goal in ShortTermGoals.objects.only('goal_slug').all() or []])
        super(ActivityCreateForm, self).__init__(*args, **kwargs)
        self.fields['activity_goal_map'].choices = goals

    class Meta:
        model = DailyActivity
        fields = ['activity_detail', 'activity_goal_map', 'activity_weightage', 'activity_star']
