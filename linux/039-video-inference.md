# nemotron3:33b video inference pipeline


ffprobe -v quiet -print_format json -show_streams ~/Videos/Toll-Plaza.mp4 | grep -E "width|height|duration|r_frame_rate"
-----
ffmpeg -i ~/Videos/Toll-Plaza.mp4 -vf fps=1 ~/toll_analysis/frames/frame_%04d.jpg -q:v 2
-----
cd ~/toll_analysis

python3 - <<'EOF'
import requests, base64, time

with open("frames/frame_0001.jpg", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode()

start = time.time()

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "nemotron3:33b",
    "prompt": "This is a frame from a toll plaza surveillance camera. Describe what you see: vehicles, lane usage, people, and any activity at the toll booths.",
    "images": [img_b64],
    "stream": False
})

elapsed = time.time() - start
data = response.json()

print("=== RESPONSE ===")
print(data.get("response", "No response"))
print(f"\n=== TIME: {elapsed:.1f} seconds ===")
EOF
-----
cd ~/toll_analysis
-----
nano ~/toll_analysis/analyze_toll.py
-----
import requests, base64, time, json, os
from datetime import datetime, timedelta

FRAMES_DIR = "/home/dell/toll_analysis/frames"
OUTPUT_JSON = "/home/dell/toll_analysis/results.json"
OUTPUT_TXT  = "/home/dell/toll_analysis/results.txt"
MODEL       = "nemotron3:33b"
PROMPT      = (
    "This is a frame from a toll plaza surveillance camera. "
    "Describe what you see: vehicles (type, color, count), "
    "lane usage, people visible, and any activity at the toll booths."
)

frames = sorted([f for f in os.listdir(FRAMES_DIR) if f.endswith(".jpg")])
total  = len(frames)
results = []

# Resume support — skip already done frames
done_frames = set()
if os.path.exists(OUTPUT_JSON):
    with open(OUTPUT_JSON) as f:
        results = json.load(f)
    done_frames = {r["frame"] for r in results}
    print(f"Resuming — {len(done_frames)} frames already done.\n")

print(f"Total frames: {total}")
print(f"Remaining   : {total - len(done_frames)}")
print(f"Est. time   : {str(timedelta(seconds=(total - len(done_frames)) * 32)).split('.')[0]}")
print("="*50)

with open(OUTPUT_TXT, "a") as txt_out:
    for i, fname in enumerate(frames, 1):
        if fname in done_frames:
            continue

        frame_path = os.path.join(FRAMES_DIR, fname)
        second     = int(fname.replace("frame_","").replace(".jpg",""))
        timestamp  = str(timedelta(seconds=second - 1))

        with open(frame_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode()

        try:
            start = time.time()
            resp  = requests.post("http://localhost:11434/api/generate", json={
                "model":  MODEL,
                "prompt": PROMPT,
                "images": [img_b64],
                "stream": False
            }, timeout=120)
            elapsed = time.time() - start
            description = resp.json().get("response", "No response")

        except Exception as e:
            description = f"ERROR: {e}"
            elapsed = 0

        # Calculate ETA
        remaining = total - i
        eta = str(timedelta(seconds=int(remaining * elapsed))).split(".")[0]

        # Save result
        entry = {
            "frame":       fname,
            "timestamp":   timestamp,
            "description": description,
            "time_sec":    round(elapsed, 1)
        }
        results.append(entry)

        # Write JSON after every frame (safe resume)
        with open(OUTPUT_JSON, "w") as f:
            json.dump(results, f, indent=2)

        # Write to text file
        txt_out.write(f"\n[{timestamp}] {fname}\n{description}\n{'-'*60}\n")
        txt_out.flush()

        # Progress
        pct = (i / total) * 100
        print(f"[{i:3}/{total}] {fname} | {timestamp} | {elapsed:.1f}s | ETA: {eta} | {pct:.1f}%")

print("\n✅ Done! Results saved to:")
print(f"   {OUTPUT_JSON}")
print(f"   {OUTPUT_TXT}")
-----
cd ~/toll_analysis
python3 analyze_toll.py
-----

