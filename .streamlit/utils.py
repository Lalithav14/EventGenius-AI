def calculate_vibe_alignment(vendor_vibe, user_vibe):
    if vendor_vibe.lower() == user_vibe.lower():
        return 1
    return 0
