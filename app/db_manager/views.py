import pandas as pd
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.shortcuts import render

from core.models import PostcodeModel


@user_passes_test(lambda u: u.is_superuser)
def db_manager(request):
    return render(request, "db-manager.html", )


@user_passes_test(lambda u: u.is_superuser)
def postcode_upload(request):
    """View for uploading data to database """
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            critical_error = "Incorrect file format. Please upload CSV file"
            return render(request, "postcode-upload.html",
                {"critical_error": critical_error, })
        dataset = pd.read_csv(csv_file, encoding="utf-8-sig")

        for code in dataset.itertuples():
            PostcodeModel.objects.create(
                postcode=code.postcode,
                lat=code.lat,
                long =code.long,
                county=code.county,
                district=code.district,
                ward=code.ward,
                constituency=code.constituency,
            )

        return redirect("/")

    return render(request, "postcode-upload.html", )
