from pathlib import Path

print("Current:", Path.cwd())
print("Data:", Path("data"))
print("Raw:", Path("data") / "raw")
print("CSV:", Path("data") / "raw" / "tesla.csv")

print(Path(__file__))
print(Path(__file__).resolve())
print(Path(__file__).resolve().parent)
print(Path(__file__).resolve().parents[1])
print(Path(__file__).resolve().parents[2])


