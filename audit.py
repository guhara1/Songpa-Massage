#!/usr/bin/env python3
"""배포 전 감사 스크립트.

검사 항목:
  1. 타이틀/디스크립션 중복
  2. 디스크립션 길이 (50~160자)
  3. 색인 페이지 본문 글자수 (2,000~2,500자)
  4. 페이지 간 유사도 (8-gram Jaccard < 0.30)
  5. 도어웨이 URL 패턴 (숫자 행정동, 역+테마 조합, 출구별)
  6. JSON-LD 파싱
  7. 내부링크 대상 존재 여부
"""
import html
import json
import re
import sys

sys.path.insert(0, ".")
from content import PAGES

MIN_CHARS, MAX_CHARS = 2000, 2500


def body_text(page):
    text = re.sub(r'<section class="pricing">.*?</section>', " ", page["body"], flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def ngrams(text, n=8):
    toks = text.split()
    return set(tuple(toks[i:i + n]) for i in range(max(0, len(toks) - n + 1)))


errors, warnings = [], []

# 1. 타이틀/디스크립션 중복
seen_t, seen_d = {}, {}
for p in PAGES:
    if p["title"] in seen_t:
        errors.append(f"타이틀 중복: {p['path']} == {seen_t[p['title']]}")
    seen_t[p["title"]] = p["path"]
    if p["desc"] in seen_d:
        errors.append(f"디스크립션 중복: {p['path']} == {seen_d[p['desc']]}")
    seen_d[p["desc"]] = p["path"]

# 2~3. 디스크립션 길이 / 본문 글자수
for p in PAGES:
    if not p.get("noindex"):
        dl = len(p["desc"])
        if not (50 <= dl <= 160):
            warnings.append(f"디스크립션 길이 {dl}자: /{p['path']}")
        cl = len(body_text(p))
        if not (MIN_CHARS <= cl <= MAX_CHARS):
            errors.append(f"본문 {cl}자 (기준 {MIN_CHARS}~{MAX_CHARS}): /{p['path']}")

# 4. 유사도
texts = {p["path"]: ngrams(body_text(p)) for p in PAGES if not p.get("noindex")}
paths = list(texts)
worst = 0.0
for i in range(len(paths)):
    for j in range(i + 1, len(paths)):
        a, b = texts[paths[i]], texts[paths[j]]
        if not a or not b:
            continue
        jac = len(a & b) / len(a | b)
        worst = max(worst, jac)
        if jac >= 0.30:
            errors.append(f"유사도 {jac:.2f}: /{paths[i]} ~ /{paths[j]}")

# 5. 도어웨이 URL 패턴
bad_url = re.compile(
    r"(-\d+-dong/)|(stations/.+/(swedish|thai|aroma|24hours|homecare))|(exit)|"
    r"(songpa/.+-dong/.+/)"
)
for p in PAGES:
    if bad_url.search(p["path"]):
        errors.append(f"도어웨이 의심 URL: /{p['path']}")

# 6. JSON-LD 파싱
for p in PAGES:
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',
                         p.get("extra_head", ""), re.S):
        try:
            json.loads(m.group(1))
        except json.JSONDecodeError as e:
            errors.append(f"JSON-LD 오류 /{p['path']}: {e}")

# 7. 내부링크 대상 존재 여부
known = {"/" + p["path"] for p in PAGES} | {"/"}
for p in PAGES:
    for href in re.findall(r'href="(/[^"#]*)[#"]', p["body"]):
        if not href.endswith("/"):
            continue
        if href not in known:
            errors.append(f"끊어진 내부링크 /{p['path']} -> {href}")

print(f"페이지 {len(PAGES)}개 검사 / 최고 유사도 {worst:.2f}")
for w in warnings:
    print(f"  [경고] {w}")
for e in errors:
    print(f"  [오류] {e}")
if not errors:
    print("통과: 중복 0 / 글자수 범위 위반 0 / 유사도 OK / 도어웨이 0 / JSON-LD 오류 0")
sys.exit(1 if errors else 0)
