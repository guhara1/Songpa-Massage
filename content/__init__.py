# 전체 페이지 목록 집계 — 모듈이 아직 없으면 건너뛴다(부분 빌드 허용).
import importlib

_MODULES = [
    "main",        # 메인 1
    "areas_a",     # 지역 허브 + 대표 동 7 (풍납·거여·마천·방이·오금·송파·석촌)
    "areas_b",     # 대표 동 7 (삼전·가락·문정·장지·위례·잠실·신천)
    "stations_a",  # 역 허브 + 2·3호선 + 5호선 일부 (11개 역)
    "stations_b",  # 5호선 올림픽공원 + 8·9호선 (11개 역)
    "themes",      # 테마 허브 + 14
    "info",        # 안내·코스·예약·가이드·후기·고객센터·약관
    "magazine",    # 매거진 허브 + 아티클
    "about",       # 운영자 소개
]

PAGES = []
for _name in _MODULES:
    try:
        _m = importlib.import_module("." + _name, __package__)
    except ImportError:
        continue
    if hasattr(_m, "PAGES"):
        PAGES += list(_m.PAGES)
    elif hasattr(_m, "PAGE"):
        PAGES.append(_m.PAGE)
