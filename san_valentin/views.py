from django.shortcuts import render
from .models import AccessLogValentine
import user_agents


def main_index(request):
    return render(request, 'san_valentin/main_index.html')


def index_v1(request):
    # 1. Obtener la dirección IP del visitante
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip_address:
        # Si se utiliza un proxy, se toma la primera IP
        ip_address = ip_address.split(',')[0].strip()
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    # 2. Obtener el user agent para conocer el dispositivo
    user_agent_str = request.META.get('HTTP_USER_AGENT', '')
    ua = user_agents.parse(user_agent_str)
    if ua.is_mobile:
        device = 'Móvil'
    elif ua.is_tablet:
        device = 'Tablet'
    elif ua.is_pc:
        device = 'PC'
    else:
        device = 'Otro'

    # 4. Guardar el registro en la base de datos
    AccessLogValentine.objects.create(
        ip_address=ip_address,
        device=device,
        user_agent=user_agent_str,
    )

    return render(request, 'san_valentin/index_v1.html')