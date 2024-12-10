from django.shortcuts import render, redirect
from .forms import CustomerRegisterForm

def register_view(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Kullanıcıyı kaydet
            return redirect('login')  # Kayıttan sonra giriş sayfasına yönlendir
    else:
        form = CustomerRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
