import requests
import pandas as pd
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




""" 'ARRIVAL' """

# url 바꾸면 다른 공항도 가능
url = 'https://ubikais.fois.go.kr:8030/sysUbikais/biz/airport/airportinfo?mode=&airport=RKSI'

# 날짜 바꿔가며 데이터 가져오기
start = '2020-01-01'
end = '2020-01-02'

# date range 만들기
datelist = pd.date_range(start, end).astype(str).to_list()


for date in datelist:
    # 크롬 열기
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    
    # 원하는 날짜로 가기
    element = driver.find_element_by_xpath("//*[@id='srchDate']")
    element.click()
    element.clear()
    element.send_keys(date)
    element.send_keys(Keys.RETURN)
    time.sleep(3)           # 시간을 주었지만 홈페이지가 안불러와지면 에러남
                            # 자동으로 해당 시간으로 내려감 -> 일단 3초뒤 스크롤 하는걸로 떔빵
    
    
    """ 'Arrival' """
    # 테이블에서 스크롤을 맨 위로 올리는 것
    driver.find_element_by_xpath("//*[@id='grid_w2uiGridArrival_records']").click()
    time.sleep(1)    
    driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
    time.sleep(1) 
    driver.find_element_by_xpath("//*[@id='grid_w2uiGridArrival_records']").click()
    time.sleep(1)    
    driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
    time.sleep(1)    
    
    # 해당 운항 횟수
    arrival_end = driver.find_element_by_xpath("//*[@id='grid_w2uiGridArrival_footer']/div/div[2]")
    arrival_total = arrival_end.text
    arrival_total = int(arrival_total[-3:])           # 만약 그날 1000대가 넘게 들어오면 제대로 안됨 
    
    # 빈 list 만들기
    Arrival_FLT = []
    Arrival_DEP = []
    Arrival_SCH = []
    Arrival_ETA = []
    Arrival_ATA = []
    Arrival_STT = []

    
    
# 패턴이 9줄 9줄 9줄 10줄 이후에 9줄 10줄 반복이어서 이렇게 넣음
############################################################################################################################
############################################################################################################################
############################################################################################################################

    # 스크롤 내리기    
    #driver.find_element_by_xpath("//*[@id='grid_w2uiGridArrival_records']").click()
    for i in range(9):        # 맨 처음에 17번 내려도 상관 없음
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
        time.sleep(0.05)    
    
    for i in range(0,14):
        arrival_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_0']/div/span")
        arrival_dep = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_1']/div")
        arrival_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_2']/div")
        arrival_eta = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_3']/div")
        arrival_ata = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_5']/div")
        arrival_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_7']/div")
        Arrival_FLT.append(arrival_flt.text)
        Arrival_DEP.append(arrival_dep.text)
        Arrival_SCH.append(arrival_sch.text)
        Arrival_ETA.append(arrival_eta.text)
        Arrival_ATA.append(arrival_ata.text)
        Arrival_STT.append(arrival_stt.text)
    # 스크롤 내리기    
    driver.find_element_by_xpath("//*[@id='grid_w2uiGridArrival_records']").click()
    time.sleep(0.1)
    for i in range(10):
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
        time.sleep(0.05)    

    for i in range(14,28):
        arrival_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_0']/div/span")
        arrival_dep = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_1']/div")
        arrival_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_2']/div")
        arrival_eta = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_3']/div")
        arrival_ata = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_5']/div")
        arrival_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_7']/div")
        Arrival_FLT.append(arrival_flt.text)
        Arrival_DEP.append(arrival_dep.text)
        Arrival_SCH.append(arrival_sch.text)
        Arrival_ETA.append(arrival_eta.text)
        Arrival_ATA.append(arrival_ata.text)
        Arrival_STT.append(arrival_stt.text)
    # 스크롤 내리기    
    driver.find_element_by_xpath("//*[@id='grid_w2uiGridArrival_records']").click()
    time.sleep(0.1)
    for i in range(10):
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
        time.sleep(0.05)           
        
    for i in range(28,42):
        arrival_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_0']/div/span")
        arrival_dep = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_1']/div")
        arrival_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_2']/div")
        arrival_eta = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_3']/div")
        arrival_ata = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_5']/div")
        arrival_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_7']/div")
        Arrival_FLT.append(arrival_flt.text)
        Arrival_DEP.append(arrival_dep.text)
        Arrival_SCH.append(arrival_sch.text)
        Arrival_ETA.append(arrival_eta.text)
        Arrival_ATA.append(arrival_ata.text)
        Arrival_STT.append(arrival_stt.text)
    # 스크롤 내리기    
    driver.find_element_by_xpath("//*[@id='grid_w2uiGridArrival_records']").click()
    time.sleep(0.1)
    for i in range(10):
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
        time.sleep(0.05)           
        
    for i in range(42,56):
        arrival_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_0']/div/span")
        arrival_dep = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_1']/div")
        arrival_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_2']/div")
        arrival_eta = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_3']/div")
        arrival_ata = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_5']/div")
        arrival_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_7']/div")
        Arrival_FLT.append(arrival_flt.text)
        Arrival_DEP.append(arrival_dep.text)
        Arrival_SCH.append(arrival_sch.text)
        Arrival_ETA.append(arrival_eta.text)
        Arrival_ATA.append(arrival_ata.text)
        Arrival_STT.append(arrival_stt.text)
    # 스크롤 내리기    
    driver.find_element_by_xpath("//*[@id='grid_w2uiGridArrival_records']").click()
    time.sleep(0.1)
    for i in range(11):
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
        time.sleep(0.05)           
        
