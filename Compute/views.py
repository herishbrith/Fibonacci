from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from Compute.forms import NumberForm
from Compute.models import Count, SiteUser
from time import time

@csrf_exempt
def computeNthNumber(request):

	# Get the IP of the requesting user using the following lambda
	getAddress = lambda req: request.META.get('HTTP_X_FORWARDED_FOR')\
	if request.META.get('HTTP_X_FORWARDED_FOR')\
	else request.META.get('REMOTE_ADDR')

	# Get the visitor count
	count = Count.objects.get(pk=1)

	# if the request method is GET, get a blank form
	form = NumberForm()

	# Make a pageDict to hold the counts
	pageDict = {

		"visitCount": str(count.visitCount),
		"searchCount": str(count.searchCount),
		"form": form
	}

	if request.method == "GET":

		# Create response object
		response = render(request, "Compute/Fibonacci.html", pageDict)

		try:

			IP_DATA = str(getAddress(request))
			user, firstVisit = SiteUser.objects.get_or_create(ipAddress=IP_DATA)

			# Increase the visit count of the IP user if it's not his first visit
			if not firstVisit: user.visits += 1; user.save()

		except Exception, e: print e

		# Get cookie from the browser
		try: cookie = request.COOKIES["count"]

		except:

			# pass cookie along with response object
			response.set_cookie('count', True, max_age=86400)

			# Increase the user visit count on every GET request
			count.visitCount += 1; count.save()
		return response

	elif request.method == "POST":

		# if the request is POST, return the result
		form = NumberForm(data=request.POST)

		if form.is_valid():

			data = form.data
			pos = int(data["nthNumber"])

			# Increase the search count
			count

			try:

				IP_DATA = str(getAddress(request))
				user, firstVisit = SiteUser.objects.get_or_create(ipAddress=IP_DATA)

				# Increase the search count of the IP user
				user.searchCount += 1; user.save()

			except Exception, e: print e

			# Lambda function to get the ordinal of a number
			ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
			start = time() # time to calculate the processing time
			x, y, z = 0, 1, 1

			for i in range(pos-1):

				z = x + y
				x = y
				y = z
			stop = time() - start

			# Create the pageDict variables
			pageDict["result"] = z
			pageDict["time"] = stop
			pageDict["ordinal"] = ordinal(pos)
			return render(request, "Compute/Fibonacci.html", pageDict)

		else: return render(request, "Compute/Fibonacci.html", pageDict)

	else: return redirect("computeNthNumber")

def createCountEntry():

	count = Count.objects.all()

	if not count: Count.objects.create(visitCount=1, searchCount=1)
createCountEntry()
