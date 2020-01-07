import re
abc = "!@#Card slot!@#microSD, up to 32 GB!@#Internal!@#16 GB 1.5 GB RAM"
ram = re.findall(r"(\d.\d\sGB RAM|\d{,2}\sGB RAM|\d{,3}\sMB RAM)",abc)
print(ram)
