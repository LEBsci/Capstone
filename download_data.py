import os

i2m = list(zip(range(1,13), ['Gener','Febrer','Marc','Abril','Maig','Juny','Juliol','Agost','Setembre','Octubre','Novembre','Desembre']))
for year in range(2024, 2019, -1):
     for month, month_name in i2m:     
         if (month > 5) and (year>2023): continue 
         os.system(f"wget 'https://opendata-ajuntament.barcelona.cat/resources/bcn/BicingBCN/{year}_{month:02d}_{month_name}_BicingNou_ESTACIONS.7z'")
         os.system(f"7z x '{year}_{month:02d}_{month_name}_BicingNou_ESTACIONS.7z' -o./data")
         os.system(f"rm '{year}_{month:02d}_{month_name}_BicingNou_ESTACIONS.7z'")