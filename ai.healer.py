import re

class AIHealer:
    """
    Simulates an AI self-healing layer that detects broken selectors
    and dynamically adjusts parsing strategies when HTML structures change.
    """
    def __init__(self):
        print("[AI Healer] Initialized and monitoring scraper health...")

    def heal_selector(self, html_content, failed_selector):
        print(f"[AI Healer warning] Selector '{failed_selector}' failed or returned empty results.")
        print("[AI Healer action] Analyzing DOM structure for fallback patterns...")
        
        # Fallback heuristic: Try to find tags containing potential data elements
        if "price" in failed_selector.lower():
            # Look for common price patterns like $XX.XX using regex fallback
            prices = re.findall(r'\$\d+(?:\.\d{2})?', html_content)
            if prices:
                print(f"[AI Healer success] Healed! Recovered prices using fallback regex: {prices[:3]}")
                return prices
        elif "title" in failed_selector.lower() or "heading" in failed_selector.lower():
            # Fallback to headings if titles fail
            matches = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', html_content, re.IGNORECASE)
            if matches:
                cleaned = [re.sub(r'<[^>]+>', '', m).strip() for m in matches]
                print(f"[AI Healer success] Healed! Recovered headings using fallback regex: {cleaned[:3]}")
                return cleaned

        print("[AI Healer error] Could not heal selector automatically.")
        return []
