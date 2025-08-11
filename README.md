# 🌏 alpha-hunter (KRX Stock Trader)
> 국내(코스피·코스닥) 자동매매 봇 — Python 기반, 백테스트 및 실매매 연동을 지원합니다.

**KRX Stock Trader**는 원래 해외 시장용으로 설계된 프로젝트를  
국내 주식(한국거래소: KRX — KOSPI, KOSDAQ) 환경에 맞게 변환한 오픈소스 자동매매 템플릿입니다.  
키움 OpenAPI 등 국내 증권사 API와 연동하여 전략 실행, 실시간 시세/체결 처리, 로그와 백테스트를 제공합니다.

---

## 📌 핵심 기능
- 📈 룰 기반 전략(시그널) 및 ML 기반 전략(선택적) 실행  
- 🔄 실시간/호가/체결 데이터 연동 (예: **키움증권 OpenAPI+** 사용 — 국내 매매 목적)  
- 🧪 백테스트: 히스토리컬 데이터로 전략 성능 검증 (pandas, backtrader 등)  
- 💬 텔레그램 / 디스코드 / 이메일 알림(선택) — 주문 실행, 오류, 일별 리포트 전송  
- 🧠 플러그형 모델: 전략 모듈을 쉽게 추가/교체 가능  
- 🔒 주문 전·후 안전장치: 포지션/자금관리, 주문 속도 제한, 슬리피지/수수료 고려

---

## 🎯 설계 철학
1. **모듈화** — 데이터 공급, 시그널 생성, 실행(브로커드라이버), 리스크관리, 알림을 분리.  
2. **안전 우선** — 실매매 전 필수 체크(계좌 잔고, 일별 최대 손실 등).  
3. **투명한 로그** — 모든 주문/체결/에러를 로컬 및 원격(옵션)으로 저장.  
4. **확장성** — 다른 증권사 API(지원되는 경우)나 외부 데이터 소스로 확장 가능.

---

## 🛠 권장 스택 / 라이브러리
- Python 3.9+  
- pandas, numpy — 데이터 처리  
- backtrader or vectorbt — 백테스트(선택)  
- requests / websockets — 외부 API 연동(필요 시)  
- pyqt5, comtypes 또는 pythonnet — 키움 OpenAPI+ (Windows, ActiveX) 연동  
- aiohttp / asyncio — 비동기 주문/데이터 처리(권장)  
- python-telegram-bot / discord.py — 알림

---

## 📦 설치 예시
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install pandas numpy backtrader requests websockets python-telegram-bot
# 키움 연동에 필요한 PyQt5, comtypes (Windows)
pip install pyqt5 comtypes
