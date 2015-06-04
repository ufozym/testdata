import sys

f1=open("D:\\python-code\\testdata\\testdata1.sql","r+",encoding='utf-8')
f2=open("D:\\python-code\\testdata\\testdata2.sql","r+",encoding='utf-8')

#替换sql模板中的？1
def replaceStr(strr,src,li):

    strtemp = strr
    
    for i in li:

        strtemp=strtemp.replace(src,i,1)

    return(strtemp)

#创建表头参数
def creatHeadParams(declist,t):
    x = t%10
    if x == 0 :
        #ID
        declist.append("C224401400000"+str(t+1))
        #I_E_PORT
        declist.append("2201")
        #Merchant_code
        declist.append("1000000001")
        #Merchant_name
        declist.append("test01")
        #Transport_mode
        declist.append("5")
        #Destination_country
        declist.append("110")
        #Destination_port
        declist.append("1003")
    elif x == 1:
        declist.append("C224401400000"+str(t+1))
        declist.append("2202")
        declist.append("1000000002")
        declist.append("test02")
        declist.append("5")
        declist.append("116")
        declist.append("1004")
    elif x == 2:
        declist.append("C224401400000"+str(t+1))
        declist.append("2203")
        declist.append("1000000003")
        declist.append("test03")
        declist.append("5")
        declist.append("132")
        declist.append("1005")
    elif x == 3:
        declist.append("C224401400000"+str(t+1))
        declist.append("2204")
        declist.append("1000000004")
        declist.append("test04")
        declist.append("5")
        declist.append("133")
        declist.append("1006")
    elif x == 4:
        declist.append("C224401400000"+str(t+1))
        declist.append("2205")
        declist.append("1000000005")
        declist.append("test05")
        declist.append("5")
        declist.append("142")
        declist.append("1007")
    elif x == 5:
        declist.append("C224401400000"+str(t+1))
        declist.append("2206")
        declist.append("1000000006")
        declist.append("test06")
        declist.append("5")
        declist.append("303")
        declist.append("1008")
    elif x == 6:
        declist.append("C224401400000"+str(t+1))
        declist.append("2207")
        declist.append("1000000007")
        declist.append("test07")
        declist.append("5")
        declist.append("304")
        declist.append("1009")
    elif x == 7:
        declist.append("C224401400000"+str(t+1))
        declist.append("2208")
        declist.append("1000000008")
        declist.append("test08")
        declist.append("5")
        declist.append("305")
        declist.append("1009")
    elif x == 8:
        declist.append("C224401400000"+str(t+1))
        declist.append("2209")
        declist.append("1000000009")
        declist.append("test09")
        declist.append("5")
        declist.append("307")
        declist.append("1010")
    else:
        declist.append("C224401400000"+str(t+1))
        declist.append("2210")
        declist.append("1000000010")
        declist.append("test10")
        declist.append("5")
        declist.append("312")
        declist.append("1011")
    return(declist)

