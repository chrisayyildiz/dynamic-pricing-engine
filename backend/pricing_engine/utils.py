# utils.py

def calculate_PED(old_price, new_price, old_quantity, new_quantity):
    """
    Calculate Price Elasticity of Demand from observed data.
    PED = (% Change in Quantity) / (% Change in Price)
    """
    try:
        pct_change_quantity = (new_quantity - old_quantity) / old_quantity
        pct_change_price = (new_price - old_price) / old_price
        return round(pct_change_quantity / pct_change_price, 2)
    except ZeroDivisionError:
        return 0


def linear_demand(price, base_quantity=100, slope=-1.2):
    """
    Linear demand function:
    Q = base_quantity + slope * price
    Returns quantity demanded at a given price.
    """
    return max(0, base_quantity + slope * price)


def estimate_PED_from_profile(user_profile, competitor_price):
    """
    Estimate PED based on:
    - Loyalty: lowers PED
    - Price difference between WTP and competitor: increases PED
    - If WTP < competitor price: spike PED to reflect extreme sensitivity
    """
    wtp = user_profile.wtp
    loyalty = user_profile.loyalty

    # Base elasticity
    base_ped = 1.5

    # Normalised difference between WTP and competitor price
    diff = (wtp - competitor_price) / max(wtp, 1)
    loyalty_factor = (1 - loyalty)  # lower loyalty = more elastic

    # Price unfairness spike: if we’re more expensive than competitor, spike PED
    if wtp < competitor_price:
        penalty = (competitor_price - wtp) / max(wtp, 1)
        spike = 4.0 * loyalty_factor * penalty
    else:
        spike = 0

    ped = base_ped + loyalty_factor * abs(diff) * 2 + spike
    return round(ped, 2)
