from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from Compute.forms import NumberForm
from time import time

@csrf_exempt
def computeNthNumber(request):

	if request.method == "GET":

		# if the request method is GET, get a blank form
		form = NumberForm()
		return render(request, "Compute/Fibonacci.html", {"form": form})


	elif request.method == "POST":

		# if the request is POST, return the result
		form = NumberForm(data=request.POST)

		if form.is_valid():

			data = form.data
			pos = int(data["nthNumber"])
			start = time() # time to calculate the processing time
			x, y, z = 0, 1, 1

			for i in range(pos-1):

				z = x + y
				x = y
				y = z
			stop = time() - start
			return render(request, "Compute/Fibonacci.html", {"result": z, "form": form, "time": stop})

		else: return render(request, "Compute/Fibonacci.html", {"form": form})

	else: return redirect("computeNthNumber")
