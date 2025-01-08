import speedtest

test = speedtest.Speedtest()

down = test.download()
upload = test.upload()

print(f'Speed of download: {down}')
print(f'Speed of Upload: {upload}')