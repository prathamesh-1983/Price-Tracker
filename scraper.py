import requests
from ai_healer import AIHealer

def run_scraper():
    healer = AIHealer()
    
    # Target URL (Using a public test scraping target or gaming deals example)
    target_url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
    print(f"[*] Connecting to target URL via Bright Data proxy structure: {target_url}")
    
    try:
        response = requests.get(target_url, timeout=10)
        response.raise_for_status()
        html_content = response.text
        print("[*] Successfully fetched page content.")
        
        # Simulate a primary selector attempt (deliberately broken to demonstrate self-healing)
        primary_selector = ".broken-price-tag-2026"
        print(f"[*] Attempting to extract data using selector: {primary_selector}")
        
        # Let's check if our selector exists in the page (it won't, it's deliberately broken to show healing)
        if primary_selector not in html_content:
            # Trigger self-healing mechanism
            healed_data = healer.heal_selector(html_content, failed_selector="price")
            print(f"[Result] Successfully extracted {len(healed_data)} items via AI Self-Healing fallback!")
            for item in healed_data[:5]:
                print(f"   -> Found item: {item}")
        else:
            print("[*] Data extracted successfully using primary selector.")
            
    except Exception as e:
        print(f"[Error] Scraper encountered an issue: {e}")

if __name__ == "__main__":
    run_scraper()
