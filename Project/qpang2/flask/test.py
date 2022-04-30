data = {
    "html_attributions": [],
    "results": [
        {
            "business_status": "noOPERATIONAL",
            "geometry": {
                "location": {
                    "lat": 40.1102575,
                    "lng": -88.21890329999999
                },
                "viewport": {
                    "northeast": {
                        "lat": 40.1117398802915,
                        "lng": -88.2177390697085
                    },
                    "southwest": {
                        "lat": 40.1090419197085,
                        "lng": -88.22043703029151
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/gas_station-71.png",
            "icon_background_color": "#909CE1",
            "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/gas_pinlet",
            "name": "first K",
            "opening_hours": {
                "open_now": True
            },
            "photos": [
                {
                    "height": 608,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/106505817082601656647\">Circle K</a>"
                    ],
                    "photo_reference": "Aap_uEDMs5htW4_jctgx9JONYv7SgcrRVc5zQKWqpJG5yCdaJ09GCejG5b_EFOG-XboK7MKWXu-apyEPo-Om3q4u7cEowluQfdAmmk3HMqSXd4oggVsjhfZnM87RnBNevLtoXPbnNd6i6ynNJJW7KFSj13RtbE00aeI_xdoxtFlkNcsJovC3",
                    "width": 1080
                }
            ],
            "place_id": "ChIJm76n2RLXDIgR70FP1zAhYUk",
            "plus_code": {
                "compound_code": "4Q6J+4C Urbana, IL, USA",
                "global_code": "86GH4Q6J+4C"
            },
            "price_level": 1,
            "rating": 2.1,
            "reference": "ChIJm76n2RLXDIgR70FP1zAhYUk",
            "scope": "GOOGLE",
            "types": [
                "gas_station",
                "atm",
                "car_wash",
                "convenience_store",
                "meal_takeaway",
                "finance",
                "cafe",
                "car_repair",
                "restaurant",
                "food",
                "point_of_interest",
                "store",
                "establishment"
            ],
            "user_ratings_total": 9,
            "vicinity": "809 West Green Street, Urbana"
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {
                    "lat": 40.1108482,
                    "lng": -88.2190303
                },
                "viewport": {
                    "northeast": {
                        "lat": 40.11210473029151,
                        "lng": -88.21775006970849
                    },
                    "southwest": {
                        "lat": 40.10940676970851,
                        "lng": -88.22044803029149
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/shopping-71.png",
            "icon_background_color": "#4B96F3",
            "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/convenience_pinlet",
            "name": "second K",
            "opening_hours": {
                "open_now": False
            },
            "photos": [
                {
                    "height": 3000,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/116364601228449896522\">Jay Aviana</a>"
                    ],
                    "photo_reference": "Aap_uEAYmfWEjDWXYSfRlC4JzDbq16cVR6tadx6m527WoPmCim0lgiWFCUYybMvEJvlKJDg_reRHgCNIQhCXuCvgGuW2ACCNJkX2l09C6e53HQWFWOBoFpfTgpb-61geAk02Wc8Osf6UH1ei2H7t6-uzlGOkFXNYtSxMOxmcxTt2PXKAnl09",
                    "width": 4000
                }
            ],
            "place_id": "ChIJIdMa1BLXDIgRF-zYQUMtQvo",
            "plus_code": {
                "compound_code": "4Q6J+89 Urbana, IL, USA",
                "global_code": "86GH4Q6J+89"
            },
            "rating": 2.6,
            "reference": "ChIJIdMa1BLXDIgRF-zYQUMtQvo",
            "scope": "GOOGLE",
            "types": [
                "convenience_store",
                "gas_station",
                "restaurant",
                "food",
                "point_of_interest",
                "store",
                "establishment"
            ],
            "user_ratings_total": 16,
            "vicinity": "810 West Green Street, Urbana"
        }
    ],
    "status": "OK"
}
def operationfilter(dict):
    filtered = {}
    for res in dict["results"]:
        if res["business_status"] == "OPERATIONAL":
            filtered[res["name"]] = res
    return filtered

def openingfilter(dict):
    filtered = {}
    for res in dict["results"]:
        if res["opening_hours"]["open_now"] == True:
            filtered[res["name"]] = res
    return filtered

print(operationfilter(data))
print(openingfilter(data))