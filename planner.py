import pandas as pd

def load_vendors(path='vendors.csv'):
    return pd.read_csv(path)

def recommend_vendors(vendors, event_type, budget, city, vibe):
    vendors = vendors.copy()
    relevant = vendors[vendors['city'].str.lower() == city.lower()]

    # Score = cost-fit + rating + vibe-match
    relevant['score'] = (
        0.5 * (1 - abs(relevant['cost'] - (budget / 5)) / budget) +  # normalize cost diff
        0.3 * (relevant['rating'] / 5) +                             # rating weight
        0.2 * (relevant['vibe'].str.lower() == vibe.lower()).astype(int)
    )

    return relevant.sort_values(by='score', ascending=False)

def suggest_timeline(event_type):
    timelines = {
        "wedding": [
            "Book Venue - 6 months before",
            "Confirm Caterers - 3 months before",
            "Send Invitations - 1 month before",
            "Finalize Outfits - 2 months before",
            "Hire Photographer - 3 months before"
        ],
        "birthday": [
            "Book Venue - 1 month before",
            "Order Cake - 2 weeks before",
            "Send Invites - 1 week before",
            "Decor & Lights - 3 days before"
        ],
        "corporate": [
            "Book Venue - 2 months before",
            "Arrange Catering - 3 weeks before",
            "Invite Speakers - 1 month before",
            "Setup A/V - 2 days before"
        ]
    }
    return timelines.get(event_type.lower(), [])
