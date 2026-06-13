#!/usr/bin/env python3
"""색인 요청 자동화 스크립트.

사용법:
  python3 ping.py              # 전체 (IndexNow + 구글 sitemap ping)
  python3 ping.py --indexnow   # IndexNow(Bing·Naver·기타)만
  python3 ping.py --google     # 구글 sitemap ping만
  python3 ping.py --google-api # 구글 Indexing API (credentials.json 필요)

IndexNow (Bing·Naver 모두 커버):
  api.indexnow.org 로 URL 목록을 일괄 전송합니다.
  Naver는 IndexNow 참여 엔진이므로 별도 전송 불필요합니다.

Google Indexing API:
  1. Google Cloud Console > API & Services > 사용 설정 > "Indexing API" 활성화
  2. 서비스 계정 생성 > JSON 키 다운로드 > 이 파일과 같은 위치에 credentials.json 로 저장
  3. Google Search Console > 설정 > 사용자 및 권한 > 서비스 계정 이메일 추가 (소유자)
  4. pip install google-auth requests
  5. python3 ping.py --google-api
"""

import argparse
import json
import sys
import urllib.request
import urllib.parse
import urllib.error

# ─── 설정 ─────────────────────────────────────────────────────────────────────
BASE_URL = "https://songpa-massage.pages.dev"
INDEXNOW_KEY = "38dd0fc8c6bb488e95fb1fb03bf805a6"
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"

# IndexNow 참여 엔진 (api.indexnow.org 하나로 전체 배포됨)
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"


def load_sitemap_urls() -> list[str]:
    """sitemap.xml 에서 URL 목록을 읽는다."""
    import re
    with open("sitemap.xml", encoding="utf-8") as f:
        content = f.read()
    return re.findall(r"<loc>([^<]+)</loc>", content)


def ping_indexnow(urls: list[str]) -> None:
    """IndexNow 프로토콜로 Bing·Naver·Yandex 등에 일괄 통보."""
    host = urllib.parse.urlparse(BASE_URL).netloc
    payload = json.dumps({
        "host": host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }).encode()
    req = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"[IndexNow] {r.status} — {len(urls)}개 URL 전송 완료")
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        print(f"[IndexNow] 오류 {e.code}: {body[:200]}", file=sys.stderr)


def ping_google_sitemap() -> None:
    """Google에 sitemap ping (구글 Search Console 자동 크롤 요청)."""
    ping_url = f"https://www.google.com/ping?sitemap={urllib.parse.quote(SITEMAP_URL, safe=':/')}"
    try:
        with urllib.request.urlopen(ping_url, timeout=15) as r:
            print(f"[Google sitemap ping] {r.status}")
    except urllib.error.HTTPError as e:
        print(f"[Google sitemap ping] 오류 {e.code}", file=sys.stderr)


def ping_naver_sitemap() -> None:
    """네이버 서치어드바이저 sitemap ping."""
    ping_url = (
        f"https://searchadvisor.naver.com/tools/request"
        f"?url={urllib.parse.quote(SITEMAP_URL, safe=':/')}"
    )
    try:
        with urllib.request.urlopen(ping_url, timeout=15) as r:
            print(f"[Naver sitemap ping] {r.status}")
    except Exception as e:
        # 네이버 ping은 리다이렉트·인증 요구 등으로 오류가 날 수 있음
        print(f"[Naver sitemap ping] {e}")


def ping_google_indexing_api(urls: list[str]) -> None:
    """Google Indexing API — 서비스 계정 credentials.json 필요.

    pip install google-auth requests
    """
    try:
        from google.oauth2 import service_account
        import requests as req_lib
    except ImportError:
        print("[Google API] 의존성 미설치: pip install google-auth requests", file=sys.stderr)
        return

    import os
    cred_path = os.path.join(os.path.dirname(__file__), "credentials.json")
    if not os.path.exists(cred_path):
        print("[Google API] credentials.json 파일이 없습니다. README 안내를 확인하세요.", file=sys.stderr)
        return

    SCOPES = ["https://www.googleapis.com/auth/indexing"]
    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    token = creds.token
    if not token:
        creds.refresh(req_lib.Request())
        token = creds.token

    endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    ok, fail = 0, 0
    for url in urls:
        resp = req_lib.post(
            endpoint,
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json={"url": url, "type": "URL_UPDATED"},
            timeout=20,
        )
        if resp.status_code == 200:
            ok += 1
        else:
            fail += 1
            print(f"  [Google API] {resp.status_code} {url}", file=sys.stderr)
    print(f"[Google Indexing API] 성공 {ok} / 실패 {fail}")


def main():
    parser = argparse.ArgumentParser(description="색인 요청 자동화")
    parser.add_argument("--indexnow", action="store_true", help="IndexNow만 실행")
    parser.add_argument("--google", action="store_true", help="Google sitemap ping만 실행")
    parser.add_argument("--google-api", action="store_true", help="Google Indexing API 실행")
    args = parser.parse_args()

    run_all = not (args.indexnow or args.google or args.google_api)

    urls = load_sitemap_urls()
    print(f"sitemap 에서 {len(urls)}개 URL 로드됨")

    if args.indexnow or run_all:
        ping_indexnow(urls)
    if args.google or run_all:
        ping_google_sitemap()
        ping_naver_sitemap()
    if args.google_api:
        ping_google_indexing_api(urls)


if __name__ == "__main__":
    main()
