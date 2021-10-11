# Internet Speed Test
# $ pip install speedtest-cli

from speedtest import Speedtest

st = Speedtest()


print("Running speed test...")
print("Your connection's download speed is: ", st.download())
print("Your connection's upload speed is: ", st.upload())
