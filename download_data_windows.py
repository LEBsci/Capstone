import os
import py7zr

# Create the data directory if it doesn't exist
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

i2m = list(zip(range(1, 13), ['Gener', 'Febrer', 'Marc', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Setembre', 'Octubre', 'Novembre', 'Desembre']))
for year in range(2024, 2019, -1):
    for month, month_name in i2m:
        if (month > 5) and (year > 2023):
            continue
        file_name = f"{year}_{month:02d}_{month_name}_BicingNou_ESTACIONS.7z"
        file_path = os.path.join(data_dir, file_name)
        os.system(f'curl -L -o "{file_path}" "https://opendata-ajuntament.barcelona.cat/resources/bcn/BicingBCN/{file_name}"')
        
        # Extract the 7z file
        with py7zr.SevenZipFile(file_path, mode='r') as archive:
            archive.extractall(path=data_dir)
        
        # Delete the 7z file
        os.remove(file_path)