from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from utill import select_pdf,save_text_to_parent_dir
import os

def extract_pdf_text_by_page():
    pdf_path = select_pdf()  #读取pdf文件路径
    texts = []
    for page_layout in extract_pages(pdf_path): #提取每一页的文字
        page_text = ''
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                page_text += element.get_text()
        texts.append(page_text)
    pdf_filename,_ = os.path.splitext(os.path.basename(pdf_path))  # 获取pdf文件名(不包含后缀)

    for i, page_text in enumerate(texts):
        filename = f'{pdf_filename}_page_{i + 1}_text.txt'
        save_text_to_parent_dir(page_text, f'extract_text_for_{pdf_filename}', filename)
    return texts,pdf_filename

if __name__=='__main__':
    extract_pdf_text_by_page()






