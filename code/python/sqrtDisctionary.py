import math

data = {
    "x" : int(input("Masukkan x: ")),
    "y": int(input("Masukkan y: ")),
    "hasil" : None,
}

data["hasil"] = math.sqrt(data["x"]) + math.sqrt(data["y"])

print(data)