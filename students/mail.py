from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


class MailSender:

    @staticmethod
    def notify_about_new_group(request, group):
        message = f"На вашем сайте создана новая группа\n\n" \
                  f"Группа '{group.name}'\n\n#Ваш сайт."

        message_html = render_to_string("mail/new_group.html", {"group": group}, request)

        send_mail("Создана новая группа", message, settings.DEFAULT_FROM_EMAIL,
                  ["masteraalish@gmail.com"], False, html_message=message_html)

