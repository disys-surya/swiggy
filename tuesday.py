db = {"customer": {"500": {"ID": "500", "name": "suriyaprakash ", "DOB": "17/03/2002", "Gender": "M", "Age": "20","Zip code": "07895-2789", "Amount ": "1000.20"},"500": {"ID": "2000", "name": "Jim McDonald ", "DOB": "02/02/2020", "Gender": "M", "Age": "25","Zip code": "08136-2324","Amount ": "1500.20"},"20": {"ID": "20", "name": "Jim McDonald", "DOB": "02/02/1999", "Gender": "M", "Age": "25","Zip code": "08124-6565","Amount ": "1500.20"}}}
for i in db.values():
     #print(i)
     for j in i.values():
          for k,l in j.items():
               if k == "Age" and int(l)>25:
                    print(j,l)
               else:
                    print("No Customer Found in the Database")
