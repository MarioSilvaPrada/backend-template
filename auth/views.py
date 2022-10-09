from django.views.generic import TemplateView

# Create your views here.


class SuccessVerifyView(TemplateView):
    template_name = 'account/success_verification.html'

success_verify = SuccessVerifyView.as_view()
