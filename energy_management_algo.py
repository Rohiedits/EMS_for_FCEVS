# import streamlit as st
# import plotly.graph_objects as go

# st.set_page_config(page_title="Hybrid Energy Storage System", layout="wide")

# st.title("Hybrid Energy Storage System")
# st.subheader("Energy Management Algorithm Dashboard")

# ems = st.sidebar.radio("Select EMS Type", ["Rule-Based EMS", "Fuzzy Logic EMS"])

# def show_output(mode, decision, fc, bat, uc,
#                 battery_soc=70, uc_soc=60, hydrogen=80,
#                 battery_temp=35, fc_temp=40, dc_voltage=350):
#     c1,c2=st.columns(2)
#     c1.metric("Operating Mode",mode)
#     c2.metric("Decision",decision)

#     fig=go.Figure(data=[go.Pie(
#         labels=["Fuel Cell","Battery","Ultracapacitor"],
#         values=[fc,bat,uc],
#         hole=0.45)])
#     st.plotly_chart(fig,use_container_width=True)

#     st.subheader("Battery SOC")
#     st.progress(battery_soc/100)
#     st.write(f"{battery_soc}%")

#     st.subheader("Ultracapacitor SOC")
#     st.progress(uc_soc/100)
#     st.write(f"{uc_soc}%")

#     st.subheader("Hydrogen Level")
#     st.progress(hydrogen/100)
#     st.write(f"{hydrogen}%")

#     st.subheader("System Status")

#     if battery_temp<45:
#         st.success("Battery Temperature Normal")
#     else:
#         st.warning("Battery Temperature High")

#     if fc_temp<70:
#         st.success("Fuel Cell Temperature Normal")
#     else:
#         st.warning("Fuel Cell Temperature High")

#     if 300<=dc_voltage<=400:
#         st.success("DC Bus Voltage Stable")
#     else:
#         st.error("DC Bus Voltage Out of Range")


# if ems=="Rule-Based EMS":

#     st.sidebar.header("Numeric Inputs")

#     with st.sidebar.form("rule"):
#         speed=st.slider("Vehicle Speed",0,150,50)
#         acceleration=st.slider("Acceleration",-5.0,5.0,0.0)
#         power=st.slider("Motor Power Demand",0,120,40)
#         battery_soc=st.slider("Battery SOC",0,100,70)
#         uc_soc=st.slider("UC SOC",0,100,60)
#         fuel_cell_power=st.slider("Fuel Cell Power",0,120,60)
#         fuel_efficiency=st.slider("Fuel Cell Efficiency",50,100,90)
#         battery_temp=st.slider("Battery Temperature",20,80,35)
#         fc_temp=st.slider("Fuel Cell Temperature",20,90,40)
#         hydrogen=st.slider("Hydrogen Level",0,100,80)
#         dc_voltage=st.slider("DC Bus Voltage",250,450,350)
#         regen=st.selectbox("Regenerative Braking",["No","Yes"])
#         road=st.selectbox("Road",["Flat","Uphill","Downhill"])
#         run=st.form_submit_button("Run")

#     if run:
#         mode=""
#         decision=""
#         fc=bat=uc=0

#         if hydrogen<15:
#             mode="Emergency"
#             decision="Battery + UC supply load"
#             fc,bat,uc=0,60,40

#         elif regen=="Yes":
#             mode="Regenerative Braking"
#             if uc_soc<95:
#                 decision="Charge UC"
#                 fc,bat,uc=0,20,80
#             else:
#                 decision="Charge Battery"
#                 fc,bat,uc=0,80,20

#         else:
#             if power<=fuel_cell_power:
#                 mode="Mode 1"
#                 decision="Fuel Cell supplies load"
#                 fc=100
#             else:
#                 if battery_soc>60:
#                     mode="Mode 6"
#                     decision="Fuel Cell + Battery"
#                     fc,bat=70,30
#                 elif uc_soc>40:
#                     mode="Mode 7"
#                     decision="Fuel Cell + UC"
#                     fc,uc=65,35
#                 else:
#                     mode="Mode 9"
#                     decision="Fuel Cell Maximum"
#                     fc=100

#             if acceleration>2:
#                 mode="Peak Acceleration"
#                 decision="UC Assists"
#                 fc,bat,uc=60,20,20

#             if road=="Uphill":
#                 mode="Hill Climb"
#                 decision="Fuel Cell + Battery + UC"
#                 fc,bat,uc=50,30,20

#         show_output(mode,decision,fc,bat,uc,battery_soc,uc_soc,hydrogen,battery_temp,fc_temp,dc_voltage)

# else:

#     st.sidebar.header("Linguistic Inputs")

#     levels=["Low","Medium","High"]

