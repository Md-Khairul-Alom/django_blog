
from .models import Category


def get_cetegories(request):
    categories=Category.objects.all()
    return dict(categories=categories)