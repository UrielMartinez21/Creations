from django.shortcuts import render
from .models import AccessLogValentine
import user_agents


def index_v1(request):
    # Get the user's name from the URL
    name = request.GET.get('name', '')

    # Get the user's IP address
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip_address:
        # If the request comes from a proxy, the IP address is a list of IPs
        ip_address = ip_address.split(',')[0].strip()
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    # Get the user's device
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

    # Save the access log
    AccessLogValentine.objects.create(
        ip_address=ip_address,
        device=device,
        user_agent=user_agent_str,
    )

    return render(request, 'san_valentin/index_v1.html', {'name': name})