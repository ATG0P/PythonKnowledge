import numpy as nm
rng = nm.random.default_rng()
arr = nm.array([1,2,3,4,5])
rng.shuffle(arr) 
print(arr)

Vegetabes = nm.array(["Brocoli","Carrot","Capcicum","Onions","Okala"])
print(rng.choice(Vegetabes,size=(3,3)))

emojis=nm.array(["✅","😀","🤩"])
print(rng.choice(emojis))