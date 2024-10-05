
import translators as ts   #translate 库可以直接调用多个翻译平台的服务
from utill import save_text_to_parent_dir
from translators.server import TranslatorError
def translate(texts,pdf_filename,service,from_lang,to_lang):

    print(f'选择服务：{service}')
    print(f'可用服务：{ts.translators_pool}')

    for i, text in enumerate(texts):
        to_text = None  # 初始化 to_text 为空值

        # 设置最大重试次数，防止陷入死循环
        max_retries = 10
        retries = 0

        # 重试机制：只要翻译结果为空并且重试次数没有超过上限，就继续重试
        while not to_text and retries < max_retries:
            try:
                # 尝试调用翻译函数
                to_text = ts.translate_text(query_text=text, translator=service, from_language=from_lang,
                                            to_language=to_lang)
                # 如果翻译成功（to_text 不为空），打印成功消息并跳出循环
                if to_text:
                    print(f"{pdf_filename}_page_{i + 1} 翻译成功")
                    break
            except TranslatorError:
                retries += 1
                print(f"Translation failed due to TranslatorError. Retrying {retries}/{max_retries}...")
            except Exception as e:  # 捕获其他异常
                retries += 1
                print(f"An unexpected error occurred: {e}. Retrying {retries}/{max_retries}...")

        # 检查最终的翻译结果，如果未成功翻译则输出提示
        if not to_text:
            print(f"Translation failed for {pdf_filename}_page_{i + 1} after maximum retries.")
            continue  # 跳过保存并继续翻译下一段文本

        filename = f'{pdf_filename}_page_{i + 1}_translated_text.txt'
        save_text_to_parent_dir(to_text, f'translated_text_for_{pdf_filename}', filename)
