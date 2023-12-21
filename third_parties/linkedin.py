import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    scrape information from linkedin profile,
    Manually scrape the information from the LinkedIn profile
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data


def json_filter(json: dict):
    data = json
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data


gist_response = requests.get(
    "https://gist.githubusercontent.com/Akumsk/f878eb88715aa8d37932d59d9cc34f4d/raw/9fe9ab1d5deee943f4469781479f88b0f817f5a5/Andrey_Kumskov_Linkedin.json"
)
gist_linkedin_profile = gist_response.json()
gist_linkedin_profile_filtered = json_filter(gist_linkedin_profile)
