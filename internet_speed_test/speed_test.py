# Internet Speed Test
# $ pip install speedtest-cli

from speedtest import Speedtest

st = Speedtest()



print("Your connection's download is:", st.download())
st.upload()