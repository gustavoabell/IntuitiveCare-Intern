import camelot
import shutil
from pathlib import Path

BASE_PATH = "./csvs"

# Quadro 30 e Inici­o do 31
quadro_30, quadro_31 = camelot.read_pdf('input.pdf', pages="79")
quadro_30.to_csv(Path(f'{BASE_PATH}/quadro_30.csv'))

# Finaliza Quadro 31
quadro_31_df = quadro_31.df
for page in range(80, 85):
    tables = camelot.read_pdf('input.pdf', pages=str(page))
    quadro_31_df = quadro_31_df.append(tables[0].df)

quadro_31_df.to_csv(Path(f'{BASE_PATH}/quadro_31.csv'))

# Quadro 32
quadro_32 = camelot.read_pdf('input.pdf', pages="85")[0]
quadro_32.to_csv(Path(f'{BASE_PATH}/quadro_32.csv'))

shutil.make_archive('Teste_Intuitive_Care_Gustavo_Abel', 'zip', BASE_PATH)