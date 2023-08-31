import pandas as pd


############################# 4TH YEAR SHEET #############################

############################# CLASS NAME SHEET ###########################
year4=pd.read_excel("tables.xlsx",sheet_name="year4_class_name")
year3=pd.read_excel("tables.xlsx",sheet_name="year3_class_name")
year2=pd.read_excel("tables.xlsx",sheet_name="year2_class_name")
#### IOT SHEET ####
iot4=pd.read_excel("tables.xlsx",sheet_name="iot4")
tiot4=pd.read_excel("tables.xlsx",sheet_name="teach_iot4")
teach_iot4={}
i=0
while i<=11:
  try:
    teach_iot4[tiot4["CODE"][i]]=tiot4["TEACHER"][i]
    i += 1
  except:
    break
  
#### CS SHEET ####

cs4=pd.read_excel("tables.xlsx",sheet_name="cs4")
tcs4=pd.read_excel("tables.xlsx",sheet_name="teach_cs4")
teach_cs4={}
i=0
while i<=11:
  try:
    teach_cs4[tcs4["CODE"][i]]=tcs4["TEACHER"][i]
    i += 1
  except:
    break
#### DSA SHEET ####

dsa4=pd.read_excel("tables.xlsx",sheet_name="dsa4")
tdsa4=pd.read_excel("tables.xlsx",sheet_name="teach_dsa4")
teach_dsa4={}
i=0
while i<=11:
  try:
    teach_dsa4[tdsa4["CODE"][i]]=tdsa4["TEACHER"][i]
    i += 1
  except:
    break

#### DSB SHEET ####

dsb4=pd.read_excel("tables.xlsx",sheet_name="dsb4")
tdsb4=pd.read_excel("tables.xlsx",sheet_name="teach_dsb4")
teach_dsb4={}
i=0
while i<=11:
  try:
    teach_dsb4[tdsb4["CODE"][i]]=tdsb4["TEACHER"][i]
    i += 1
  except:
    break

#### DSC SHEET ####

dsc4=pd.read_excel("tables.xlsx",sheet_name="dsc4")
tdsc4=pd.read_excel("tables.xlsx",sheet_name="teach_dsc4")
teach_dsc4={}
i=0
while i<=11:
  try:
    teach_dsc4[tdsc4["CODE"][i]]=tdsc4["TEACHER"][i]
    i += 1
  except:
    break


############################# 3RD YEAR SHEET #############################

#### IOT SHEET ####

iot3=pd.read_excel("tables.xlsx",sheet_name="iot3")
tiot3=pd.read_excel("tables.xlsx",sheet_name="teach_iot3")
teach_iot3={}
i=0
while i<=11:
  try:
    teach_iot3[tiot3["CODE"][i]]=tiot3["TEACHER"][i]
    i += 1
  except:
    break
  
#### CS SHEET ####

cs3=pd.read_excel("tables.xlsx",sheet_name="cs3")
tcs3=pd.read_excel("tables.xlsx",sheet_name="teach_cs3")
teach_cs3={}
i=0
while i<=11:
  try:
    teach_cs3[tcs3["CODE"][i]]=tcs3["TEACHER"][i]
    i += 1
  except:
    break
#### DSA SHEET ####

dsa3=pd.read_excel("tables.xlsx",sheet_name="dsa3")
tdsa3=pd.read_excel("tables.xlsx",sheet_name="teach_dsa3")
teach_dsa3={}
i=0
while i<=11:
  try:
    teach_dsa3[tdsa3["CODE"][i]]=tdsa3["TEACHER"][i]
    i += 1
  except:
    break

#### DSB SHEET ####

dsb3=pd.read_excel("tables.xlsx",sheet_name="dsb3")
tdsb3=pd.read_excel("tables.xlsx",sheet_name="teach_dsb3")
teach_dsb3={}
i=0
while i<=11:
  try:
    teach_dsb3[tdsb3["CODE"][i]]=tdsb3["TEACHER"][i]
    i += 1
  except:
    break

#### DSC SHEET ####

dsc3=pd.read_excel("tables.xlsx",sheet_name="dsc3")
tdsc3=pd.read_excel("tables.xlsx",sheet_name="teach_dsc3")
teach_dsc3={}
i=0
while i<=11:
  try:
    teach_dsc3[tdsc3["CODE"][i]]=tdsc3["TEACHER"][i]
    i += 1
  except:
    break


############################# 2ND YEAR SHEET #############################

#### IOT SHEET ####

iot2=pd.read_excel("tables.xlsx",sheet_name="iot2")
tiot2=pd.read_excel("tables.xlsx",sheet_name="teach_iot2")
teach_iot2={}
i=0
while i<=11:
  try:
    teach_iot2[tiot2["CODE"][i]]=tiot2["TEACHER"][i]
    i += 1
  except:
    break
  
#### CS SHEET ####

cs2=pd.read_excel("tables.xlsx",sheet_name="cs2")
tcs2=pd.read_excel("tables.xlsx",sheet_name="teach_cs2")
teach_cs2={}
i=0
while i<=11:
  try:
    teach_cs2[tcs2["CODE"][i]]=tcs2["TEACHER"][i]
    i += 1
  except:
    break




#### DSA SHEET ####

dsa2=pd.read_excel("tables.xlsx",sheet_name="dsa2")
tdsa2=pd.read_excel("tables.xlsx",sheet_name="teach_dsa2")
teach_dsa2={}
i=0
while i<=11:
  try:
    teach_dsa2[tdsa2["CODE"][i]]=tdsa2["TEACHER"][i]
    i += 1
  except:
    break

#### DSB SHEET ####

dsb2=pd.read_excel("tables.xlsx",sheet_name="dsb2")
tdsb2=pd.read_excel("tables.xlsx",sheet_name="teach_dsb2")
teach_dsb2={}
i=0
while i<=11:
  try:
    teach_dsb2[tdsb2["CODE"][i]]=tdsb2["TEACHER"][i]
    i += 1
  except:
    break

#### DSC SHEET ####

dsc2=pd.read_excel("tables.xlsx",sheet_name="dsc2")
tdsc2=pd.read_excel("tables.xlsx",sheet_name="teach_dsc2")
teach_dsc2={}
i=0
while i<=11:
  try:
    teach_dsc2[tdsc2["CODE"][i]]=tdsc2["TEACHER"][i]
    i += 1
  except:
    break
