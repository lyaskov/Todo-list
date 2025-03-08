from django import forms

from tasks.models import Task


class TaskFormUpdate(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'})
    )

    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags', 'is_done']
        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'tags': forms.CheckboxSelectMultiple(
                attrs={'class': 'form-check-inline'}
            ),
            'is_done': forms.CheckboxInput(
                attrs={'class': 'form-check-input fw-bold'}
            ),
        }


class TaskFormCreate(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'})
    )

    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags']
        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'tags': forms.CheckboxSelectMultiple(
                attrs={'class': 'form-check-inline'}
            ),

        }
