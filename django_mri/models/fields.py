"""
Definition of a custom :class:`~django.contrib.postgres.fields.ArrayField`
subclass.

Copied from
https://blogs.gnome.org/danni/2016/03/08/multiple-choice-using-djangos-postgres-arrayfield/.
"""

from django import forms
from django.contrib.postgres.fields import ArrayField


class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of choices.

    Uses Django's PostgreSQL ArrayField and a MultipleChoiceField for its
    formfield.
    """

    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
        }
        defaults.update(kwargs)
        # Skip our parent's formfield implementation completely as we don't
        # care for it.
        # pylint:disable=bad-super-call
        return super(ArrayField, self).formfield(**defaults)
