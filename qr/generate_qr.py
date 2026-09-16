import qrcode
import os
import sys
import json
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

if len(sys.argv) != 2:
    print("Usage: python generate_qr.py <package_id>")
    sys.exit(1)

package_id = sys.argv[1]

BASE_URL = "https://bald-knowing-lee-shaped.trycloudflare.com"

verification_url = f"{BASE_URL}/verify/{package_id}"

try:
    with urlopen(verification_url) as response:
        data = json.loads(response.read().decode())

except HTTPError as e:
    print(f"Package verification failed: HTTP {e.code}")
    print("QR was not generated.")
    sys.exit(1)

except URLError:
    print("Could not connect to HoneyChain.")
    print("Make sure FastAPI and Cloudflare Tunnel are running.")
    sys.exit(1)

if not data.get("seal_valid"):
    print("Seal verification failed.")
    print("QR was not generated.")
    sys.exit(1)

output_dir = "generated"
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(
    output_dir,
    f"{package_id}.png"
)

qr = qrcode.make(verification_url)
qr.save(output_file)

print("QR generated successfully")
print("Package ID:", package_id)
print("Seal status: VALID")
print("Verification URL:", verification_url)
print("Saved to:", output_file)