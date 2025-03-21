import os
import concurrent.futures

def process_file(year, month, month_name):
    url = f"https://opendata-ajuntament.barcelona.cat/resources/bcn/BicingBCN/{year}_{month:02d}_{month_name}_BicingNou_ESTACIONS.7z"
    filename = f"{year}_{month:02d}_{month_name}_BicingNou_ESTACIONS.7z"
    os.system(f"wget '{url}'")
    os.system(f"7z x '{filename}' -o./data")
    os.system(f"rm '{filename}'")

i2m = list(zip(range(1, 13), ['Gener', 'Febrer', 'Marc', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Setembre', 'Octubre', 'Novembre', 'Desembre']))

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for year in range(2024, 2019, -1):
        for month, month_name in i2m:
            if (month > 5) and (year > 2023):
                continue
            futures.append(executor.submit(process_file, year, month, month_name))

    # Wait for all futures to complete
    concurrent.futures.wait(futures)
print("All files have been processed.")