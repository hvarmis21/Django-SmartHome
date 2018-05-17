from typing import List, Any

from django.shortcuts import render
from matplotlib.axes import Axes


def home_view(request):

        return render(request, 'home.html', {})


"""""
def graphic_view(request):
    from matplotlib import pylab
    from pylab import *
    import PIL, PIL.Image, StringIO
    x = arange(0, 2 * pi, 0.01)
    s = cos(x) ** 2
    plot(x, s)

    xlabel('xlabel(X)')
    ylabel('ylabel(Y)')
    title('Simple Graph!')
    grid(True)

    # Store image in a string buffer
    buffer = StringIO.StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.fromstring("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), mimetype="image/png")
"""


def detail_view(request):
    from .models import Data,User

    import matplotlib.pyplot as plt

   #  my_user = User.objects.all().get(username = request.user.username).id
    if request.user.is_authenticated():
        y_temperature = list(Data.objects.values_list("temperature").filter(user_id=3).order_by("-id")[:])
        y_noise = list(Data.objects.values_list("noise").filter(user_id=3).order_by("-id")[:])
        y_light = list(Data.objects.values_list("light").filter(user_id=3).order_by("-id")[:])
        # x_time = Data.objects.values_list("datetime").filter(user_id=2).order_by("-id")[:]
        y_temperature_end = list()
        y_noise_end = list()
        y_light_end = list()
        for y_t in y_temperature:
            for x in y_t:
                y_temperature_end.append(x)
        for y_n in y_noise:
            for i in y_n:
                y_noise_end.append(i)
        for y_l in y_light:
            for n in y_l:
                y_light_end.append(n)
        x = [0, 1,2]
        fig = plt.figure()
        ax = plt.subplot(111)
        ax2 = plt.subplot(111)
        ax3 = plt.subplot(111)

        ax.plot(x, y_temperature_end, label="Temperature")
        ax2.plot(x, y_noise_end, label="Noise")
        ax3.plot(x, y_light_end, label="Light")

        plt.xlabel("Time")
        plt.ylabel("Data's")
        plt.title("my-graph")

        ax.legend()
        ax2.legend()
        ax3.legend()

        fig.savefig("./graphics/static/my_figure.png")
        context = {
            "pic": "User"
        }
    else:

        context = {
            "pic": "Guest"
        }

    return render(request, 'graphics/detail.html', context)


def user_form(request):
    from .forms import UserForm
    # my_user = User.objects.get(username=str(request.user.username)).id
    if request.method == "POST":

        form = UserForm(request.POST or None)

        if form.is_valid():
            title = form.cleaned_data['title']
            my_content = form.cleaned_data['content']

            form.save()
            del form
            form = UserForm()
            content = {
                "form": form
            }
            return render(request, "graphics/form.html", content)
    else:
        form = UserForm()

    content = {
        'form': form,
    }

    return render(request, "graphics/form.html", content)


def login_view(request):

    return render(request, "login.html",{})


