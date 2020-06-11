from utils.csvFinder import csvFinder

CSV = csvFinder(csvPath="./CSVs/รายการบ้านสองชั้น.csv")
# res = CSV.find_row(val="ทราบครอบสันโค้ง" , limit=5)

res_value = CSV.find_value(val="อยากทราบเหล็กกลม",col_to_find="จำนวนเท่าไหร่",limit=1)
print(res_value)