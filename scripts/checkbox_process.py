def get_page_processed_checkbox(page_text):
    
    CHECKBOX_UNSELECTED = "□"
    CHECKBOX_SELECTED="√"
    CHECKBOX_START_WORD=["：","?",":","？"]
    CHECKBOX_START_DEFAULT_WORD="："
    WORDS_BREAKS = [" "," ","\t", "\n"]
    while(page_text.find(CHECKBOX_UNSELECTED) != -1):
        idx = page_text.find(CHECKBOX_UNSELECTED)
        for i in range(idx, len(page_text)):
            # 对于没有选中的选项，找到第一个空格或者换行，做为checkbox的label结束，然后将checkbox和label内容删除
            if page_text[i] in WORDS_BREAKS:
                page_text = page_text[:idx] + page_text[i:]
                break
    print("page_text removed unchecked: " + page_text)    

    while(page_text.find(CHECKBOX_SELECTED) != -1):
        idx = page_text.find(CHECKBOX_SELECTED)
        # 对于选中的选项，找到第一个非空格或者换行，如果不是：或者？，则加上：
        for i in range(1,idx):
            if page_text[idx - i] not in WORDS_BREAKS:
                if(page_text[idx - i] not in CHECKBOX_START_WORD):
                    page_text = page_text[:(idx - i+1)] + CHECKBOX_START_DEFAULT_WORD + page_text[(idx+1):]
                else:
                   page_text = page_text[:(idx-i+1)] + page_text[(idx+1):]
                break
        print("processed page_text: " + page_text)   

    
    return page_text

testContent='''科大讯飞股份有限科大讯飞股份有限公司2022年半年度报告全文\n
    除上述各项之外的其他营业外收入和支出为-53,219,541.58元。所得税影响额为16,487,436.44元。少数股东权益影响额（税后）为2,840,670.54元。
    合计为-933,044.81元。\n其他符合非经常性损益定义的损益项目的具体情况：
    \n□适用 √ 不适用
    \n科大讯飞股份有限公司不存在其他符合非经常性损益定义的损益项目的具体情况。
    \n将《公开发行证券的科大讯飞股份有限公司信息披露解释性公告第1号——非经常性损益》中列举的非经常性损益项目界 定为经常性损益项目的情况说明
    \n□适用\n√\n不适用\n
    科大讯飞股份有限公司不存在将《公开发行证券的科大讯飞股份有限公司信息披露解释性公告第1号——非经常性损益》中列举的非经常性 损益项目界定为经常性损益的项目的情形。
    \n7 :unselected: :selected: :unselected: :selected: '''

if __name__ == "__main__":
    get_page_processed_checkbox(testContent)