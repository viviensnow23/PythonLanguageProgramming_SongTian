#PyWordCloud1.py
import wordcloud
c = wordcloud.WordCloud()
c.generate("wordcloud by Python")
c.to_file("pywordcloud.png")


#PyWordCloud2.py
import wordcloud
txt = "life is short,you need python"
w = wordcloud.WordCloud(background_color = "white")
w.generate(txt)
w.to_file("pywcloud.png")

#PyWordCloud3.py
import jieba
import wordcloud
txt = "程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，它按照特定规则组织计算机指令，使计算机能够自动进行各种运算处理。"
w = wordcloud.WordCloud(width=1000,font_path="msyh.ttc",height=700)
w.generate(" ".join(jieba.lcult(txt)))
w.to_file("pywordcloud.png")

