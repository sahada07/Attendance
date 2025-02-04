from django.contrib import admin
from .models import User, AuthCredential, Report, Visitor, IncomingLetter, OutgoingLetter

admin.site.register(User)
admin.site.register(AuthCredential)
admin.site.register(Report)
admin.site.register(Visitor)
admin.site.register(IncomingLetter)
admin.site.register(OutgoingLetter)