#创建表体参数
def creatItemsParams(item,t,no):
    x = t%10
    if x == 0 :
        #Declist_id
        item.append("C224401400000"+str(t+1))
        #NO
        item.append(str(no+1))
        #Code_ts
        item.append(str(no+1))
        #Goods_name
        item.append("testgoods"+str(no+1))
        #Goods_Unit
        item.append(str(no+1))
        #Unit_1
        item.append(str(no+1))
        #Currency
        if no == 0:
            item.append("110")
        elif no == 1:
            item.append("116")
        elif no == 2:
            item.append("121")
        elif no == 3:
            item.append("302")
        elif no == 4:
            item.append("129")
        elif no == 5:
            item.append("132")
        elif no == 6:
            item.append("133")
        elif no == 7:
            item.append("136")
        elif no == 8:
            item.append("142")
        else :
            item.append("300")
    elif x == 1:
        #Declist_id
        item.append("C224401400000"+str(t+1))
        #NO
        item.append(str(no+1))
        #Code_ts
        item.append(str(no+1))
        #Goods_name
        item.append("testgoods"+str(no+1))
        #Goods_Unit
        item.append(str(no+1))
        #Unit_1
        item.append(str(no+1))
        #Currency
        if no == 0:
            item.append("110")
        elif no == 1:
            item.append("116")
        elif no == 2:
            item.append("121")
        elif no == 3:
            item.append("302")
        elif no == 4:
            item.append("129")
        elif no == 5:
            item.append("132")
        elif no == 6:
            item.append("133")
        elif no == 7:
            item.append("136")
        elif no == 8:
            item.append("142")
        else :
            item.append("300")
    elif x == 2:
        #Declist_id
        item.append("C224401400000"+str(t+1))
        #NO
        item.append(str(no+1))
        #Code_ts
        item.append(str(no+1))
        #Goods_name
        item.append("testgoods"+str(no+1))
        #Goods_Unit
        item.append(str(no+1))
        #Unit_1
        item.append(str(no+1))
        #Currency
        if no == 0:
            item.append("110")
        elif no == 1:
            item.append("116")
        elif no == 2:
            item.append("121")
        elif no == 3:
            item.append("302")
        elif no == 4:
            item.append("129")
        elif no == 5:
            item.append("132")
        elif no == 6:
            item.append("133")
        elif no == 7:
            item.append("136")
        elif no == 8:
            item.append("142")
        else :
            item.append("300")
    elif x == 3:
        #Declist_id
        item.append("C224401400000"+str(t+1))
        #NO
        item.append(str(no+1))
        #Code_ts
        item.append(str(no+1))
        #Goods_name
        item.append("testgoods"+str(no+1))
        #Goods_Unit
        item.append(str(no+1))
        #Unit_1
        item.append(str(no+1))
        #Currency
        if no == 0:
            item.append("110")
        elif no == 1:
            item.append("116")
        elif no == 2:
            item.append("121")
        elif no == 3:
            item.append("302")
        elif no == 4:
            item.append("129")
        elif no == 5:
            item.append("132")
        elif no == 6:
            item.append("133")
        elif no == 7:
            item.append("136")
        elif no == 8:
            item.append("142")
        else :
            item.append("300")
    elif x == 4:
        #Declist_id
        item.append("C224401400000"+str(t+1))
        #NO
        item.append(str(no+1))
        #Code_ts
        item.append(str(no+1))
        #Goods_name
        item.append("testgoods"+str(no+1))
        #Goods_Unit
        item.append(str(no+1))
        #Unit_1
        item.append(str(no+1))
        #Currency
        if no == 0:
            item.append("110")
        elif no == 1:
            item.append("116")
        elif no == 2:
            item.append("121")
        elif no == 3:
            item.append("302")
        elif no == 4:
            item.append("129")
        elif no == 5:
            item.append("132")
        elif no == 6:
            item.append("133")
        elif no == 7:
            item.append("136")
        elif no == 8:
            item.append("142")
        else :
            item.append("300")
    elif x == 5:
        #Declist_id
        item.append("C224401400000"+str(t+1))
        #NO
        item.append(str(no+1))
        #Code_ts
        item.append(str(no+1))
        #Goods_name
        item.append("testgoods"+str(no+1))
        #Goods_Unit
        item.append(str(no+1))
        #Unit_1
        item.append(str(no+1))
        #Currency
        if no == 0:
            item.append("110")
        elif no == 1:
            item.append("116")
        elif no == 2:
            item.append("121")
        elif no == 3:
            item.append("302")
        elif no == 4:
            item.append("129")
        elif no == 5:
            item.append("132")
        elif no == 6:
            item.append("133")
        elif no == 7:
            item.append("136")
        elif no == 8:
            item.append("142")
        else :
            item.append("300")
    elif x == 6:
        #Declist_id
        item.append("C224401400000"+str(t+1))
        #NO
        item.append(str(no+1))
        #Code_ts
        item.append(str(no+1))
        #Goods_name
        item.append("testgoods"+str(no+1))
        #Goods_Unit
        item.append(str(no+1))
        #Unit_1
        item.append(str(no+1))
        #Currency
        if no == 0:
            item.append("110")
        elif no == 1:
            item.append("116")
        elif no == 2:
            item.append("121")
        elif no == 3:
            item.append("302")
        elif no == 4:
            item.append("129")
        elif no == 5:
            item.append("132")
        elif no == 6:
            item.append("133")
        elif no == 7:
            item.append("136")
        elif no == 8:
            item.append("142")
        else :
            item.append("300")
    elif x == 7:
        #Declist_id
        item.append("C224401400000"+str(t+1))
        #NO
        item.append(str(no+1))
        #Code_ts
        item.append(str(no+1))
        #Goods_name
        item.append("testgoods"+str(no+1))
        #Goods_Unit
        item.append(str(no+1))
        #Unit_1
        item.append(str(no+1))
        #Currency
        if no == 0:
            item.append("110")
        elif no == 1:
            item.append("116")
        elif no == 2:
            item.append("121")
        elif no == 3:
            item.append("302")
        elif no == 4:
            item.append("129")
        elif no == 5:
            item.append("132")
        elif no == 6:
            item.append("133")
        elif no == 7:
            item.append("136")
        elif no == 8:
            item.append("142")
        else :
            item.append("300")
    elif x == 8:
        #Declist_id
        item.append("C224401400000"+str(t+1))
        #NO
        item.append(str(no+1))
        #Code_ts
        item.append(str(no+1))
        #Goods_name
        item.append("testgoods"+str(no+1))
        #Goods_Unit
        item.append(str(no+1))
        #Unit_1
        item.append(str(no+1))
        #Currency
        if no == 0:
            item.append("110")
        elif no == 1:
            item.append("116")
        elif no == 2:
            item.append("121")
        elif no == 3:
            item.append("302")
        elif no == 4:
            item.append("129")
        elif no == 5:
            item.append("132")
        elif no == 6:
            item.append("133")
        elif no == 7:
            item.append("136")
        elif no == 8:
            item.append("142")
        else :
            item.append("300")
    else:
        #Declist_id
        item.append("C224401400000"+str(t+1))
        #NO
        item.append(str(no+1))
        #Code_ts
        item.append(str(no+1))
        #Goods_name
        item.append("testgoods"+str(no+1))
        #Goods_Unit
        item.append(str(no+1))
        #Unit_1
        item.append(str(no+1))
        #Currency
        if no == 0:
            item.append("110")
        elif no == 1:
            item.append("116")
        elif no == 2:
            item.append("121")
        elif no == 3:
            item.append("302")
        elif no == 4:
            item.append("129")
        elif no == 5:
            item.append("132")
        elif no == 6:
            item.append("133")
        elif no == 7:
            item.append("136")
        elif no == 8:
            item.append("142")
        else :
            item.append("300")
    return(item)

