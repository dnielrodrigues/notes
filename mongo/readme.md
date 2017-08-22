# Console Commands

Create or select database: `use db_name`

Show databases: `show dbs`

Insert Sample: `db_name.product.insert({'name':'Fixed Bike'});`

Show Collections (tables): `show collections`

Delete database:
> Select the target db and run: `db.dropDatabase()`

Delete Collection (tables): `db.product.drop()`

# Remember

* O mongo trabalha com conceito de "create when insert". Exemplo: ele cria um banco quando inserimos algo em um banco que no existe. Logo não existe um comando "create" em muitos casos. Apenas o "insert" ja resolve.

...

# Queries

* Filtrar na arvore:
```
db.my_collection.find({
    "my_prop":"my_value",
    "my_prop.my_sub_prop":"my_value",
    "my_parent_prop.my_parent_prop.my_prop":"my_value"
})
```
