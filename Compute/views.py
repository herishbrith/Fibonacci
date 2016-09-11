from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Compute.forms import NumberForm

@csrf_exempt
def computeNthNumber(request):

	if request.method == "GET":

		form = NumberForm()
		return render(request, "Compute/Fibonacci.html", {"form": form})


	elif request.method == "POST":

		form = NumberForm(data=request.POST)

		if form.is_valid():

			data = form.data
			pos = int(data["nthNumber"])
			x, y, z = 0, 1, 1

			for i in range(pos-1):

				z = x + y
				x = y
				y = z

			return render(request, "Compute/Fibonacci.html", {"result": z, "form": form})

		else: return render(request, "Compute/Fibonacci.html", {"form": form})
