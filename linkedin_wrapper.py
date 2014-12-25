from linkedin import linkedin

## get all API info by registering your app with the Linkedin Developer API (https://www.linkedin.com/secure/developer)


class LinkedIn():
	def __init__(self):
		self.consumer_key = "consumer_key" #consumer key
		self.consumer_secret = "consumer_secret" # consumer secret 
		self.access_token = "access_token" #consumer access token
		self.access_token_secret = "access_token_secret" #consumer access token secret
		self.RETURN_URL = 'http://site.com' # redirection after LinkedIn authentication
		self.authentication= linkedin.LinkedInAuthentication(self.consumer_key,self.consumer_secret,self.RETURN_URL,linkedin.PERMISSIONS.enums.values())

	# go to returned url, and authorize linkedin profile, to get authorization code for token generation! It'll be in the slug of the redirection url, prefixed by "?code="
	def get_authorization_url(self):
		 url = self.authentication.authorization_url 
		 return url 
	
	# generate token using authorization
	def generate_token(self,code):
		self.authentication.authorization_code = code
		token = self.authentication.get_access_token()
		return token

	# use token from generate_token above to get profile
	def get_profile(self, token):
		app = linkedin.LinkedInApplication(token=token)
		return app.get_profile(selectors=['id', 'first-name', 'last-name', 'positions','location', 'distance', 'num-connections', 'skills', 'educations'])




