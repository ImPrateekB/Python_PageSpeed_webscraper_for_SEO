#Code written By Pratik B
import requests


#This Block of Code is responsible for fetching Desktop Insights
def get_pagespeed_insights1(url, strategy="desktop"):
    try:
        api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy={strategy}"
        response = requests.get(api_url)
        data = response.json()
        
        score = data["lighthouseResult"]["categories"]["performance"]["score"]
        return score
    except Exception as e:
        print("An error occurred:", e)
        return None
    
#This Block of Code is responsible for fetching Mobile Insights    

def get_pagespeed_insights(url, strategy="mobile"):
    try:
        api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy={strategy}"
        response = requests.get(api_url)
        data = response.json()
        
        score = data["lighthouseResult"]["categories"]["performance"]["score"]
        return score
    except Exception as e:
        print("An error occurred:", e)
        return None

##This Block of Code is responsible for fetching User Input
if __name__ == "__main__":
    website_url = input("Enter the URL you want to analyze : ") 
    pagespeed_score1 = get_pagespeed_insights1(website_url)
    pagespeed_score2 = get_pagespeed_insights(website_url)
    
    if pagespeed_score1 is not None:
        print(f"PageSpeed Score for desktop is : {pagespeed_score1 * 100:.2f}")

    if pagespeed_score2 is not None:
        print(f"PageSpeed Score for mobile is : {pagespeed_score2 * 100:.2f}")
