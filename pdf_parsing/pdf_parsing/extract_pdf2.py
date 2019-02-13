import pathlib
import tabula

# tabula.convert_into("CM-SP-R-PHY-I10-180509.pdf", "output.csv", output_format="csv")
current_dir = pathlib.Path(__file__).parent
pdf_path = f"{current_dir}/CM-SP-R-PHY-I10-180509.pdf"
print(pdf_path)
tabula.convert_into(pdf_path, guess=True, encoding='utf-8', pages='158',
                    output_path="output.csv", output_format="csv")


