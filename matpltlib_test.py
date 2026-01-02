import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["Font.family"] = "Malgun Gothic"
plt.rcPrams["axex.unicode_minus"] = False

df = pd.DataFrame({
        "hour":[9,15,18,21],
        "views":[120,340,560,290]
        
})

plt.plot(df["hour"],df["views"])

plt.title("시간대별 기사 조회수")
plt.xlabel("시간")
plt.ylabel("조회수")
         
plt.show()