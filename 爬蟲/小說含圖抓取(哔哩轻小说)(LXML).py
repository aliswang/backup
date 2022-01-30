import time
import web_crawler
from IPython.display import clear_output
  
def download_linovelib(name,next_link):
  wc = web_crawler.web_crawler()
  headers = wc.headers
  output_file = "./" + name + "/"
  txt_name = output_file + name + ".txt"
  try:
    os.mkdir(output_file)
  except:
    pass

  data = []
  while(True):
    try:
      time.sleep(0.1)
      data_etree = wc.get_etree(next_link)
      #抓取文字資料
      title = data_etree.xpath("/html/body/div[1]/div[2]/div/div[1]/h3/text()")[0] + "_" + data_etree.xpath("//*[@id=\"atitle\"]/text()")[0]
      content = data_etree.xpath("//html/body/div[1]/div[2]/div/div[2]//text()")
      next_link = "/".join(next_link.split("/")[:3]) + re.findall("url_next:'[a-z0-9./_]*",str(data_etree.xpath("/html/body/script[1]/text()")[0]))[0].replace("url_next:'","")
      #抓取圖片資料
      pic_link = data_etree.xpath("/html/body/div[1]/div[2]/div/div[2]//img/@src")
      for pic in pic_link:
        name = output_file + pic.split("/")[-1]
        with open(name, "wb") as file:
          file.write(requests.get(pic,headers=headers).content)
      #顯示當前進度
      clear_output()
      print(title)
      #新增入檔案
      data.extend([title])
      data.extend(content)
    except:
      break
  #寫入檔案
  with open(txt_name,"w", encoding='UTF-8') as w:
    for i in data:
      if(i != "\n"):
        w.write(i + "\n")
        
if __name__ == '__main__':
  name = "谁是最强鉴定士？～吃饱喝足的异世界生活～"
  next_link = "https://w.linovelib.com/novel/2536/92671.html"
  download_linovelib(name,next_link)