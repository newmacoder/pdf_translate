from extract import  extract_pdf_text_by_page
from translate import translate
import configparser
config = configparser.ConfigParser()
# 读取 .cfg 配置文件
config.read('config.cfg', encoding='utf-8')
service = config['translation_service']['service']
from_lang = config['translation_service']['from_lang']
to_lang = config['translation_service']['to_lang']


texts,pdf_filename=extract_pdf_text_by_page()    #提取pdf每一页的文字并保存

translate(texts,pdf_filename,service,from_lang,to_lang)    #逐页翻译文本并保存





