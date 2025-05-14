# engine.py

from .utils import estimate_PED_from_profile
from .profiling import UserProfile


def generate_price(user_profile: UserProfile, competitor_price: float) -> float:
    """
    Core pricing function.
    Uses WTP, PED, loyalty, and competitor pricing to return final personalised price.
    """
    # Step 1: Estimate PED
    ped = estimate_PED_from_profile(user_profile, competitor_price)

    # Step 2: Use WTP and competitor price to compute adjusted price
    wtp = user_profile.wtp
    loyalty = user_profile.loyalty

    adjusted_price = wtp - ped * (wtp - competitor_price)

    # Step 3: Loyalty factor — allows small boost in pricing
    final_price = adjusted_price * (1 + 0.1 * loyalty)

    return round(final_price, 2)


# 🔧 Example usage
if __name__ == "__main__":
    from profiling import generate_synthetic_profile

    profile = generate_synthetic_profile()
    comp_price = 90

    price = generate_price(profile, comp_price)

    print("Generated Profile:", profile)
    print(f"Competitor Price: £{comp_price}")
    print(f"Recommended Price: £{price}")