############################################################################################################################
############################################################################################################################
############################################################################################################################



    # Data 가져오고 각 list에 저장
    for a in range(56,1000,27):     # 1000은 그냥 임의의 숫자

        if a+27 <= arrival_total:
            # 데이터 읽어오기 - 1
            for i in range(a,a+13):
                arrival_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_0']/div/span")
                arrival_dep = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_1']/div")
                arrival_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_2']/div")
                arrival_eta = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_3']/div")
                arrival_ata = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_5']/div")
                arrival_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_7']/div")
                Arrival_FLT.append(arrival_flt.text)
                Arrival_DEP.append(arrival_dep.text)
                Arrival_SCH.append(arrival_sch.text)
                Arrival_ETA.append(arrival_eta.text)
                Arrival_ATA.append(arrival_ata.text)
                Arrival_STT.append(arrival_stt.text)
            # 스크롤 내리기    
            driver.find_element_by_xpath("//*[@id='grid_w2uiGridArrival_records']").click()
            time.sleep(0.1)
            for i in range(10):
                driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
                time.sleep(0.05)
                
            # 데이터 읽어오기 - 2
            for i in range(a+13,a+27):
                arrival_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_0']/div/span")
                arrival_dep = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_1']/div")
                arrival_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_2']/div")
                arrival_eta = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_3']/div")
                arrival_ata = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_5']/div")
                arrival_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_7']/div")
                Arrival_FLT.append(arrival_flt.text)
                Arrival_DEP.append(arrival_dep.text)
                Arrival_SCH.append(arrival_sch.text)
                Arrival_ETA.append(arrival_eta.text)
                Arrival_ATA.append(arrival_ata.text)
                Arrival_STT.append(arrival_stt.text)
            # 스크롤 내리기    
            driver.find_element_by_xpath("//*[@id='grid_w2uiGridArrival_records']").click()
            time.sleep(0.1)
            for i in range(11):
                driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
                time.sleep(0.05)
                
        # 마지막 나머지 가져오기        
        #elif a+42 >= arrival_total:    
        else:
            # 데이터 읽어오기
            for i in range(a,arrival_total):
                arrival_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_0']/div/span")
                arrival_dep = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_1']/div")
                arrival_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_2']/div")
                arrival_eta = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_3']/div")
                arrival_ata = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_5']/div")
                arrival_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridArrival_data_{i}_7']/div")
                Arrival_FLT.append(arrival_flt.text)
                Arrival_DEP.append(arrival_dep.text)
                Arrival_SCH.append(arrival_sch.text)
                Arrival_ETA.append(arrival_eta.text)
                Arrival_ATA.append(arrival_ata.text)
                Arrival_STT.append(arrival_stt.text)

                
    # DataFrame으로 넣기            
    Arrival = pd.DataFrame({'Arrival_FLT' : Arrival_FLT,
                            'Arrival_DEP' : Arrival_DEP,
                            'Arrival_SCH' : Arrival_SCH,
                            'Arrival_ETA' : Arrival_ETA,
                            'Arrival_ATA' : Arrival_ATA,
                            'Arrival_STT' : Arrival_STT })
    # csv로 저장
    Arrival.to_csv(f'C:\\Users\\user\\proj\\TMA_capacity\\data\\FOIS\\Arrival_{date}.csv')
   
    
    """ '종료' """
    # Chrome webdriver 종료
    driver.quit()
    
    # fois 사이트야 로딩 좀 바로 되라
    time.sleep(3)




