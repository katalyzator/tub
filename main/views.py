from django.http import Http404
from django.shortcuts import render

# Create your views here.
from main.models import News, NewsImage, Event, EventImage, Photo, SliderImage, Activity, Activity2, Activity3, \
    ActivityImage, ActivityImage2, ActivityImage3


def index_view(request):
    news = News.objects.all().order_by('-updated')[:8]
    events = Event.objects.all().order_by('-updated')[:8]
    photos = Photo.objects.all().order_by('-timestamp')[:8]
    sliderImage = SliderImage.objects.all().order_by('-timestamp')[:3]
    context = {"news": news, "events": events, "photos": photos, "sliderImage": sliderImage}

    template = 'main/index.html'

    return render(request, template, context)


def singleNews(request, id):
    try:
        news = News.objects.get(id=id)

        images = NewsImage.objects.filter(news=news)

        context = {"news": news, "images": images}
        template = 'single_post.html'

        return render(request, template, context)

    except News.DoesNotExist:
        raise Http404
    except NewsImage.DoesNotExist:
        raise Http404


def singleActivity1(request, id):
    try:
        activity1 = Activity.objects.get(id=id)

        images = ActivityImage.objects.filter(activity=activity1)

        context = {"active": activity1, "images": images}
        template = 'single_activity.html'

        return render(request, template, context)

    except Activity.DoesNotExist:
        raise Http404
    except ActivityImage.DoesNotExist:
        raise Http404


def singleActivity3(request, id):
    try:
        activity3 = Activity3.objects.get(id=id)

        images = ActivityImage3.objects.filter(activity=activity3)

        context = {"active": activity3, "images": images}
        template = 'single_activity3.html'

        return render(request, template, context)

    except News.DoesNotExist:
        raise Http404
    except NewsImage.DoesNotExist:
        raise Http404


def singleActivity2(request, id):
    try:
        activity2 = Activity2.objects.get(id=id)

        images = ActivityImage2.objects.filter(activity=activity2)

        context = {"active": activity2, "images": images}
        template = 'single_activity2.html'

        return render(request, template, context)

    except News.DoesNotExist:
        raise Http404
    except NewsImage.DoesNotExist:
        raise Http404


def singleEvents(request, id):
    try:
        events = Event.objects.get(id=id)

        images = EventImage.objects.filter(event=events)

        context = {"events": events, "images": images}
        template = 'single_event.html'

        return render(request, template, context)

    except Event.DoesNotExist:
        raise Http404
    except EventImage.DoesNotExist:
        raise Http404


def more_photos(request):
    photos = Photo.objects.all().order_by('-timestamp')[:8]
    context = {"photos": photos}
    template = 'main/photos.html'

    return render(request, template, context)


def more_photos2(request):
    photos = Photo.objects.all().order_by('-timestamp')[:8]
    context = {"photos": photos}
    template = 'main/photos2.html'

    return render(request, template, context)


def more_photos3(request):
    photos = Photo.objects.all().order_by('-timestamp')[:8]
    context = {"photos": photos}
    template = 'main/photos3.html'

    return render(request, template, context)


def activity_news1(request):
    activity1 = Activity.objects.all().order_by('-timestamp')
    context = {"activity": activity1}
    template = 'activities.html'

    return render(request, template, context)


def activity_news2(request):
    activity2 = Activity2.objects.all().order_by('-timestamp')
    context = {"activity": activity2}
    template = 'activities2.html'

    return render(request, template, context)


def activity_news3(request):
    activity3 = Activity3.objects.all().order_by('-timestamp')
    context = {"activity": activity3}
    template = 'activities3.html'

    return render(request, template, context)


def all_news_view(request):
    context = {}
    template = 'all_news.html'

    return render(request, template, context)
