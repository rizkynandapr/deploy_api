from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

#http://127.0.0.1:8000/names/nanda

@app.get("/names/{variabel_nama}")
def read_name(variabel_nama):
  return {"name":variabel_nama,
          "message":f"Hello, my name is {variabel_nama}"}


data = []

@app.get("/carts")
def read_carts():
    return {"carts": data, "length": len(data)}

@app.post("/carts")
def add_carts(added_item: dict):
   id = len(data) + 1
   added_item['id'] = id
   data.append(added_item)

   return{'massage': f"Data berhasil ditambahkan"}


    