declist_queryTempHead="insert into `cbe_declist` (`ID`, `WAYBILL_ID`, `STATUS`, `VOYAGE_NO`,\
`CUSTOMS_CODE`, `CUSTODY_CODE`, `I_E_PORT`, `I_E_DATE`, `OWNER_CODE`, `OWNER_NAME`,\
`OWNER_DISTRICT_CODE`, `MERCHANT_CODE`, `MERCHANT_NAME`, `DECLARER_NODE_CODE`,\
`DECLARER_CODE`, `DECLARER_NAME`, `TRANSPORT_MODE`, `PARENT_BILL_NO`, `BILL_NO`,\
`LICENSE_NO`, `DESTINATION_COUNTRY`, `DESTINATION_PORT`, `TRANSACTION_MODE`, \
`FEE_MARK`, `FEE_CURR`, `FEE_RATE`, `INSUR_MARK`, `INSUR_CURR`, `INSUR_RATE`, \
`OTHER_MARK`, `OTHER_CURR`, `OTHER_RATE`, `WRAP_TYPE`, `PACK_NO`, `GROSS_WEIGHT`,\
`NET_WEIGHT`, `NOTES`, `MERGE_TIME`, `REQ_TIME`, `RSP_TIME`, `RSP_CODE`, `RSP_MSG`,\
`CREATE_USER`, `CREATE_TIME`, `UPDATE_USER`, `UPDATE_TIME`, `DELETE_USER`, \
`DELETE_TIME`, `IS_DELETE`, `MERGE_STATUS`) values"

declist_queryTempList="('?','21','C','ZYO2015060200002','2244',NULL,\
'?','2015-06-02 00:00:00','Z105980011','张发货',NULL,'?',\
'?','CEA0000','3105980001','上海东航快递有限公司','?',\
'ZYD2015060200002','ZFD2015060200002',NULL,'?','?','2',NULL,NULL,\
'0.00000',NULL,NULL,'0.00000',NULL,NULL,'0.00000','3','1','20.00000','10.00000',\
NULL,'2015-06-02 17:35:02','2015-06-02 14:35:50','2015-06-02 14:46:04','B031',\
'放行','DHKJ_Express','2015-06-02 14:35:50','MessageHandler','2015-06-02 17:37:12',\
NULL,NULL,'0',''),"

item_queryTempHead="insert into `cbe_declist_item` (`DECLIST_ID`, `NO`, \
`CODE_TS`, `GOODS_NAME`, `GOODS_MODEL`, `GOODS_QTY`, `GOODS_UNIT`, `QTY_1`, \
`UNIT_1`, `QTY_2`, `UNIT_2`, `UNIT_PRICE`, `TOTAL_PRICE`, `CURRENCY`, `RMB_PRICE`,\
`USD_PRICE`, `USE_TO`, `GROSS_WEIGHT`, `NET_WEIGHT`, `DUTY_MODE`, `NOTES`, \
`MERGE_TO`) values"

item_queryTempList="('?','?','?','?','袋装',\
'9.00000','?','1.00000','?','2.00000','035','10.00000','90.00000','?',\
NULL,NULL,NULL,'4.50000','4.00000','1',NULL,NULL),"

declist=[]
item=[]
declist_sql=''
item_sql=''

for i in range(0,20):
    print(i)
    
    creatHeadParams(declist,i)
    #print(declist)
    declistAll = replaceStr(declist_queryTempList,"?",declist)
    #print(declistAll)
    declist_sql =  declist_sql + declistAll
    declist=[]
    for j in range(0,2):
        creatItemsParams(item,i,j)
        #print(item)
        itemAll = replaceStr(item_queryTempList,"?",item)
        #print(itemAll)
        item_sql = item_sql + itemAll
        item=[]

declist_sql_all = declist_queryTempHead + declist_sql
declist_sql_all = declist_sql_all[0:len(declist_sql_all)-1] + ";"
item_sql_all = item_queryTempHead + item_sql
item_sql_all = item_sql_all[0:len(item_sql_all)-1] + ";"

#print(declist_sql_all)
#print(item_sql_all)

f1.write(declist_sql_all)
f2.write(item_sql_all)

f1.close()
f2.close()
    

