from django.shortcuts import render
from jobPost.models import JobPost
from Categories.models import Categories

def home(request, brand_slug=None):
    data = JobPost.objects.all()
    if brand_slug is not None:
        category = Categories.objects.get(slug=brand_slug)
        data = JobPost.objects.filter(categories=category)
    categories = Categories.objects.all()
    job_types = dict(JobPost.JOB_TYPES)
    return render(request, 'home.html', {'data': data, 'categories': categories, 'job_types': job_types})
