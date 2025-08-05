from pykiwoom.kiwoom import Kiwoom

# 로그인
kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# 계좌번호 출력
accounts = kiwoom.GetLoginInfo("ACCNO")
print("📂 계좌번호:", accounts)

# 삼성전자 현재가 조회
kiwoom.SetInputValue("종목코드", "005930")  # 삼성전자
data = kiwoom.CommRqData("주식기본정보요청", "opt10001", 0, "0101")
price = kiwoom.GetCommData("주식기본정보요청", "opt10001", 0, "현재가")
print("💰 현재가:", int(price))
