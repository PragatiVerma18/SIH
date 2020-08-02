from django.http import JsonResponse


def stats(request):
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

    }
    return JsonResponse(data)
