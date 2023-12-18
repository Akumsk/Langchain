import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    scrape information from linkedin profile,
    Manually scrape the information from the LinkedIn profile
    """
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}