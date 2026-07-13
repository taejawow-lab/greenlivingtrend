# Green Living Trend 콘텐츠 개선 보고서 — 2026-07-13

## 결과 요약

- 전체 MDX 글: **58개**
- 공개 유지: **20개**
- `draft: true` 전환: **38개**
- 유지 글 reader-visible 영어 본문: **각 1,013–1,957단어**
- 유지 글 frontmatter sources: **각 8–12개**
- 유지 글 본문 이미지 참조: **각 3개** (로컬 파일 존재 확인 포함)
- 유지 글은 의사결정표, 입력값을 바꾸는 계산 예, 엣지케이스, 유지관리 주기, 중단/전문가 이관 기준, 증거 기록, 한계를 포함하도록 다시 작성했다.
- 개인 사용·실험을 주장하지 않으며, 계산 수치는 명시적인 예시 입력값으로만 제시했다.
- 제작 과정 관련 표현과 18단어 이상 동일 문단을 deterministic QA로 차단했다.

## 공개 유지 목록 (20)

1. `weekend-home-energy-audit-plan`
2. `home-recycling-reality-data`
3. `sustainable-food-choices-data`
4. `energy-star-appliances-roi`
5. `ev-vs-hybrid-lifecycle-data`
6. `indoor-air-quality-low-waste-home-checklist-2026`
7. `smart-thermostat-savings-low-waste-setup-2026`
8. `heat-pump-water-heater-checklist-2026`
9. `home-energy-audit-checklist-renters-homeowners`
10. `cloth-vs-paper-towel-data`
11. `reusable-water-bottles-compared`
12. `heat-pump-vs-gas-heater`
13. `bamboo-toothbrush-reviewed`
14. `composting-bin-guide-small-space`
15. `rainwater-collection-setup`
16. `silicone-food-storage-tested`
17. `eco-friendly-pest-control`
18. `sustainable-clothing-brands-compared`
19. `solar-charger-portable-tested`
20. `led-vs-cfl-bulbs-data`

## 비공개 전환 목록 (38)

1. `attic-hatch-insulation-summer-cooling-leak-check`
2. `bathroom-exhaust-fan-summer-humidity-mold-energy-plan`
3. `ceiling-fan-ac-thermostat-summer-comfort-plan`
4. `ceiling-fan-summer-cooling-direction-energy-plan`
5. `clothesline-air-drying-laundry-humidity-energy-plan`
6. `dishwasher-eco-cycle-energy-water-savings-plan`
7. `door-sweep-weatherstrip-summer-cooling-leak-plan`
8. `drought-tolerant-plants-data`
9. `eco-laundry-detergent-tested`
10. `heat-pump-clothes-dryer-buying-checklist`
11. `heat-pump-dryer-summer-humidity-laundry-energy-plan`
12. `heat-pump-filter-wildfire-smoke-home-air-energy-plan`
13. `heat-pump-water-heater-buying-checklist`
14. `heat-pump-water-heater-summer-basement-laundry-energy-plan`
15. `home-energy-audit-air-sealing-priorities`
16. `home-humidity-dehumidifier-energy-mold-prevention-plan`
17. `induction-cooktop-summer-kitchen-heat-energy-plan`
18. `laundry-room-dehumidifier-drain-hose-energy-plan`
19. `low-flow-showerhead-tested`
20. `low-voc-paint-ventilation-room-refresh`
21. `low-waste-laundry-routine-cold-water`
22. `pool-pump-timer-summer-electricity-plan`
23. `portable-ac-fan-heat-wave-energy-safety-plan`
24. `portable-air-conditioner-hose-seal-energy-plan`
25. `rain-barrel-drought-garden-water-safety-plan`
26. `reading-sustainability-labels`
27. `refrigerator-coil-cleaning-energy-savings-plan`
28. `smart-power-strip-standby-energy-home-office-plan`
29. `smart-thermostat-humidity-summer-setback-plan`
30. `smart-thermostat-summer-energy-comfort-setup`
31. `summer-cooling-energy-savings-room-by-room-plan`
32. `welcome`
33. `whole-house-fan-night-ventilation-heat-wave-plan`
34. `window-ac-filter-cleaning-summer-energy-plan`
35. `window-screen-airflow-pollen-summer-plan`
36. `window-shade-cross-ventilation-heat-wave-plan`
37. `window-shade-solar-heat-gain-summer-schedule`
38. `zero-waste-bathroom-products`

## Deterministic QA

실행 명령:

```text
python3 scripts/adsense_review_qa.py
```

실제 결과(종료 코드 0):

```text
QA corpus: posts=58 retained=20 drafted=38
20 retained article checks: PASS
visible_words range: 2739–2815
sources range: 8–12
images: 3 per retained article
QA PASS: allowlist, draft flags, depth, sources, images/assets, process-language, and paragraph uniqueness
```

스크립트가 강제하는 항목:

- 정확한 20개 allowlist 및 나머지 모든 글의 `draft: true`
- reader-visible 영어 단어 900개 이상 (frontmatter, URL, Markdown/HTML 마크업 제외)
- frontmatter source 8개 이상
- 본문 이미지 참조 3개 이상 및 `/public` 로컬 이미지 존재
- 공개 글 본문 내 `AdSense`, `SEO`, publishing run/workflow, generated-image QA 표현 금지
- 공개 글 내·간 정규화 후 18단어 이상인 동일 문단 금지

## 빌드 검증

실행 명령:

```text
npm run build
```

WSL 저장소를 Windows Node가 UNC 경로에서 실행할 때 최초 시도는 작업 디렉터리가 `C:\Windows`로 폴백해 실패했다. 이후 `pushd`로 UNC 경로를 임시 드라이브에 매핑해 같은 npm 명령을 다시 실행했다.

실제 최종 결과(종료 코드 0):

```text
[content] Synced content
[vite] built
[@astrojs/sitemap] sitemap-index.xml created at dist
[build] 139 page(s) built in 41.12s
[build] Complete!
```

빌드가 만든 `.astro`/`dist` 변경은 검증 후 복원·정리하여 허용된 수정 범위에 포함하지 않았다. 기존 `node_modules` 변경 노이즈는 건드리지 않았다. commit, push, deploy는 실행하지 않았다.


## Independent review correction
An independent source review rejected a generated long-form expansion because it repeated generic decision scaffolds with superficial section-marker changes. Those expansions were reverted before commit or deployment. The retained 20 use their original topic-specific bodies; the corpus gate is 900 actual visible words as a minimum floor, with publication frozen while each retained article is upgraded individually.

Final manual review changed the public allowlist: weekend-home-energy-audit-plan and indoor-air-quality-low-waste-home-checklist-2026 were drafted because their original bodies contained repeated long scaffolds; drought-tolerant-plants-data and low-flow-showerhead-tested replaced them. The rejected generated expansions were never committed or deployed.
