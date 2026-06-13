# 지하철역별 안내(A) — 허브 1개 + 2·3호선 + 5호선 일부 (역 11개).
# 환승역도 URL은 하나만 사용한다. 출구별·역+테마 조합 페이지는 만들지 않는다.
from .site import PHONE, PHONE_DISPLAY
from .pricing import PRICING

_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>역 인근 위치와 희망 시간을 알려주시면 방문 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

_HUB_BODY = """
<p class="lead">송파구를 지나는 2·3·5·8·9호선 주요 역세권을 기준으로 방문 관리를 안내합니다. 환승역은 노선이 여러 개라도 페이지는 하나만 운영합니다.</p>

<section>
<h2>역세권 안내 구성 기준</h2>
<p>송파구는 서울 자치구 가운데 지하철 노선이 가장 촘촘하게 깔린 곳 중 하나로, 다섯 개 노선이 구를 가로지릅니다. 이 사이트의 역 안내는 역마다 페이지 하나를 두는 단일 페이지 원칙을 따릅니다. 잠실역처럼 두 노선이 만나는 환승역도, 오금역처럼 한 노선의 종점이면서 다른 노선이 지나는 역도 페이지는 하나입니다. 출구 번호별 페이지나 역 이름 뒤에 관리 테마를 붙인 조합 페이지는 만들지 않습니다. 그런 식의 양산형 페이지는 내용이 겹쳐 검색하는 분에게 오히려 혼란만 주기 때문입니다. 각 역 페이지에는 역세권 분위기, 인근 대표 동, 자주 들어오는 일정 유형, 예약 시 참고할 점을 역마다 다르게 담았습니다.</p>
</section>

<section>
<h2>2호선 송파권</h2>
<p>2호선은 한강을 따라 송파구 북서부를 지납니다. 파크리오 단지 앞의 <a href="/songpa/stations/jamsillaru-station/">잠실나루역</a>, 롯데월드타워가 서 있는 <a href="/songpa/stations/jamsil-station/">잠실역</a>, 먹자골목과 대단지가 만나는 <a href="/songpa/stations/jamsilsaenae-station/">잠실새내역</a>, 경기장 일대의 <a href="/songpa/stations/sports-complex-station/">종합운동장역</a>이 차례로 이어집니다. 송파에서 유동인구가 가장 많은 구간이라 숙소 방문과 심야 문의가 집중되는 노선입니다.</p>
</section>

<section>
<h2>3호선 송파권</h2>
<p>3호선은 송파구 남부에서 끝납니다. 도매시장과 헬리오시티 사이의 <a href="/songpa/stations/garak-market-station/">가락시장역</a>, 병원을 낀 차분한 <a href="/songpa/stations/national-police-hospital-station/">경찰병원역</a>, 그리고 종점인 <a href="/songpa/stations/ogeum-station/">오금역</a> 세 정거장입니다. 주거지와 생활 시설이 섞인 구간이라 자택 방문 예약이 중심을 이룹니다.</p>
</section>

<section>
<h2>5호선 송파권</h2>
<p>5호선 마천지선은 송파구 동부를 책임집니다. <a href="/songpa/stations/olympic-park-station/">올림픽공원역</a>에서 시작해 <a href="/songpa/stations/bangi-station/">방이역</a>, <a href="/songpa/stations/ogeum-station/">오금역</a>, <a href="/songpa/stations/gaerong-station/">개롱역</a>, <a href="/songpa/stations/geoyeo-station/">거여역</a>을 지나 종점 <a href="/songpa/stations/macheon-station/">마천역</a>까지 닿습니다. 뉴타운 신축 단지와 오래된 주택가가 함께 있는 구간으로, 입주 직후 예약과 가족 단위 자택 예약이 많은 노선입니다.</p>
</section>

<section>
<h2>8호선 송파권</h2>
<p>8호선은 송파구를 남북으로 관통하는 중심축입니다. 올림픽공원 서쪽의 <a href="/songpa/stations/mongchontoseong-station/">몽촌토성역</a>에서 시작해 <a href="/songpa/stations/jamsil-station/">잠실역</a>, <a href="/songpa/stations/seokchon-station/">석촌역</a>, <a href="/songpa/stations/songpa-station/">송파역</a>, <a href="/songpa/stations/garak-market-station/">가락시장역</a>, <a href="/songpa/stations/munjeong-station/">문정역</a>, <a href="/songpa/stations/jangji-station/">장지역</a>을 거쳐 <a href="/songpa/stations/bokjeong-station/">복정역</a>으로 빠집니다. 법조타운과 위례 생활권까지 이어져 송파 거주자의 일상 동선 대부분이 이 노선 위에 있습니다.</p>
</section>

<section>
<h2>9호선 송파권</h2>
<p>9호선 연장 구간은 송파구 한가운데를 동서로 가로지릅니다. <a href="/songpa/stations/sports-complex-station/">종합운동장역</a>에서 들어와 <a href="/songpa/stations/samjeon-station/">삼전역</a>, <a href="/songpa/stations/seokchon-gobun-station/">석촌고분역</a>, <a href="/songpa/stations/seokchon-station/">석촌역</a>, <a href="/songpa/stations/songpanaru-station/">송파나루역</a>, <a href="/songpa/stations/hanseong-baekje-station/">한성백제역</a>을 지나 <a href="/songpa/stations/olympic-park-station/">올림픽공원역</a>까지 이어집니다. 빌라와 소형 단지가 많은 안쪽 생활권을 훑는 노선이라 1인 가구 방문 문의가 꾸준한 구간입니다.</p>
</section>

<section>
<h2>환승역은 페이지 하나로 안내합니다</h2>
<p>송파구 안의 환승역은 여섯 곳입니다. 잠실역(2·8호선), 종합운동장역(2·9호선), 가락시장역(3·8호선), 오금역(3·5호선), 석촌역(8·9호선), 올림픽공원역(5·9호선)이 그것인데, 어느 역이든 URL은 하나만 사용합니다. 노선마다 페이지를 쪼개면 같은 동네 이야기를 두 번 쓰게 되고, 검색으로 들어온 분도 어느 쪽을 봐야 할지 헷갈리기 때문입니다. 위 노선별 목록에 환승역이 두 번 등장하더라도 연결되는 페이지는 같습니다. 예약하실 때도 몇 호선 쪽인지 구분해 말씀하실 필요가 전혀 없습니다.</p>
</section>

<section>
<h2>역 기준으로 예약하실 때</h2>
<p>역 이름은 위치를 설명하는 편한 기준이지만, 방문 자체는 언제나 주소로 이루어집니다. 전화 주실 때 가까운 역과 함께 건물명이나 도로명 주소를 알려주시면 도착 시간을 정확히 잡아 드립니다. 거주 동 기준 안내가 편하시면 <a href="/songpa/">지역별 안내</a>를, 관리 방식이 먼저 궁금하시면 <a href="/themes/">테마별 안내</a>를 보셔도 됩니다. 두 역 사이 애매한 위치라면 아무 역 페이지나 참고하셔도 무방하고, 어느 역에서 출발하든 절차와 비용 기준은 동일합니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>역 근처에서 만나 함께 이동하는 방식인가요?</h3>
<p>아니요. 관리사가 준비물을 챙겨 알려주신 주소로 직접 방문합니다. 역은 위치를 설명하는 기준일 뿐 만남 장소가 아닙니다.</p>
</div>
<div class="faq-item">
<h3>목록에 없는 역이나 버스 정류장 기준으로 설명해도 되나요?</h3>
<p>됩니다. 역 페이지는 안내 편의를 위한 구분일 뿐이며, 송파구 전지역이 방문 범위입니다. 큰 사거리나 정류장 이름으로 설명하셔도 예약에는 문제가 없습니다.</p>
</div>
</section>
""" + PRICING + _CTA


def _station(slug, name, title_name, desc, sections):
    return {
        "path": f"songpa/stations/{slug}/",
        "title": f"{title_name} 출장마사지·홈타이 | 역세권 방문 관리 안내",
        "desc": desc,
        "h1": f"{name} 인근 방문 관리 안내",
        "body": sections + PRICING + _CTA,
        "breadcrumb": [("지하철역별 안내", "/songpa/stations/"), (name, None)],
    }


HUB = {
    "path": "songpa/stations/",
    "title": "송파 지하철역별 출장마사지·홈타이 안내 | 간다GO",
    "desc": "송파구 2·3·5·8·9호선 역세권별 방문 관리 안내입니다. 환승역 단일 페이지 원칙과 노선별 역 목록, 역 기준 예약 요령을 정리했습니다.",
    "h1": "송파 지하철역별 방문 관리 안내",
    "body": _HUB_BODY,
    "breadcrumb": [("지하철역별 안내", None)],
}
