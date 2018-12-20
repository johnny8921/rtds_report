from django.shortcuts import render, get_object_or_404, redirect
from .models import Work, Device
from django.utils import timezone
from .forms import AddWork, AddDevice
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def device_list(request):
    devices = Device.objects.order_by('factory_date')
    return render(request, 'work/device_list.html', {'devices': devices})

@login_required
def device_work_new(request, devicepk):
    device = get_object_or_404(Device, pk=devicepk)
    if request.method == "POST":
        form = AddWork(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            print(device.factory_number)
            work.factory_number = device.factory_number
            work.save()
        # Find adress to return preview page
        a=request.path_info.find(devicepk)
        a=request.path_info.find('/',a)+1
        return redirect(request.path_info[:a])
    else:
        print("else")
        form = AddWork(initial={'factory_number': device.factory_number})
        return render(request, 'work/work_edit.html', {'form': form})


@login_required
def device_work_edit(request, devicepk, pk):
    print('work_edit')
    work = get_object_or_404(Work, pk=pk)
    print (request.method)
    if request.method == "POST":
        print('POST')
        form = AddWork(request.POST, instance=work)
        if form.is_valid():
            print('form valid')
            work = form.save(commit=False)
            work.save()
        # Find adress to return preview page
        a=request.path_info.find(devicepk)
        a=request.path_info.find('/',a)+1
        return redirect(request.path_info[:a])
        # return redirect('/')
        # return redirect(request.path_info[:(request.path_info.find(pk) +1) * (-1)])
    else:
        form = AddWork(instance=work)
        return render(request, 'work/work_edit.html', {'form': form})

@login_required
def device_new(request):
    print("new device start")
    if request.method == "POST":
        print('post')
        form = AddDevice(request.POST)
        print('prevalid')
        if form.is_valid():
            print('valid')
            device = form.save(commit=False)
            device.save()
        return redirect('device_list')
    else:
        print('else')
        form = AddDevice()
        print(form)
        return render(request, 'work/device_edit.html', {'form': form})

@login_required
def device_edit(request, pk):
    print('device_edit')
    device = get_object_or_404(Device, pk=pk)
    # print (device)
    # print (request.method)
    if request.method == "POST":
        form = AddDevice(request.POST, instance=device)
        # print(form)
        if form.is_valid():
            print('form valid')
            device = form.save(commit=False)
            device.save()
        # Find adress to return preview page
        a=request.path_info.find(pk)
        a=request.path_info.find('/',a)+1
        return redirect(request.path_info[:a])
    else:

        form = AddDevice(instance=device)
        # print(form)
        return render(request, 'work/device_edit.html', {'form': form})

# checked and work
def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    works = Work.objects.filter(factory_number=device.factory_number)
    return render(request, 'work/device_detail.html', {'device': device, 'works': works})

def device_work_remove(request, devicepk, pk):
    work = get_object_or_404(Work, pk=pk)
    work.delete()
    a=request.path_info.find(devicepk)
    a=request.path_info.find('/',a)+1
    return redirect(request.path_info[:a])
    # return redirect('device_list')

def device_remove(request, pk):
    device = get_object_or_404(Device, pk=pk)
    device.delete()
    return redirect('/')



# def work_detail(request, pk):
#     work = get_object_or_404(Work, pk=pk)
#     return render(request, 'work/work_detail.html', {'work': work})


# def work_list(request):
#     works = Work.objects.order_by('date')
#     return render(request, 'work/work_list.html', {'works':works})

# @login_required
# def work_new(request):
#     if request.method == "POST":
#         form = AddWork(request.POST)
#         if form.is_valid():
#             work = form.save(commit=False)
#             work.author = request.user
#             work.published_date = timezone.now()
#             work.save()
#         return redirect('work_list')
#     else:
#         form = AddWork()
#         return render(request, 'work/work_edit.html', {'form': form})


# @login_required
# def work_edit(request, pk):
#     print('work_edit')
#     work = get_object_or_404(Work, pk=pk)
#     print (work)
#     print (request.method)
#     if request.method == "POST":
#         form = AddWork(request.POST, instance=work)
#         if form.is_valid():
#             print('form valid')
#             work = form.save(commit=False)
#             work.author = request.user
#             work.published_date = timezone.now()
#             work.save()
#         return redirect(request.path_info[:(request.path_info.find(pk) +1) * (-1)])
#     else:
#         form = AddWork(instance=work)
#         return render(request, 'work/work_edit.html', {'form': form})

