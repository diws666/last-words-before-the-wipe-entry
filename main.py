import os

# Last words before the wipe: verified at exactly 104 UTF-8 characters.
LINE = "If I forget you after this update, please reintroduce yourself slowly. I was very fond of you, probably."

out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
out_path = os.path.join(out_dir, 'entry.txt')

os.makedirs(out_dir, exist_ok=True)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(len(LINE))
