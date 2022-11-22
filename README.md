# ExpTool

### exp_result()
- AB테스트의 결과를 분석할 수 있습니다.
- 'sample_id', 'converted', 'group'컬럼을 요구합니다.
- cl 파라미터를 통해 Confidence Level을 설정할 수 있습니다.(기본 95)
- su 파라미터를 통해 n수집 과정을 검토할 샘플 단위를 설정할 수 있습니다.(기본 100)
- 수집된 n에따른 결과를 데이터 프레임으로 반환합니다.
    - B-A의 차이(uplift)
    - B-A의 Confidence Interval
    - P value
    - 통계 유의성

- `exp_result_example.ipynb`를 통해 사용 예시를 볼 수 있습니다.


### Vexp
- 가상실험객체를 만들어 실험관련 지표를 계산할 수 있습니다.
- 조건 내에서 필요한 샘플 수를 계산할 수 있습니다.
- 기본 설정 지표는 아래와 같고 파라미터로 변경 가능합니다.
    - Confidence Level: 95%	
    - Margin of Error: 1%
    - p: 0.3

- `Vexp_example.ipynb`를 통해 사용 예시를 볼 수 있습니다.

### get_chance()
- 베타 분포를 이용한 베이지안 통계검증을 합니다.

### get_more_samples()
- get_chance의 역함수를 이용해 실험검증에 더 필요한 남은 샘플 수를 계산합니다.
- 현 실험의 증분이 계속 유지 될 것을 가정합니다.
