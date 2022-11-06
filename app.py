import requests
import streamlit as st


def getAllBookstore():
	url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
	headers = {"accept": "application/json"}
	response = requests.get(url, headers=headers)
	res = response.json()# 將 response 轉換成 json 格式
	return res# 回傳值

def getCountyOption(items):
	optionList = []# 創建一個空的 List 並命名為 optionList
	for item in items:
		name = item['cityName'][0:3]
        # 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
		# hint: 想辦法處理 item['cityName'] 的內容
		if name not in optionList:
            optionList.append(name)
        # 如果 name 不在 optionList 之中，便把它放入 optionList
		# hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
	return optionList

def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        if county not in name: continue
        # 如果 name 不是我們選取的 county 則跳過
        # hint: 用 if-else 判斷並用 continue 跳過
    return specificBookstoreList

def getBookstoreInfo(items):
    expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        expander.write(item['intro'])
        expander.subheader('Address')
        expander.write(item['address'])
        expander.subheader('Open Time')
        expander.write(item['openTime'])
        expander.subheader('Email')
        expander.write(item['email'])
        expanderList.append(expander)
    return expanderList

def app():
	bookstoreList = getAllBookstore()# 呼叫 getAllBookstore 函式並將其賦值給變數 bookstoreList
    
    countyOption = getCountyOption(bookstoreList)# 呼叫 getCountyOption 並將回傳值賦值給變數 countyOption
	
    st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList)) # 將 118 替換成書店的數量
	county = st.selectbox('請選擇縣市', ['A', 'B', 'C'])
    districtOption = getDistrictOption(bookstoreList, county)
	district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])
    
    specificBookstore = getSpecificBookstore(bookstoreList, county, district)# 呼叫 getSpecificBookstore 並將回傳值賦值給變數 specificBookstore
	num = len(specificBookstore)
    st.write(f'總共有{num}項結果',num)

if __name__ == '__main__':
    app()