""" DEAPRTURE """
# url 바꾸면 다른 공항도 가능
url = 'https://ubikais.fois.go.kr:8030/sysUbikais/biz/airport/airportinfo?mode=&airport=RKSI'

# 날짜 바꿔가며 데이터 가져오기
start = '2020-01-01'
end = '2020-01-02'

# date range 만들기
datelist = pd.date_range(start, end).astype(str).to_list()


for date in datelist:
    # 크롬 열기
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    
    # 원하는 날짜로 가기
    element = driver.find_element_by_xpath("//*[@id='srchDate']")
    element.click()
    element.clear()
    element.send_keys(date)
    element.send_keys(Keys.RETURN)
    time.sleep(3)           # 시간을 주었지만 홈페이지가 안불러와지면 에러남
                            # 자동으로 해당 시간으로 내려감 -> 일단 3초뒤 스크롤 하는걸로 떔빵

    
    
    """ Departure """
    # 테이블에서 스크롤을 맨 위로 올리는 것
    driver.find_element_by_xpath("//*[@id='grid_w2uiGridDeparture_records']").click()
    time.sleep(1)    
    driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='grid_w2uiGridDeparture_records']").click()
    time.sleep(1)
    driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
    time.sleep(1)
    
    # 해당 운항 횟수
    departure_end = driver.find_element_by_xpath("//*[@id='grid_w2uiGridDeparture_footer']/div/div[2]")
    departure_total = departure_end.text
    departure_total = int(departure_total[-3:])           # 만약 그날 1000대가 넘게 나가면 제대로 안됨 
    
    # 빈 list 만들기
    Departure_FLT = []
    Departure_ARR = []
    Departure_SCH = []
    Departure_ETD = []
    Departure_ATD = []
    Departure_STT = []

    
############################################################################################################################
############################################################################################################################
############################################################################################################################

    # 스크롤 내리기    
    #driver.find_element_by_xpath("//*[@id='grid_w2uiGridArrival_records']").click()
    for i in range(9):        # 맨 처음에 9번 내려도 상관 없음
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN) 
        time.sleep(0.05)    
    
    for i in range(0,14):
        departure_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_0']/div/span")
        departure_arr = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_1']/div")
        departure_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_2']/div")
        departure_etd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_3']/div")
        departure_atd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_6']/div")
        departure_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_8']/div")
        Departure_FLT.append(departure_flt.text)
        Departure_ARR.append(departure_arr.text)
        Departure_SCH.append(departure_sch.text)
        Departure_ETD.append(departure_etd.text)
        Departure_ATD.append(departure_atd.text)
        Departure_STT.append(departure_stt.text)
    # 스크롤 내리기    
    driver.find_element_by_xpath("//*[@id='grid_w2uiGridDeparture_records']").click()
    time.sleep(0.05)
    for i in range(10):
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
        time.sleep(0.03)    
      
    for i in range(14,28):
        departure_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_0']/div/span")
        departure_arr = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_1']/div")
        departure_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_2']/div")
        departure_etd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_3']/div")
        departure_atd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_6']/div")
        departure_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_8']/div")
        Departure_FLT.append(departure_flt.text)
        Departure_ARR.append(departure_arr.text)
        Departure_SCH.append(departure_sch.text)
        Departure_ETD.append(departure_etd.text)
        Departure_ATD.append(departure_atd.text)
        Departure_STT.append(departure_stt.text)
    # 스크롤 내리기    
    driver.find_element_by_xpath("//*[@id='grid_w2uiGridDeparture_records']").click()
    time.sleep(0.05)
    for i in range(10):
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
        time.sleep(0.03)           
     
    for i in range(28,42):
        departure_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_0']/div/span")
        departure_arr = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_1']/div")
        departure_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_2']/div")
        departure_etd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_3']/div")
        departure_atd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_6']/div")
        departure_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_8']/div")
        Departure_FLT.append(departure_flt.text)
        Departure_ARR.append(departure_arr.text)
        Departure_SCH.append(departure_sch.text)
        Departure_ETD.append(departure_etd.text)
        Departure_ATD.append(departure_atd.text)
        Departure_STT.append(departure_stt.text)
    # 스크롤 내리기    
    driver.find_element_by_xpath("//*[@id='grid_w2uiGridDeparture_records']").click()
    time.sleep(0.05)
    for i in range(10):
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
        time.sleep(0.03)              

    for i in range(42,56):
        departure_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_0']/div/span")
        departure_arr = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_1']/div")
        departure_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_2']/div")
        departure_etd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_3']/div")
        departure_atd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_6']/div")
        departure_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_8']/div")
        Departure_FLT.append(departure_flt.text)
        Departure_ARR.append(departure_arr.text)
        Departure_SCH.append(departure_sch.text)
        Departure_ETD.append(departure_etd.text)
        Departure_ATD.append(departure_atd.text)
        Departure_STT.append(departure_stt.text)
    # 스크롤 내리기    
    driver.find_element_by_xpath("//*[@id='grid_w2uiGridDeparture_records']").click()
    time.sleep(0.05)
    for i in range(11):
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
        time.sleep(0.03)           
        
