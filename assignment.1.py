import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("Physics.csv")
x=df.iloc[9:19:,1]
y=df.iloc[9:19:,2]

plt.bar(x,y)
plt.show()




##################################################





import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("Physics,csv")

x=df.iloc[:,1]
y=df.iloc[:,2]

plt.bar(x,y)
plt.show()






##################################################




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("Physics.csv")

x=df.head().iloc[:,1]
y=df.head().iloc[:,2]

plt.bar(x,y)
plt.show()



#################################################



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("Physics")

x=df.tail().iloc[:,1]
y=df.tail().iloc[:,2]

plt.bar(x,y)
plt.show()




