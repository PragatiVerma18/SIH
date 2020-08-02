from django.http import JsonResponse


def ApplicantStats(request):
    data = {
        'MHRD': 4,
        'ONGC': 5,
        'IOCL': 6,
        'SBI': 6,
        'CBSE': 7,
        'BHEL': 2,
        'KV': 5,
        'AIR': 2,
        'RBI': 1,
        'GAIL': 5,
        'HP': 3,
        'INDIAN POST': 4,
        'NABARD': 3,
        'ISRO': 6,
        'IIT-K': 8,
        'IIT-B': 3,
        'IRCTC': 6,
        'ICMR': 4,
        'FICCI': 6,
        'NTPC': 7,
        'DOORDARSHAN': 9,
        'ITR': 5,
        'DRDO': 7,
        'AIIMS': 10,
        'Tata Memorial Center': 4,
        'NIRDPR': 4,
        'CSIR': 8,
        'NATS': 2,
        'IIOP': 4,
        'oillimited': 4

    }
    return JsonResponse(data)


def TimeStats(request):
    data = {
        'MHRD': 40,
        'ONGC': 50,
        'IOCL': 60,
        'SBI': 45,
        'CBSE': 35,
        'BHEL': 30,
        'KV': 50,
        'AIR': 20,
        'RBI': 40,
        'GAIL': 50,
        'HP': 30,
        'INDIAN POST': 40,
        'NABARD': 30,
        'ISRO': 60,
        'IIT-K': 56,
        'IIT-B': 30,
        'IRCTC': 60,
        'ICMR': 40,
        'FICCI': 60,
        'NTPC': 50,
        'DOORDARSHAN': 38,
        'ITR': 50,
        'DRDO': 45,
        'AIIMS': 40,
        'Tata Memorial Center': 40,
        'NIRDPR': 40,
        'CSIR': 60,
        'NATS': 40,
        'IIOP': 30,
        'oillimited': 40

    }
    return JsonResponse(data)
