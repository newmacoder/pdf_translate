import os
def select_pdf():
    from tkinter import filedialog, Tk
    # 隐藏主窗口
    Tk().withdraw()

    # 打开文件选择对话框并返回路径，只允许选择PDF文件
    pdf_path = filedialog.askopenfilename(
        filetypes=[("PDF 文件", "*.pdf")]
    )

    print(f"选择的文件路径是: {pdf_path}")
    return pdf_path


def save_text_to_parent_dir(text, folder_name, filename):  #在上一级目录建立文件夹，保存文本到该目录

    # 获取当前脚本所在的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 获取上一级目录
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # 新文件夹的路径
    new_folder_path = os.path.join(parent_dir, folder_name)

    # 如果文件夹不存在，则创建该文件夹
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    # 文本文件的完整路径
    file_path = os.path.join(new_folder_path, filename)

    # 保存文本到文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"文件已保存到: {file_path}")
