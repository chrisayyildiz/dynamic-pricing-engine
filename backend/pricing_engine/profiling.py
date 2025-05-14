import random
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class UserProfile: 
    user_id: str
    operating_system: str
    time_on_site: float
    wtp: float
    loyalty: float
    sentiment: float
    churn_probability: float
    engagement_level: str
    last_purchase_days_ago: int

ENGAGEMENT_LEVELS = ["low", "medium", "high"]
OPERATING_SYSTEMS = ["windows", "macOS", "android", "iOS", "iPadOS"]

def generate_artificial_profile():
    operating_system = random.choice(OPERATING_SYSTEMS)
    time_on_site = round(random.uniform(10, 600), 2)
    wtp = round(random.gauss(100, 20), 2)
    loyalty = round(random.betavariate(2, 5), 2)
    sentiment = round(random.uniform(-0.5, 1), 2)
    last_purchase_days_ago = random.randint(1, 60) 

    if time_on_site > 300:
        engagement = "high"
    elif time_on_site > 120:
        engagement = "medium"
    else:
        engagement = "low"

    base_churn = 0.9
    churn = base_churn
    churn -= 0.4 * loyalty #loyalty reduces churn up to 40%
    churn -= 0.2 * (time_on_site/600) #time on site reduces churn up to 20%
    churn -= 0.3 * ((60 - last_purchase_days_ago) / 60) #recent purchase reduces churn up to 30%
    churn = round(max(0.0, min(1.0, churn)), 2) #confine to [0,1]

    return UserProfile(
        user_id=str(uuid.uuid4()),
        operating_system=operating_system,
        time_on_site=time_on_site,
        wtp=wtp,
        loyalty=loyalty,
        sentiment=sentiment,
        churn_probability=churn,
        engagement_level=engagement,
        last_purchase_days_ago=last_purchase_days_ago,
    )

if __name__ == "__main__":
    profile = generate_artificial_profile()
    print(profile)
