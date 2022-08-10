from django.shortcuts import render


def test_index(request):
    return render(request, "adminlte\index.html")
