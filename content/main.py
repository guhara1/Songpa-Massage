# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<meta name="naver-site-verification" content="270dc497577eacf01e6f57f10635900fcdfc334b">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HealthAndBeautyBusiness",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "송파구 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "서울특별시 송파구"
  }},
  "openingHours": "Mo-Su 00:00-24:00",
  "priceRange": "₩90,000 - ₩180,000"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "송파구 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내 페이지에서 잠실동, 문정동, 가락동, 방이동, 석촌동 등 열네 개 대표 동 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "잠실역이나 문정역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "송파구를 지나는 2·3·5·8·9호선 주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "잠실3동이나 가락1동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "숫자가 붙은 행정동은 대표 동 페이지에서 통합 안내합니다. 잠실본동·잠실2·3·7동은 잠실동, 잠실4·6동은 신천동, 가락본동·가락1·2동은 가락동 페이지를 보시면 됩니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "테마별 관리는 어디에서 확인하나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "스웨디시, 타이마사지, 홈케어 등 테마별 안내 페이지에서 특징과 추천 대상을 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 송파구 전지역</p>
    <h1>송파 출장마사지·홈타이<br>예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/courses/">코스 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>14개</strong><span>대표 지역</span></li>
      <li><strong>22개</strong><span>역세권 안내</span></li>
      <li><strong>14개</strong><span>관리 테마</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>송파 출장마사지·홈타이 서비스 안내</h2>
<p>송파구에서 방문 마사지와 홈타이 예약을 찾는 분들을 위해 가능 지역, 예약 절차, 코스 선택 기준, 이용 전 확인사항을 한곳에 정리했습니다. 이 페이지는 송파구 전체 구조를 설명하는 허브 역할을 하며, 자세한 내용은 지역별·지하철역별·테마별 안내에서 확인하실 수 있습니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차에 따라 진행하며, 처음 이용하시는 분도 어렵지 않게 예약하실 수 있습니다.</p>
</section>

<section id="coverage">
<h2>송파구 전지역 방문 가능 안내</h2>
<p>송파구 지역 안내는 풍납동부터 위례동까지 열네 개 대표 동을 중심으로 구성됩니다. 서울시 공식 기준으로 송파구는 행정동 27개, 법정동 13개인데, 풍납1·2동이나 잠실본동·잠실2·3·7동처럼 숫자로 나뉜 행정동은 별도 페이지 없이 대표 동 페이지에서 통합 안내합니다. 같은 생활권을 잘게 쪼개 비슷한 내용을 반복하기보다, 동 단위로 묶어 특징과 방문 조건을 한 번에 설명하는 편이 이용자에게도 정확하기 때문입니다.</p>
</section>

<section id="areas">
<h2>지역별 안내</h2>
<p>지역별 안내는 송파구 대표 동 기준으로 구성됩니다. 각 페이지에서는 해당 생활권의 특징, 가까운 역세권, 방문 전 확인사항, 예약 가능 시간, 어울리는 테마를 동마다 고유한 내용으로 설명합니다. 아래에서 거주하시거나 머무시는 동을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/songpa/pungnap-dong/">풍납동</a></li>
<li><a href="/songpa/geoyeo-dong/">거여동</a></li>
<li><a href="/songpa/macheon-dong/">마천동</a></li>
<li><a href="/songpa/bangi-dong/">방이동</a></li>
<li><a href="/songpa/ogeum-dong/">오금동</a></li>
<li><a href="/songpa/songpa-dong/">송파동</a></li>
<li><a href="/songpa/seokchon-dong/">석촌동</a></li>
<li><a href="/songpa/samjeon-dong/">삼전동</a></li>
<li><a href="/songpa/garak-dong/">가락동</a></li>
<li><a href="/songpa/munjeong-dong/">문정동</a></li>
<li><a href="/songpa/jangji-dong/">장지동</a></li>
<li><a href="/songpa/wirye-dong/">위례동</a></li>
<li><a href="/songpa/jamsil-dong/">잠실동</a></li>
<li><a href="/songpa/sincheon-dong/">신천동</a></li>
</ul>
<p>송파구 전체 구조가 궁금하시면 <a href="/songpa/">송파구 전체 안내</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>지하철역 인근 안내</h2>
<p>지하철역별 안내는 송파구를 지나는 2·3·5·8·9호선 역세권 기준으로 구성합니다. 각 역 페이지는 인근 생활권과 대표 동, 방문 전 준비사항을 설명하며, 출구별 페이지나 역과 테마를 조합한 페이지는 만들지 않습니다. 잠실역 같은 환승역도 페이지는 하나로 운영합니다.</p>
<ul class="card-grid">
<li><a href="/songpa/stations/jamsillaru-station/">잠실나루역</a></li>
<li><a href="/songpa/stations/jamsil-station/">잠실역</a></li>
<li><a href="/songpa/stations/jamsilsaenae-station/">잠실새내역</a></li>
<li><a href="/songpa/stations/sports-complex-station/">종합운동장역</a></li>
<li><a href="/songpa/stations/garak-market-station/">가락시장역</a></li>
<li><a href="/songpa/stations/national-police-hospital-station/">경찰병원역</a></li>
<li><a href="/songpa/stations/ogeum-station/">오금역</a></li>
<li><a href="/songpa/stations/bangi-station/">방이역</a></li>
<li><a href="/songpa/stations/gaerong-station/">개롱역</a></li>
<li><a href="/songpa/stations/geoyeo-station/">거여역</a></li>
<li><a href="/songpa/stations/macheon-station/">마천역</a></li>
<li><a href="/songpa/stations/olympic-park-station/">올림픽공원역</a></li>
<li><a href="/songpa/stations/mongchontoseong-station/">몽촌토성역</a></li>
<li><a href="/songpa/stations/seokchon-station/">석촌역</a></li>
<li><a href="/songpa/stations/songpa-station/">송파역</a></li>
<li><a href="/songpa/stations/munjeong-station/">문정역</a></li>
<li><a href="/songpa/stations/jangji-station/">장지역</a></li>
<li><a href="/songpa/stations/bokjeong-station/">복정역</a></li>
<li><a href="/songpa/stations/samjeon-station/">삼전역</a></li>
<li><a href="/songpa/stations/seokchon-gobun-station/">석촌고분역</a></li>
<li><a href="/songpa/stations/songpanaru-station/">송파나루역</a></li>
<li><a href="/songpa/stations/hanseong-baekje-station/">한성백제역</a></li>
</ul>
</section>

