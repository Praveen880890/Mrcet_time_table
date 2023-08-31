#pyinstaller --onefile -w ntg.py
import sdef as s
import excel_test as do
import PySimpleGUI as sg
import re
import pyautogui
import time as t
import datetime as dt
my_window=pyautogui.size()
width=my_window[0]
height=my_window[1]
d = dt.date.today()
lo=t.localtime()
weekDays = ("MON", "TUES",
                   "WED", "THUR",
                   "FRI", "SAT",
                   "SUN")
color="cyan"
t1=''
i=0
table_content2=[["","2nd Year"],["IOT","-----","-----"],["CS","-----","-----"],["DSA","-----","-----"],["DSB","-----","-----"],["DSC","-----","-----"]]
table_content3=[["","3rd Year"],["IOT","-----","-----"],["CS","-----","-----"],["DSA","-----","-----"],["DSB","-----","-----"],["DSC","-----","-----"]]
table_content4=[["","4th Year"],["IOT","-----","-----"],["CS","-----","-----"],["DSA","-----","-----"],["DSB","-----","-----"],["DSC","-----","-----"]]
theme_menu=['menu',['random','Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey15', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'PythonPlus', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']]
p="end"
np_11=[]
np_22=[]
np_33=[]
np_44=[]
np_ll=[]
np_55=[]
np_66=[]
np_77=[]
np_e=[]
def t_to_m(hour, minute):
    
    return hour*60+minute
def change(string):
    s=int(string[0:2],10)
    p=int(string[3:5],10)
    r=int(string[6:8],10)
    q=int(string[9:],10)
    return s,p,r,q

def create_window(theme):
    sg.theme(theme)
    layout=[[sg.Image(filename="mrcet.png"),
         sg.Text("    "),
         sg.Text("MRCET   ",font= "Franklin 32",
                 justification="center",right_click_menu=theme_menu)],
        [sg.Image(filename="et .png"),
         sg.Text("Welcome to Department of Emerging Technologies",
                 font= "Franklin 28",justification="center")],
        [sg.Text(t1,key='time',pad=(0,10), font="Franklin 30", justification="center"),
         sg.Text("                "),
         sg.Text("",key='date',font= "Franklin 30",justification="center"),
         sg.Text("            "),
         sg.Text("",key='day',font= "Franklin 30")],
        [sg.Text("CURRENT SESSION",border_width=5,
                 relief="sunken",font= "Franklin 29",justification="center")],
        [sg.Text("    "),
         sg.Text("",key='period',background_color=color,
                                 font= "Franklin 29"),
         sg.Text(" "),
         sg.Text("[--:-- - --:--]",key="timestamp",font="Franklin 30")],
        [sg.Table(headings=["Section","Subject","Teacher"],values=table_content2,enable_events=True,
                  expand_x=True,auto_size_columns=False,hide_vertical_scroll=True,
                  key="-table2-",num_rows=6,
                  row_colors=((0,color),(6,color)),
                  row_height=32,justification="center",sbar_width=20)],
        [sg.Table(headings=["Section","Subject","Teacher"],values=table_content3,
                  expand_x=True,auto_size_columns=False,hide_vertical_scroll=True,
                  key="-table3-",num_rows=6,
                  row_colors=((0,color),(6,color)),
                  row_height=32,justification="center",sbar_width=20,enable_events=True)],
        [sg.Table(headings=["Section","Subject","Teacher"],values=table_content4,
                      expand_x=True, auto_size_columns=False, hide_vertical_scroll=True,
                      key="-table4-", num_rows=6,
                      row_colors=((0, color),(6, color)),
                      row_height=32, justification="center", sbar_width=20,enable_events=True)],
        [sg.Text("Designed by S.Praveen (IoT 4th Year)",font="Helvetica 20")],
        [sg.VPush()]
    ]

    return sg.Window('Period Details', layout,finalize=True,
                     element_justification='center',
                     no_titlebar=False, location=(0, 0),
                     size=(1920,1080),font='Helvetica 22')
window = create_window('Gray Gray Gray')
while True:
    event,values=window.read(timeout=1000)
    t1="".join([str(t.localtime().tm_hour),' : ',str(t.localtime().tm_min)," : ",str(t.localtime().tm_sec)])
    d1="".join([str(d.day)," - ",str(d.month)," - ",str(d.year)])
    w1=weekDays[t.localtime().tm_wday]
    wdict={"MON":"MONDAY","TUES":"TUESDAY","WED":"WEDNESDAY","THUR":"THURSDAY","FRI":"FRIDAY","SAT":"SATURDAY","SUN":"SUNDAY"}
    window['time'].update(t1)
    window['date'].update(d1)
    window['day'].update(wdict[w1])
    if event=="" or event==sg.WIN_CLOSED:
        break
    if event in theme_menu[1]:
        window.close()
        window=create_window(event)    
    if t.localtime().tm_wday!=6:
      cur_t=[(t.localtime().tm_hour),(t.localtime().tm_min)]
      if cur_t[0]>=16:
        p="END"
      else:
        for i in range(len(do.iot4[w1])-1,0,-1):
            period_time=do.iot4["TIME"][i]
            S,P,R,Q=change(period_time)
            if t_to_m(cur_t[0],cur_t[1])>=t_to_m(S,P) and t_to_m(cur_t[0],cur_t[1])<t_to_m(R,Q):
                p = str(i+1)+"TH"
                window["timestamp"].update(period_time)
                table_content = [["", "2nd YEAR"],
                                 [do.year2["class_name"][0], do.iot2[w1][i], do.teach_iot2[do.iot2[w1][i]]],
                                 [do.year2["class_name"][1], do.cs2[w1][i], do.teach_cs2[do.cs2[w1][i]]],
                                 [do.year2["class_name"][2], do.dsa2[w1][i], do.teach_dsa2[do.dsa2[w1][i]]],
                                 [do.year2["class_name"][3], do.dsb2[w1][i], do.teach_dsb2[do.dsb2[w1][i]]],
                                 [do.year2["class_name"][4], do.dsc2[w1][i], do.teach_dsc2[do.dsc2[w1][i]]]
                                 ]
                
                window["-table2-"].update(values=table_content)
        for i in range(len(do.iot4[w1])-1,0,-1):
            period_time=do.iot3["TIME"][i]
            S,P,R,Q=change(period_time)
            if t_to_m(cur_t[0],cur_t[1])>=t_to_m(S,P) and t_to_m(cur_t[0],cur_t[1])<t_to_m(R,Q):
                p = str(i+1)+"TH"
                window["timestamp"].update(period_time)
                table_content = [["", "3rd YEAR"],
                                 [do.year3["class_name"][0], do.iot3[w1][i], do.teach_iot3[do.iot3[w1][i]]],
                                 [do.year3["class_name"][1], do.cs3[w1][i], do.teach_cs3[do.cs3[w1][i]]],
                                 [do.year3["class_name"][2], do.dsa3[w1][i], do.teach_dsa3[do.dsa3[w1][i]]],
                                 [do.year3["class_name"][3], do.dsb3[w1][i], do.teach_dsb3[do.dsb3[w1][i]]],
                                 [do.year3["class_name"][4], do.dsc3[w1][i], do.teach_dsc3[do.dsc3[w1][i]]]
                                 ]
                
                window["-table3-"].update(values=table_content)      
        for i in range(len(do.iot3[w1])-1,0,-1):
            period_time=do.iot4["TIME"][i]
            S,P,R,Q=change(period_time)
            if t_to_m(cur_t[0],cur_t[1])>=t_to_m(S,P) and t_to_m(cur_t[0],cur_t[1])<t_to_m(R,Q):
                p = str(i+1)+"TH"
                window["timestamp"].update(period_time)
                table_content = [["", "4th YEAR"],
                                 [do.year4["class_name"][0], do.iot4[w1][i], do.teach_iot4[do.iot4[w1][i]]],
                                 [do.year4["class_name"][1], do.cs4[w1][i], do.teach_cs4[do.cs4[w1][i]]],
                                 [do.year4["class_name"][2], do.dsa4[w1][i], do.teach_dsa4[do.dsa4[w1][i]]],
                                 [do.year4["class_name"][3], do.dsb4[w1][i], do.teach_dsb4[do.dsb4[w1][i]]],
                                 [do.year4["class_name"][4], do.dsc4[w1][i], do.teach_dsc4[do.dsc4[w1][i]]]
                                 ]
                window["-table4-"].update(values=table_content)
        window['period'].update(p)
      window['period'].update(p)
    window['period'].update(p)
window.close()
