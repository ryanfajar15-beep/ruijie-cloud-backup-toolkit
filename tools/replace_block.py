from pathlib import Path


file = Path(
    "development/api/render_client.py"
)

lines = file.read_text().splitlines()


start = 100
end = 150


new_block = """
# kode baru taruh di sini
""".splitlines()


result = (
    lines[:start-1]
    + new_block
    + lines[end:]
)


file.write_text(
    "\n".join(result) + "\n"
)

print("Replaced")