#     with st.sidebar.form("fuzzy"):
#         speed=st.selectbox("Vehicle Speed",levels)
#         acceleration=st.selectbox("Acceleration",levels)
#         power=st.selectbox("Power Demand",levels)
#         battery_soc=st.selectbox("Battery SOC",levels)
#         uc_soc=st.selectbox("UC SOC",levels)
#         fuel_cell=st.selectbox("Fuel Cell Power",levels)
#         fuel_eff=st.selectbox("Fuel Cell Efficiency",levels)
#         battery_temp=st.selectbox("Battery Temperature",levels)
#         fc_temp=st.selectbox("Fuel Cell Temperature",levels)
#         hydrogen=st.selectbox("Hydrogen Level",levels)
#         voltage=st.selectbox("DC Bus Voltage",["Low","Normal","High"])
#         regen=st.selectbox("Regenerative Braking",["No","Yes"])
#         road=st.selectbox("Road",["Flat","Uphill","Downhill"])
#         run=st.form_submit_button("Run Fuzzy EMS")

#     if run:

#         mode="Fuzzy Logic EMS"
#         decision=""
#         fc=bat=uc=0

#         if hydrogen=="Low":
#             decision="Hydrogen Low → Battery + UC"
#             fc,bat,uc=10,50,40

#         elif regen=="Yes":
#             decision="Regenerative Braking → Charge UC"
#             fc,bat,uc=0,20,80

#         elif battery_soc=="Low" and power=="High":
#             decision="Fuel Cell HIGH, Battery MEDIUM"
#             fc,bat,uc=70,30,0

#         elif battery_soc=="High" and power=="Low":
#             decision="Battery Supplies More Power"
#             fc,bat,uc=40,60,0

#         elif acceleration=="High":
#             decision="UC assists acceleration"
#             fc,bat,uc=60,20,20

#         elif road=="Uphill":
#             decision="All Sources Active"
#             fc,bat,uc=50,30,20

#         elif battery_temp=="High":
#             decision="Reduce Battery Usage"
#             fc,bat,uc=80,10,10

#         elif fc_temp=="High":
#             decision="Reduce Fuel Cell Usage"
#             fc,bat,uc=40,40,20

#         else:
#             decision="Balanced Power Sharing"
#             fc,bat,uc=60,25,15

#         soc_num={"Low":30,"Medium":60,"High":90}
#         temp_num={"Low":30,"Medium":45,"High":70}
#         volt_num={"Low":280,"Normal":350,"High":430}

#         show_output(mode,decision,fc,bat,uc,
#                     soc_num[battery_soc],
#                     soc_num[uc_soc],
#                     soc_num[hydrogen],
#                     temp_num[battery_temp],
#                     temp_num[fc_temp],
#                     volt_num[voltage])
#     else:
#         st.info("Choose an EMS type.")





import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

st.set_page_config(page_title="FCEV EMS Simulator", layout="wide")
st.title("Fuel Cell Electric Vehicle EMS Simulator")

speed_file=st.sidebar.file_uploader("UDDS Drive Cycle CSV",type="csv")
current_file=st.sidebar.file_uploader("UDDS Current Profile CSV",type="csv")

battery_temp=st.sidebar.slider("Battery Temp",0,70,30)
fuel_temp=st.sidebar.slider("Fuel Cell Temp",20,100,65)
battery_soc=st.sidebar.slider("Battery SOC",0,100,80)
uc_soc=st.sidebar.slider("UC SOC",0,100,90)
delay=st.sidebar.slider("Delay",0.0,1.0,0.1)

def ems(speed,current):
    if speed==0 and abs(current)<1:return "Idle","Aux Battery"
    if current<0:return "Regen","Charge UC+Battery"
    if battery_temp>45:return "Protect","Fuel Cell"
    if fuel_temp>80:return "Protect","Battery"
    if battery_soc<30:return "Charge","Fuel Cell"
    if speed<20:
        return ("Low Speed","Battery") if current<20 else ("Accel","Battery+UC")
    if speed<=40:return "Cruise","Fuel Cell"
    return ("High Speed","Fuel Cell+Battery") if current>60 else ("High Speed","Fuel Cell")

if speed_file and current_file:
    s=pd.read_csv(speed_file)
    c=pd.read_csv(current_file)
    t=s.iloc[:,0]
    sp=s.iloc[:,1]
    cur=c.iloc[:,1]
    n=min(len(s),len(c))
    hist=[]
    ph=st.empty()
    tbl=st.empty()
    if st.button("Start"):
        for i in range(n):
            mode,src=ems(float(sp.iloc[i]),float(cur.iloc[i]))
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=t[:i+1],y=sp[:i+1],name="Speed"))
            fig.add_trace(go.Scatter(x=t[:i+1],y=cur[:i+1],name="Current",yaxis="y2"))
            fig.update_layout(yaxis2=dict(overlaying="y",side="right"))
            ph.plotly_chart(fig,use_container_width=True)
            hist.append({"Time":t.iloc[i],"Speed":sp.iloc[i],"Current":cur.iloc[i],"Mode":mode,"Decision":src})
            # tbl.dataframe(pd.DataFrame(hist).tail(25),use_container_width=True)
            tbl.dataframe(pd.DataFrame(hist), use_container_width=True)
            time.sleep(delay)
else:
    st.info("Upload both CSV files.")

