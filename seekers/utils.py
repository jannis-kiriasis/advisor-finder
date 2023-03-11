def save_seeker_updates_in_request_session(request):
    """
    Save the seeker updated details in the request session to pass to the
    update seeker view.
    """
    request.session[
        'save_need'
        ] = 'save_need' in request.POST
    request.session[
        'save_postcode'
        ] = 'save_postcode' in request.POST
    request.session[
        'save_town_or_city'
        ] = 'save_town_or_city' in request.POST
    request.session[
        'save_street_address'
        ] = 'save_street_address' in request.POST
