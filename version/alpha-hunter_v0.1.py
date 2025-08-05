import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QAxContainer import QAxWidget
import time

class KiwoomAPI:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._on_login)
        self.login_event_loop = None
        self.logged_in = False

    def _on_login(self, err_code):
        if err_code == 0:
            print("로그인 성공")
            self.logged_in = True
        else:
            print("로그인 실패")
        self.login_event_loop.exit()

    def login(self):
        self.ocx.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def get_account_info(self):
        return self.ocx.dynamicCall("GetLoginInfo(QString)", "ACCNO").split(';')[0]

    def get_stock_price(self, code):
        self.ocx.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)
        self.ocx.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")
        # 수신 대기 필요 (이벤트 기반 처리 필요)

    def buy_stock(self, account, code, qty, price):
        self.ocx.dynamicCall("SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)",
                             ["주식주문", "0101", account, 1, code, qty, price, "00", ""])

    def sell_stock(self, account, code, qty, price):
        self.ocx.dynamicCall("SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)",
                             ["주식주문", "0101", account, 2, code, qty, price, "00", ""])

if __name__ == "__main__":
    kiwoom = KiwoomAPI()
    kiwoom.login()
    account = kiwoom.get_account_info()
    print("계좌번호:", account)

    # 예: 삼성전자 매수 (005930), 10주, 시장가
    kiwoom.buy_stock(account, "005930", 10, 0)
    time.sleep(2)

    # 예: 삼성전자 매도
    kiwoom.sell_stock(account, "005930", 10, 0)
