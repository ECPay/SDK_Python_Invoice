#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
發票查詢／查詢發票明細
* 特店可使用此API查詢已開立發票資訊，綠界會以回傳參數方式回覆該張發票資料。此方式可協助營業人將查詢發票機制整合至營業人網站，提供買受人可於營業人網站快速查詢。
如有多筆大量查詢需求，建議使用查詢特定多筆發票。
情境二：以發票號碼[InvoiceNo]與發票開立日期[InvoiceDate]做查詢
'''

# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'GET_ISSUE2'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/GetIssue'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['InvoiceNo'] = 'IS80056018'# 發票號碼
ecpay_invoice.Send['InvoiceDate'] = '2023-09-25'# 發票開立日期

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()
# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
