from fastapi import FastAPI
from sample_data import profiles,  interests

app = FastAPI()

@app.get("/")
def home():
    return {"hello i am working"}

@app.get("/profile/{id}")
def get_profile_by_id(id : int):
    print("id = ", id, type(id))
    for profile in profiles:
        print("checking: ", profile)
        if profile["id"] == id:
            return profile
    return {"Data not found!"}


@app.get("/profiles")
def get_profiles(city: str = None, interest: str = None):
    result = profiles
    if city:
        result = [p for p in result if p["city"].lower() == city.lower()]
    if interest:
        result = [p for p in result
                  if any(i.lower() == interest.lower() for i in p["interests"])]
    return result