<section id="themes">
<h2>테마별 관리 안내</h2>
<p>테마별 안내에서는 관리 유형별 특징, 추천 대상, 예약 전 확인사항을 설명합니다. 테마는 각각 독립 페이지로 운영하며, 지역 페이지와 역 페이지에서는 관련 테마로 연결만 해 드립니다. 특정 역과 테마를 조합한 페이지는 운영하지 않으니, 원하시는 관리 유형을 먼저 고른 뒤 예약 시 위치를 알려주시면 됩니다.</p>
<ul class="card-grid">
<li><a href="/themes/swedish/">스웨디시</a></li>
<li><a href="/themes/lomilomi/">로미로미</a></li>
<li><a href="/themes/thai/">타이마사지</a></li>
<li><a href="/themes/chinese/">중국마사지</a></li>
<li><a href="/themes/aroma/">아로마테라피</a></li>
<li><a href="/themes/homecare/">홈케어</a></li>
<li><a href="/themes/hotel-style/">호텔식마사지</a></li>
<li><a href="/themes/foot/">발마사지</a></li>
<li><a href="/themes/sports/">스포츠·경락</a></li>
<li><a href="/themes/skincare/">스킨케어</a></li>
<li><a href="/themes/waxing/">왁싱</a></li>
<li><a href="/themes/couple/">커플 관리</a></li>
<li><a href="/themes/24hours/">24시간</a></li>
<li><a href="/themes/overnight/">수면 가능</a></li>
</ul>
</section>

<section id="course">
<h2>코스 선택 안내</h2>
<p>코스는 이용 목적과 그날의 컨디션에 따라 선택하시는 것이 좋습니다. 누적된 피로 해소, 편안한 휴식, 운동 후 근육 이완, 숙소 방문, 커플 동시 관리 등 상황별 선택 기준을 <a href="/courses/">코스안내</a>에서 자세히 다룹니다. 고민되시면 예약 전화에서 상태를 말씀해 주세요. 함께 정해 드립니다.</p>
</section>

<section id="how">
<h2>예약 진행 방식</h2>
<p>예약은 위치 확인, 시간 확인, 코스·인원 결정, 방문 가능 여부 안내, 예약 확정의 다섯 단계로 진행됩니다. 저녁 시간대나 주말에는 문의가 몰릴 수 있어 한두 시간 이상 여유를 두고 연락 주시기를 권장합니다. 자세한 절차는 <a href="/reservation/">예약안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="check">
<h2>이용 전 확인사항</h2>
<p>원활한 방문 관리를 위해 정확한 주소, 공동현관 출입 방법, 주차 가능 여부, 조용한 공간 확보 여부를 미리 확인해 주시면 좋습니다. 숙소나 오피스텔 방문 시에는 건물 출입 안내도 함께 알려주세요. 준비사항 전체는 <a href="/guide/">이용가이드</a>에 정리되어 있습니다.</p>
</section>

<section id="safety">
<h2>위생 및 안전 안내</h2>
<p>건전하고 안전한 방문 관리를 위해 위생 기준, 예약 정보 확인, 개인정보 보호, 금지행위 안내를 명확히 제공합니다. 불법적이거나 무리한 요청은 어떤 경우에도 진행하지 않는다는 기준을 분명히 안내드리며, 예약 정보는 관리 목적 외에 사용하지 않습니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>송파구 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내 페이지에서 잠실동, 문정동, 가락동, 방이동, 석촌동 등 열네 개 대표 동 기준으로 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>잠실역이나 문정역 근처도 가능한가요?</h3>
<p>송파구를 지나는 2·3·5·8·9호선 주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>잠실3동이나 가락1동은 왜 따로 없나요?</h3>
<p>숫자가 붙은 행정동은 대표 동 페이지에서 통합 안내합니다. 잠실본동·잠실2·3·7동은 잠실동, 잠실4·6동은 신천동, 가락본동·가락1·2동은 가락동 페이지를 보시면 됩니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다.</p>
</div>
<div class="faq-item">
<h3>테마별 관리는 어디에서 확인하나요?</h3>
<p>스웨디시, 타이마사지, 홈케어 등 테마별 안내 페이지에서 특징과 추천 대상을 확인할 수 있습니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>송파구 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "송파 출장마사지·홈타이 | 송파구 전지역 방문 마사지 예약 안내",
    "desc": "송파 출장마사지·홈타이 안내. 잠실·문정·가락·방이·석촌 등 송파구 전지역 방문, 지하철역별·테마별 관리, 예약 안내.",
    "h1": "송파 출장마사지·홈타이 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