############################################################################################################################
############################################################################################################################
############################################################################################################################


    
    
    # Data 가져오고 각 list에 저장
    for a in range(56,1000,27):     # 1000은 그냥 임의의 숫자
        
        if a+27 < departure_total:
            # 데이터 읽어오기 - 1
            for i in range(a,a+13):
                departure_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_0']/div/span")
                departure_arr = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_1']/div")
                departure_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_2']/div")
                departure_etd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_3']/div")
                departure_atd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_6']/div")
                departure_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_8']/div")
                Departure_FLT.append(departure_flt.text)
                Departure_ARR.append(departure_arr.text)
                Departure_SCH.append(departure_sch.text)
                Departure_ETD.append(departure_etd.text)
                Departure_ATD.append(departure_atd.text)
                Departure_STT.append(departure_stt.text)
            # 스크롤 내리기    
            driver.find_element_by_xpath("//*[@id='grid_w2uiGridDeparture_records']").click()  
            time.sleep(0.05)
            for i in range(10):    
                driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
                time.sleep(0.03)       
            
            
            # 데이터 읽어오기 - 2
            for i in range(a+13,a+27):
                departure_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_0']/div/span")
                departure_arr = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_1']/div")
                departure_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_2']/div")
                departure_etd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_3']/div")
                departure_atd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_6']/div")
                departure_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_8']/div")
                Departure_FLT.append(departure_flt.text)
                Departure_ARR.append(departure_arr.text)
                Departure_SCH.append(departure_sch.text)
                Departure_ETD.append(departure_etd.text)
                Departure_ATD.append(departure_atd.text)
                Departure_STT.append(departure_stt.text)
            # 스크롤 내리기    
            driver.find_element_by_xpath("//*[@id='grid_w2uiGridDeparture_records']").click()  
            time.sleep(0.05)
            for i in range(11):    
                driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)   
                time.sleep(0.03)
                
                
        # 마지막 나머지 가져오기    
        # elif a+42 >= departure_total:
        else:
            # 데이터 읽어오기
            for i in range(a,departure_total):
                departure_flt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_0']/div/span")
                departure_arr = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_1']/div")
                departure_sch = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_2']/div")
                departure_etd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_3']/div")
                departure_atd = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_6']/div")
                departure_stt = driver.find_element_by_xpath(f"//*[@id='grid_w2uiGridDeparture_data_{i}_8']/div")
                Departure_FLT.append(departure_flt.text)
                Departure_ARR.append(departure_arr.text)
                Departure_SCH.append(departure_sch.text)
                Departure_ETD.append(departure_etd.text)
                Departure_ATD.append(departure_atd.text)
                Departure_STT.append(departure_stt.text)
             
                
    # DataFrame으로 넣기            
    Departure = pd.DataFrame({'Departure_FLT' : Departure_FLT,
                              'Departure_ARR' : Departure_ARR,
                              'Departure_SCH' : Departure_SCH,
                              'Departure_ETD' : Departure_ETD,
                              'Departure_ATD' : Departure_ATD,
                              'Departure_STT' : Departure_STT  })
    
    # csv로 저장
    Departure.to_csv(f'C:\\Users\\user\\proj\\TMA_capacity\\data\\FOIS\\Departure_{date}.csv') 
        
        
    """ 종료 """
    # Chrome webdriver 종료
    driver.quit()
    
    # fois 사이트야 로딩 좀 바로 되라
    time.sleep(3)