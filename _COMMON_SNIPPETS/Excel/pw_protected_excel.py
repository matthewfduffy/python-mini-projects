# pip install msoffcrypto-tool

import pandas as pd
import io
import msoffcrypto

protected_excel = 'excel.xlsx'
unprotected_excel_content = io.BytesIO()
with open(protected_excel, 'rb') as f:
    msoffcryptoobj = msoffcrypto.OfficeFile(f)
    msoffcryptoobj.load_key(password="enter password")
    unprotected_excel_content = io.BytesIO()
    msoffcryptoobj.decrypt(unprotected_excel_content)

df = pd.read_excel(unprotected_excel_content)

df