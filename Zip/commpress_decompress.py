import zipfile
import shutil

"""
# By dfault -> No compress --> Add argument
zip_file = zipfile.ZipFile("excel_file.zip", "w", zipfile.ZIP_DEFLATED)
zip_file.write("octobre.xlsx")
zip_file.write("novembre.xlsx")
zip_file.write("decembre.xlsx")

zip_file.close()"""

# shutil.make_archive("excel_files", "zip", "excel_file")

shutil.unpack_archive("excel_file.zip", "extract_file")