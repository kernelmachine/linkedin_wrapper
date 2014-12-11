linkedin_wrapper
================

Python wrapper to LinkedIn authentication API.

It was a pain to get LinkedIn authentication running with my Python web app, so I decided to make it simpler for everyone else. Here's a comprehensive Python wrapper to the LinkedIn authentication. 

The code includes a general class for LinkedIn authentication.

To generate authentication token in your app online, do following: 
Send user to following URL. 

url = LinkedIn().get_authorization_code()

Get token with following code (based on request library in Flask. Successful authentication redirects application to RETURN_URL?code=TOKEN)

token = LinkedIn().generate_app(request.args.get('code'))

