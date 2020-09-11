import qrcode

url = 'http://192.168.1.98'
qrcode.make(url).save('./{}.png'.format('123'))
