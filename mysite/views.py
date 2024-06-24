from django.shortcuts import render
from visits.models import PageVisit


def home_view(request):
    PageVisit.objects.create(path=request.path)
    my_page = 'Vseticek.com'
    qs_total = PageVisit.objects.all()
    qs_count = PageVisit.objects.filter(path=request.path)

    context = {
        'page_title': my_page,
        'queryset': qs_count,
        'page_visits_total': qs_total.count(),
        'page_visits': qs_count.count(),
    }
    return render(request, 'home.html', context)
