def total_carro(request):
    
    total = 0    
    if "carro" in request.session.keys():
        for key, value in request.session["carro"].items():
            total += int(value["total"])
    return {"total_carro": total}

