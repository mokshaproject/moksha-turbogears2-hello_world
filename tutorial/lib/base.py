# -*- coding: utf-8 -*-

"""The base Controller API."""

from tg import TGController, tmpl_context
from tg.render import render
from tg import request
from pylons.i18n import _, ungettext, N_
import tutorial.model as model

__all__ = ['BaseController']

import tutorial.widgets
from moksha.wsgi.ext.turbogears import global_resources

class BaseController(TGController):
    """
    Base class for the controllers in the application.

    Your web application should have one of these. The root of
    your application is used to compute URLs used by your app.

    """

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # TGController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']

        request.identity = request.environ.get('repoze.who.identity')
        tmpl_context.identity = request.identity

        tmpl_context.notification_widget = tutorial.widgets.PopupNotification
        tmpl_context.moksha_global_resources = global_resources

        return TGController.__call__(self, environ, start_response)
